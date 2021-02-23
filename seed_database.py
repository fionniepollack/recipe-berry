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

        # Seed database with recipe ingredient measurements 
        # Using create_test_measurements() function
        create_test_measurements(test_recipe, recipe.recipe_id)

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


def create_test_measurements(test_recipe, recipe_id):
    """Create test recipe ingredient measurements."""

    numMeasure = 1

    while True:
        measurement = test_recipe.get(f"strMeasure{numMeasure}")

        if measurement == " " or measurement == "" or measurement == None:
            break

        else:
            recipe_ingredient_measurement = crud.create_recipe_ingredient(recipe_id, measurement)

        numMeasure = numMeasure + 1


# def create_test_ingredients(test_recipe, recipe_id):
#     """Create test recipe ingredients."""

#     n = 1

#     while True:
#         ingredient = test_recipe.get(f"strMeasure{n}")
#         if ingredient != "" or ingredient != None:
#             recipe_ingredient = crud.create_recipe_ingredient(recipe_id, measurement)
#             n += 1
        
#         else:
#             break


#-----------------------------------------------------------------------------#


if __name__ == '__main__':
    model.connect_to_db(server.app)
    model.db.create_all()

    # Create test users in database
    test_users = create_test_users()

    # Create test cuisines in database
    test_cuisines_in_db = create_test_cuisines()

    # Create test recipes in database
    create_test_recipes(test_users)