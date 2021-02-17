"""CRUD operations."""

from model import db, User, connect_to_db


# Functions start here!
def create_user(email, password, fname, lname, join_date):
    """Create and return a new user."""

    user = User(email=email, password=password, fname=fname, lname=lname, join_date=join_date)

    db.session.add(user)
    db.session.commit()

    return user


def create_recipe(title, **kwargs):
    """Create and return new recipe."""

    recipe = Recipe(
                    title=title,
                    description = kwargs.get("description"),
                    prep_time = kwargs.get("prep_time"),
                    cook_time = kwargs.get("cook_time"),
                    total_time = kwargs.get("total_time"),
                    serving_qty = kwargs.get("serving_qty"),
                    recipe_notes = kwargs.get("recipe_notes"),
                    source = kwargs.get("source")
    )

    db.session.add(recipe)
    db.session.commit()

    return recipe


if __name__ == '__main__':
    from server import app
    connect_to_db(app)