"""CRUD operations."""

from model import db, User, connect_to_db


# Functions start here!
def create_user(email, password, fname, lname, join_date):
    """Create and return a new user."""

    user = User(email=email, password=password, fname=fname, lname=lname, join_date=join_date)

    db.session.add(user)
    db.session.commit()

    return user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)