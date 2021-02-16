"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb recipeberry')
os.system('createdb recipeberry')

model.connect_to_db(server.app)
model.db.create_all()


# Create 5 test users
for n in range(5):
    email = f'user{n}@test.com'  # A unique email
    password = 'test'
    fname = f'user_fname{n}'
    lname = f'user_lname{n}'
    join_date = datetime.now()

    # TODO: create a user here
    user = crud.create_user(email, password, fname, lname, join_date)