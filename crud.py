"""CRUD operations."""

from model import db, User, Recipe, Cuisine, RecipeStep, RecipeIngredient, connect_to_db


def create_user(email, password, first_name, last_name, join_date):
    """Create and return a new user."""

    user = User(email = email,
                password = password,
                first_name = first_name,
                last_name = last_name,
                join_date = join_date)

    db.session.add(user)
    db.session.commit()

    return user


def create_recipe(title, **kwargs):
    """Create and return a new recipe."""

    recipe = Recipe(title=title,
                    description = kwargs.get("description"),
                    prep_time = kwargs.get("prep_time"),
                    cook_time = kwargs.get("cook_time"),
                    total_time = kwargs.get("total_time"),
                    serving_qty = kwargs.get("serving_qty"),
                    source = kwargs.get("source"),
                    user_id = kwargs.get("user_id"))

    db.session.add(recipe)
    db.session.commit()

    return recipe


def get_recipes():
    """Return all recipes."""

    recipes = Recipe.query.all()

    return recipes


def get_recipe_by_id(recipe_id):
    """Return a particular recipe."""

    recipe = Recipe.query.get(recipe_id)

    return recipe


def create_cuisine(cuisine_name):
    """Create and return a new cuisine."""

    cuisine = Cuisine(cuisine_name=cuisine_name)

    db.session.add(cuisine)
    db.session.commit()

    return cuisine


def get_cuisines():
    """Return all cuisines."""

    cuisines = Cuisine.query.all()

    return cuisines


def get_cuisine_id_by_cuisine_name(cuisine_name):
    """Given a cuisine_name, return a particular cuisine_id."""

    cuisine_id = Cuisine.query.filter(Cuisine.cuisine_name == cuisine_name)

    return cuisine_id


def create_recipe_step(recipe_id, step_num, instruction):
    """Create and return a new recipe step."""

    recipe_step = RecipeStep(recipe_id = recipe_id, 
                             step_num = step_num,
                             instruction = instruction)

    db.session.add(recipe_step)
    db.session.commit()

    return recipe_step


def create_recipe_ingredient(recipe_id, measurement):
    """Create and return a new recipe ingredient."""

    recipe_ingredient = RecipeIngredient(recipe_id = recipe_id,
                                         measurement = measurement)

    db.session.add(recipe_ingredient)
    db.session.commit()

    return recipe_ingredient


#-----------------------------------------------------------------------------#


if __name__ == '__main__':
    from server import app
    connect_to_db(app)