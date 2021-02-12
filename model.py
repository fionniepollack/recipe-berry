"""Models for recipe berry app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    join_date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Recipe(db.Model):
    """A recipe."""

    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    prep_time = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    total_time = db.Column(db.Integer)
    serving_qty = db.Column(db.Integer)
    recipe_notes = db.Column(db.Text)
    source = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisines.cusine_id'))

    user = db.relationship('User', backref='recipes')
    cuisine = db.relationship('Cuisine', backref='recipes')

    def __repr__(self):
        return f'<Recipe recipe_id={self.recipe_id} title={self.title}>'


class Cuisine(db.Model):
    """A cuisine."""

    __tablename__ = 'cuisines'

    cusine_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cuisine = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'<Cuisine cusine_id={self.cusine_id} cuisine={self.cuisine}>'


class RecipeSteps(db.Model):
    """A recipe step."""

    __tablename__ = 'recipe_steps'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    step_num = db.Column(db.Integer)
    instruction = db.Column(db.Text)

    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe.recipe_id'))

    recipe = db.relationship('Recipe', backref='recipe_steps')

    def __repr__(self):
        return f'<RecipeSteps id={self.id} step_num={self.step_num} instruction={self.instruction}>'


class RecipeIngredient(db.Model):
    """A recipe ingredient."""

    __tablename__ = 'recipe_ingredients'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    measurement_qty = db.Column(db.Integer)

    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe.recipe_id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('cuisines.cusine_id'))
    measurement_id = db.Column(db.Integer, db.ForeignKey('cuisines.cusine_id'))

    recipe = db.relationship('Recipe', backref='recipe_ingredients')
    ingredient_name = db.relationship('Ingredient', backref='recipe_ingredients')
    measurement_description = db.relationship('MeasurementUnit', backref='recipe_ingredients')

    def __repr__(self):
        return f'<RecipeIngredient id={self.id}>'


class Ingredient(db.Model):
    """An ingredient."""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ingredient_name = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'<Ingredient ingredient_id={self.ingredient_id} ingredient_name={self.ingredient_name}>'



def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
