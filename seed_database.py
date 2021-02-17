"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
import requests
from pprint import pprint

import crud
import model
import server

os.system('dropdb recipeberry')
os.system('createdb recipeberry')

model.connect_to_db(server.app)
model.db.create_all()


def get_test_recipes():
    """Fetch recipes for testing purposes."""

    # response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=chicken")
    # test_meals = response.json().get("meals")[:5]
    # import pdb; pdb.set_trace()

    test_recipe_ids = [52795, 53020, 52937, 52830, 53011]

    test_recipes = []

    for id in test_recipe_ids:
        response = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
        response_data = response.json()
        test_recipes.append(response_data["meals"][0])

    pprint(json.dumps(test_recipes, indent=2))

    return test_recipes

get_test_recipes()


# Create 5 test users
for n in range(5):
    email = f"user{n}@test.com"  # A unique email
    password = "test"
    fname = f"user_fname{n}"
    lname = f"user_lname{n}"
    join_date = datetime.now()

    # TODO: create a user here
    user = crud.create_user(email, password, fname, lname, join_date)