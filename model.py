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
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
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
    source = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisines.cuisine_id'))

    user = db.relationship('User', backref='recipes')
    cuisine = db.relationship('Cuisine', backref='recipes')

    # Defining the relationship between the category class and the recipe table
    categories = db.relationship("Category", secondary="recipe_categories")

    def __repr__(self):
        return f'<Recipe recipe_id={self.recipe_id} title={self.title}>'


class Cuisine(db.Model):
    """A cuisine."""

    __tablename__ = 'cuisines'

    cuisine_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cuisine_name = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'<Cuisine cuisine_id={self.cuisine_id} cuisine_name={self.cuisine_name}>'


class RecipeStep(db.Model):
    """A recipe step."""

    __tablename__ = 'recipe_steps'

    step_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    step_num = db.Column(db.Integer, nullable=False)
    instruction = db.Column(db.Text, nullable=False)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))

    recipe = db.relationship('Recipe', backref='recipe_steps')

    def __repr__(self):
        return f'<RecipeStep step_id={self.step_id} step_num={self.step_num} instruction={self.instruction}>'


class RecipeIngredient(db.Model):
    """A recipe ingredient."""

    __tablename__ = 'recipe_ingredients'

    recipe_ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    measurement = db.Column(db.String, nullable=True)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))

    recipe = db.relationship('Recipe', backref='recipe_ingredients')
    ingredient_name = db.relationship('Ingredient', backref='recipe_ingredients')

    def __repr__(self):
        return f'<RecipeIngredient id={self.id}>'


class Ingredient(db.Model):
    """An ingredient."""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    ingredient_name = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'<Ingredient ingredient_id={self.ingredient_id} ingredient_name={self.ingredient_name}>'


class RecipeCategory(db.Model):
    """Associative table for the relationships of recipe and category."""

    __tablename__ = 'recipe_categories'

    recipe_category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))

    recipe = db.relationship('Recipe', backref='recipe_categories')
    category = db.relationship('Category', backref='recipe_categories')

    def __repr__(self):
        return f'<RecipeCategory recipe_category_id={self.recipe_category_id}>'


class Category(db.Model):
    """A category."""

    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_name = db.Column(db.String)

    # Defining the relationship between the category class and the recipe table
    recipes = db.relationship("Recipe", secondary="recipe_categories")

    def __repr__(self):
        return f'<Category category_id={self.category_id} category_name={self.category_name}>'


# class RecipeDietType(db.Model):
#     """A recipe diet type."""

#     __tablename__ = 'recipe_diet_types'

#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     diet_typet_id = db.Column(db.Integer)

#     recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))

#     recipe = db.relationship('Recipe', backref='recipe_diet_types')

#     def __repr__(self):
#         return f'<RecipeDietType id={self.id}>'


# class DietTypes(db.Model):
#     """A diet type."""

#     __tablename__ = 'diet_types'

#     diet_type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     diet = db.Column(db.String)

#     def __repr__(self):
#         return f'<DietTypes diet_type_id={self.diet_type_id} diet={self.diet}>'


class RecipeImage(db.Model):
    """A recipe image."""

    __tablename__ = 'recipe_images'

    recipe_image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    image_id = db.Column(db.Integer, db.ForeignKey('images.image_id'))

    recipe = db.relationship('Recipe', backref='recipe_images')
    image_name = db.relationship('Image', backref='recipe_images')

    def __repr__(self):
        return f'<RecipeImage id={self.id}>'


class Image(db.Model):
    """An image."""

    __tablename__ = 'images'

    image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    image_url = db.Column(db.String)

    def __repr__(self):
        return f'<Image image_id={self.image_id} image={self.image}>'


#-----------------------------------------------------------------------------#


def connect_to_db(flask_app, db_uri='postgresql:///recipeberry', echo=True):
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