"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
import requests
from pprint import pprint
from faker import Faker

import crud
import model
import server

os.system('dropdb recipeberry')
os.system('createdb recipeberry')

fake = Faker()


def create_test_users():
    """Create test users using Faker module."""

    test_users = []

    for n in range(5):
        first_name = fake.unique.first_name()
        last_name = fake.unique.last_name()
        email = f"{first_name}.{last_name}@recipeberry.com"
        password = "test"
        join_date = datetime.now()

        user = crud.create_user(email, password, first_name, last_name, join_date)
        test_users.append(user)

    # Create admin user that will always remain the same unlike users created with Faker
    admin_user = crud.create_user("admin@recipeberry.com",
                                  "admin",
                                  "admin_first_name" ,
                                  "admin_last_name",
                                  "2021-02-25 21:24:17.727103")

    return test_users


def get_test_recipes():
    """Fetch recipes for testing purposes from TheMealDB API."""

    # response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=chicken")
    # test_meals = response.json().get("meals")[:5]
    # import pdb; pdb.set_trace()


    # Five random recipe id's sourced from TheMealDB API
    test_recipe_ids = [52795, 53020, 52937, 52830, 53011]

    test_recipes = []

    for id in test_recipe_ids:
        response = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
        response_data = response.json()

        # Example response data
        """
        {
            "meals": [{
                "idMeal": "52772",
                "strMeal": "Teriyaki Chicken Casserole",
                "strDrinkAlternate": null,
                "strCategory": "Chicken",
                ...
            }]
        }
        """

        test_recipes.append(response_data["meals"][0])

    # pprint(json.dumps(test_recipes, indent=2))

    return test_recipes


def create_test_recipes(test_users):
    """Create test recipes."""

    test_recipes_in_db = []

    # Capture test recipes from get_test_recipes() function
    test_recipes = get_test_recipes()

    for test_recipe in test_recipes:
        user = choice(test_users)
        prep_time = randint(5,20)
        cook_time = randint(10,30)

        kwargs = {"title" : test_recipe["strMeal"],
                  "description" : "Sample recipe from TheMealDB API",
                  "prep_time" : prep_time,
                  "cook_time" : cook_time,
                  "total_time" : prep_time + cook_time,
                  "serving_qty" : randint(1,5),
                  "source" : "Sample recipe from TheMealDB API",
                  "user_id" : user.user_id,
                  "cuisine_id" : crud.get_cuisine_id_by_cuisine_name(test_recipe["strArea"])}

        recipe = crud.create_recipe(**kwargs)
        test_recipes_in_db.append(recipe)
        
        # Seed database with recipe step(s)
        crud.create_recipe_step(recipe.recipe_id, 1, test_recipe["strInstructions"])

        # Seed database with recipe ingredients, measurements
        # Using create_test_recipe_ingredients() function
        create_test_recipe_ingredients(test_recipe, recipe.recipe_id)

        # Seed database with recipe category
        category = crud.get_category_by_name(test_recipe["strCategory"])
        crud.create_recipe_category(recipe.recipe_id, category.category_id)

        # Seed database with an image
        image = create_test_image(test_recipe)

        # Seed database with recipe image
        crud.create_recipe_image(recipe.recipe_id, image.image_id)

    return test_recipes_in_db


def get_test_cuisines():
    """Fetch cuisines for testing purposes from TheMealDB API."""

    test_cuisines = []

    response = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?a=list")
    cuisines_in_api = response.json().get("meals")

    for cuisine in cuisines_in_api:
        cuisine = cuisine["strArea"]
        test_cuisines.append(cuisine)

    return test_cuisines


def create_test_cuisines():
    """Create test cuisines."""

    test_cuisines_in_db = []

    # Capture test cuisines from get_test_cuisines() function
    test_cuisines = get_test_cuisines()

    for test_cuisine in test_cuisines:
        cuisine = crud.create_cuisine(test_cuisine)
        test_cuisines_in_db.append(cuisine)

    return test_cuisines_in_db


def create_test_recipe_ingredients(test_recipe, recipe_id):
    """Create test recipe ingredients."""

    num = 1

    while True:
        measurement = test_recipe.get(f"strMeasure{num}")
        ingredient = test_recipe.get(f"strIngredient{num}")

        if measurement == " " or measurement == "" or measurement == None:
            break

        else:
            # Check if ingredient found in JSON matches an ingredient in the database
            # Use .title() to make the first letter of all ingredients capitalized
            ingredient_in_db = model.Ingredient.query.filter(model.Ingredient.ingredient_name == ingredient.title()).first()
            recipe_ingredient = crud.create_recipe_ingredient(recipe_id, ingredient_in_db.ingredient_id, measurement)

        num = num + 1


def get_test_ingredients():
    """Fetch ingredients for testing purposes from TheMealDB API."""

    test_ingredients = []

    response = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?i=list")
    ingredients_in_api = response.json().get("meals")


    for ingredient in ingredients_in_api:
        ingredient = ingredient["strIngredient"]
        test_ingredients.append(ingredient)

    # Convert test_ingredients list to a set
    # To remove duplicate ingredients in JSON from TheMealDB API
    test_ingredients_set = set(test_ingredients)

    return test_ingredients_set


def create_test_ingredients():
    """Create test ingredients."""

    test_ingredients_in_db = []

    # Capture test ingredients from get_test_ingredients() function
    test_ingredients = get_test_ingredients()

    for test_ingredient in test_ingredients:

        # Use .title() to make the first letter of all ingredients capitalized
        ingredient = crud.create_ingredient(test_ingredient.title())
        test_ingredients_in_db.append(ingredient)

    return test_ingredients_in_db


def get_test_categories():
    """Fetch categories for testing purposes from TheMealDB API."""

    test_categories = []

    response = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php")
    categories_in_api = response.json().get("categories")

    for category in categories_in_api:
        category = category["strCategory"]
        test_categories.append(category)

    return test_categories


def create_test_categories():
    """Create test categories."""

    test_categories_in_db = []

    # Capture test categories from get_test_categories() function
    test_categories = get_test_categories()

    for test_category in test_categories:
        category = crud.create_category(test_category)
        test_categories_in_db.append(category)

    return test_categories_in_db


def create_test_image(test_recipe):
    """Create test image."""

    image_in_api = test_recipe["strMealThumb"]

    image = crud.create_image(image_in_api)

    return image


#-----------------------------------------------------------------------------#


if __name__ == '__main__':
    model.connect_to_db(server.app)
    model.db.create_all()

    # Create test users in database
    test_users = create_test_users()

    # Create test cuisines in database
    test_cuisines_in_db = create_test_cuisines()

    # Create test ingredients in database
    test_ingredients_in_db = create_test_ingredients()

    # Create test categories in database
    create_test_categories()

    # Create test recipes in database
    create_test_recipes(test_users)