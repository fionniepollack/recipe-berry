"""Server for recipe berry app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, User
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("homepage.html")


@app.route("/recipes")
def all_recipes():
    """View all recipes."""

    recipes = crud.get_recipes()

    return render_template('all_recipes.html', recipes=recipes)


@app.route("/recipes/<recipe_id>")
def show_recipe(recipe_id):
    """Show details for a particular recipe."""

    recipe = crud.get_recipe_by_id(recipe_id)

    return render_template("recipe_details.html", recipe=recipe)


@app.route("/cuisines")
def all_cuisines():
    """View all cuisines."""

    cuisines = crud.get_cuisines()

    return render_template('all_cuisines.html', cuisines=cuisines)


@app.route("/authenticate", methods=["POST"])
def authenticate():
    """Handle login and check user credentials."""

    # Handle login
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    # Check to make sure the user is in DB
    if user:

        # Check if password matches passowrd in db for user
        if password == user.password:
            session["user_id"] = user.user_id
            flash("Logged in!")

        # If user password does not match, flash error message
        else:
            flash("Invalid password.")

    # If user does not exist, flash error message
    else:
        flash("User does not exist.")

    return redirect('/')



#-----------------------------------------------------------------------------#


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)