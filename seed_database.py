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

    # Capture test recipes from get_test_recipes() function
    test_recipes = get_test_recipes()

    for recipe in test_recipes:
        user = choice(test_users)
        prep_time = randint(5,20)
        cook_time = randint(10,30)

        kwargs = {"title" : recipe["strMeal"],
                  "description" : "Sample recipe from TheMealDB API",
                  "prep_time" : prep_time,
                  "cook_time" : cook_time,
                  "total_time" : prep_time + cook_time,
                  "serving_qty" : randint(1,5),
                  "source" : "Sample recipe from TheMealDB API",
                  "user_id" : user.user_id}

        recipe = crud.create_recipe(**kwargs)



#-----------------------------------------------------------------------------#


if __name__ == '__main__':
    model.connect_to_db(server.app)
    model.db.create_all()

    test_users = create_test_users()
    create_test_recipes(test_users)