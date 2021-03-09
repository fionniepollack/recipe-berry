"""CRUD operations."""

from model import (db,
                   User,
                   Recipe,
                   Cuisine,
                   RecipeStep,
                   RecipeIngredient,
                   Ingredient,
                   RecipeCategory,
                   Category,
                   RecipeImage,
                   Image,
                   Rating,
                   Favorite,
                   connect_to_db)

#-----------------------------------------------------------------------------#
#- USER ----------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

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


def get_users():
    """Return all users."""

    users = User.query.all()

    return users


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def get_user_by_id(user_id):
    """Return a particular user."""

    user = User.query.get(user_id)

    return user


#-----------------------------------------------------------------------------#
#- RECIPE --------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

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


def archive_recipe(recipe_id):
    """Archive a recipe."""

    recipe = get_recipe_by_id(recipe_id)

    recipe.is_active = False

    db.session.commit()

    return recipe


#-----------------------------------------------------------------------------#
#- CUISINE -------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

def create_cuisine(cuisine_name):
    """Create and return a new cuisine."""

    cuisine = Cuisine(cuisine_name = cuisine_name)

    db.session.add(cuisine)
    db.session.commit()

    return cuisine


def get_cuisines():
    """Return all cuisines in alphabetical order."""

    cuisines = Cuisine.query.order_by(Cuisine.cuisine_name).all()

    return cuisines


def get_cuisine_by_id(cuisine_id):
    """Return a particular cuisine given a cuisine_id."""

    cuisine = Cuisine.query.get(cuisine_id)

    return cuisine


def get_cuisine_id_by_cuisine_name(cuisine_name):
    """Given a cuisine_name, return a particular cuisine_id."""

    # Get cuisine object that matches the given cuisine_name 
    cuisine_match = Cuisine.query.filter(Cuisine.cuisine_name == cuisine_name).first()

    cuisine_id = cuisine_match.cuisine_id

    return cuisine_id


#-----------------------------------------------------------------------------#
#- RECIPE STEP ---------------------------------------------------------------#
#-----------------------------------------------------------------------------#

def create_recipe_step(recipe_id, step_num, instruction):
    """Create and return a new recipe step."""

    recipe_step = RecipeStep(recipe_id = recipe_id, 
                             step_num = step_num,
                             instruction = instruction)

    db.session.add(recipe_step)
    db.session.commit()

    return recipe_step


#-----------------------------------------------------------------------------#
#- RECIPE INGREDIENT ---------------------------------------------------------#
#-----------------------------------------------------------------------------#

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

    # Check if ingredient already exists
    ingredient = Ingredient.query.filter(Ingredient.ingredient_name == ingredient_name).first()

    # If ingredient does not already exists, create it and add to database
    if not ingredient:
        ingredient = Ingredient(ingredient_name = ingredient_name.title())

        db.session.add(ingredient)
        db.session.commit()

    return ingredient


def get_ingredients():
    """Return all ingredients in alphabetical order."""

    ingredients = Ingredient.query.order_by(Ingredient.ingredient_name).all()

    return ingredients


# def upsert_ingredients(ingredient_name):
#     """Upsert."""
#     ingredient = Ingredient.query.filter(Ingredient.ingredient_name == ingredient_name).first()

#     import pdb; pdb.set_trace()


#-----------------------------------------------------------------------------#
#- RECIPE CATEGORY -----------------------------------------------------------#
#-----------------------------------------------------------------------------#

def create_category(category_name):
    """Create and return a new category."""

    category = Category(category_name = category_name)

    db.session.add(category)
    db.session.commit()

    return category


def get_categories():
    """Return all categories in alphabetical order."""

    categories = Category.query.order_by(Category.category_name).all()

    return categories


def get_category_by_id(category_id):
    """Return a particular category given a category_id."""

    category = Category.query.get(category_id)

    return category


def get_category_by_name(category_name):
    """Return a Category object that matches the given category_name"""

    category = Category.query.filter(Category.category_name == category_name).first()

    return category


def create_recipe_category(recipe_id, category_id):
    """Given a recipe_id and category_name, create and return a new recipe category."""

    recipe_category = RecipeCategory(recipe_id = recipe_id,
                                     category_id = category_id)

    db.session.add(recipe_category)
    db.session.commit()

    return recipe_category


#-----------------------------------------------------------------------------#
#- RECIPE IMAGE --------------------------------------------------------------#
#-----------------------------------------------------------------------------#

def create_image(image_url):
    """Create and return a new image."""

    image = Image(image_url = image_url)

    db.session.add(image)
    db.session.commit()

    return image


def create_recipe_image(recipe_id, image_id):
    """Given a recipe_id and image_url, create and return a new recipe image."""

    recipe_image = RecipeImage(recipe_id = recipe_id,
                               image_id = image_id)

    db.session.add(recipe_image)
    db.session.commit()

    return recipe_image


#-----------------------------------------------------------------------------#
#- RATING ----------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

def create_rating(rating_value, user_id, recipe_id):
    """Create and return a new rating given a rating_value, user_id, and recipe_id."""

    rating = Rating(rating_value = rating_value,
                    user_id = user_id,
                    recipe_id = recipe_id)

    db.session.add(rating)
    db.session.commit()

    return rating


def get_ratings():
    """Return all ratings."""

    ratings = Rating.query.all()

    return ratings


def get_rating_by_user_and_recipe(user_id, recipe_id):
    """Return a particular rating given a user_id and recipe_id."""

    rating = Rating.query.filter(Rating.user_id == user_id, Rating.recipe_id == recipe_id).first()

    return rating


#-----------------------------------------------------------------------------#
#- FAVORITE ------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

def create_favorite(user_id, recipe_id):
    """Given a user_id and recipe_id, create and return a favorite."""

    favorite = Favorite(user_id = user_id,
                        recipe_id = recipe_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite


def get_favorite_by_user_and_recipe(user_id, recipe_id):
    """Given a user_id and recipe_id, return a particular favorite"""

    favorite = Favorite.query.filter(Favorite.user_id == user_id, Favorite.recipe_id == recipe_id).first()

    return favorite


def delete_favorite(user_id, recipe_id):
    """Given a user_id and recipe_id, delete and return a favorite."""

    favorite_to_delete = get_favorite_by_user_and_recipe(user_id, recipe_id)

    db.session.delete(favorite_to_delete)
    db.session.commit()

    return favorite_to_delete


def get_favorites_by_user_id(user_id):
    """Given a user_id, return all favorites."""

    favorites = Favorite.query.filter(Favorite.user_id == user_id).all()

    return favorites


#-----------------------------------------------------------------------------#


if __name__ == '__main__':
    from server import app
    connect_to_db(app)