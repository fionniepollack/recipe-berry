"""CRUD operations."""

from model import *
# from model import db, User, Recipe, Cuisine, RecipeStep, RecipeIngredient, Ingredient, Category, RecipeCategory, connect_to_db


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
                    user_id = kwargs.get("user_id"),
                    cuisine_id = kwargs.get("cuisine_id"))

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

    cuisine = Cuisine(cuisine_name = cuisine_name)

    db.session.add(cuisine)
    db.session.commit()

    return cuisine


def get_cuisines():
    """Return all cuisines."""

    cuisines = Cuisine.query.all()

    return cuisines


def get_cuisine_id_by_cuisine_name(cuisine_name):
    """Given a cuisine_name, return a particular cuisine_id."""

    # Get cuisine object that matches the given cuisine_name 
    cuisine_match = Cuisine.query.filter(Cuisine.cuisine_name == cuisine_name).first()

    cuisine_id = cuisine_match.cuisine_id

    return cuisine_id


def create_recipe_step(recipe_id, step_num, instruction):
    """Create and return a new recipe step."""

    recipe_step = RecipeStep(recipe_id = recipe_id, 
                             step_num = step_num,
                             instruction = instruction)

    db.session.add(recipe_step)
    db.session.commit()

    return recipe_step


def create_recipe_ingredient(recipe_id, ingredient_id, measurement):
    """Create and return a new recipe ingredient."""

    recipe_ingredient = RecipeIngredient(recipe_id = recipe_id,
                                         ingredient_id = ingredient_id,
                                         measurement = measurement)

    db.session.add(recipe_ingredient)
    db.session.commit()

    return recipe_ingredient


def create_ingredient(ingredient_name):
    """Create and return a new ingredient."""

    ingredient = Ingredient(ingredient_name = ingredient_name)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient


def create_category(category_name):
    """Create and return a new category."""

    category = Category(category_name = category_name)

    db.session.add(category)
    db.session.commit()

    return category


def create_recipe_category(recipe_id, category_name):
    """Given a recipe_id and category_name, create and return a new recipe category."""

    # Get category object that matches the given category_name 
    category_match = Category.query.filter(Category.category_name == category_name).first()

    category_id = category_match.category_id

    recipe_category = RecipeCategory(recipe_id = recipe_id,
                                     category_id = category_id)

    db.session.add(recipe_category)
    db.session.commit()

    return recipe_category



#-----------------------------------------------------------------------------#


if __name__ == '__main__':
    from server import app
    connect_to_db(app)