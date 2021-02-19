"""CRUD operations."""

from model import db, User, Recipe, connect_to_db


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


#-----------------------------------------------------------------------------#


if __name__ == '__main__':
    from server import app
    connect_to_db(app)