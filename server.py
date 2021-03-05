"""Server for recipe berry app."""

from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined
from datetime import datetime

from model import connect_to_db, User, Recipe
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


#-----------------------------------------------------------------------------#
#- HOMEPAGE ------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("homepage.html")


#-----------------------------------------------------------------------------#
#- RECIPE ROUTES -------------------------------------------------------------#
#-----------------------------------------------------------------------------#


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


@app.route("/cuisines/<cuisine_id>")
def show_cuisine(cuisine_id):
    """Show recipes for a particular cuisine."""

    cuisine = crud.get_cuisine_by_id(cuisine_id)

    return render_template("cuisine_recipes.html", cuisine=cuisine)


@app.route("/categories")
def all_categories():
    """View all categories."""

    categories = crud.get_categories()

    return render_template('all_categories.html', categories=categories)


@app.route("/categories/<category_id>")
def show_category(category_id):
    """Show recipes for a particular category."""

    category = crud.get_category_by_id(category_id)

    return render_template("category_recipes.html", category=category)


@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    """Show create recipe page."""

    cuisines = crud.get_cuisines()
    categories = crud.get_categories()

    if request.method == "GET":

        if session.get("user_id") == None:
            flash("Please log in to create a new recipe.")
            return redirect('/')

        return render_template("create_recipe.html", cuisines=cuisines, categories=categories)

    elif request.method == "POST":

        kwargs = {"title" : request.form.get("title"),
                  "description" : request.form.get("description"),
                  "prep_time" : request.form.get("prep_time"),
                  "cook_time" : request.form.get("cook_time"),
                  "total_time" : request.form.get("total_time"),
                  "serving_qty" : request.form.get("serving_qty"),
                  "source" : request.form.get("source"),
                  "user_id" : session.get("user_id"),
                  "cuisine_id" : request.form.get("cuisine_id")}

        recipe = crud.create_recipe(**kwargs)

        category_id = request.form.get("category_id")
        crud.create_recipe_category(recipe.recipe_id, category_id)


        # Get ingredient items in a dictionary
        # If flat is False, returns all items as a list
        request_dict = request.form.to_dict(flat=False)
        print(f"********{request.form}*********")

        print('PRINTING request_dict...')
        print(request_dict)
        print('END request_dict')

        # ingredient_id = request.form.get("ingredients")


        #TODO
        #get ingredients
        #get instructions
        #get image

        if recipe:
            flash('Congrats! A new recipe was created.')

        else:
            flash('Error.')

        return redirect('/create_recipe')


#-----------------------------------------------------------------------------#
#- USER ROUTES ---------------------------------------------------------------#
#-----------------------------------------------------------------------------#

@app.route("/users")
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template('all_users.html', users=users)


@app.route("/profile")
def show_user():
    """Show details for the logged in user."""

    user_id = session.get("user_id")

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


@app.route("/registration", methods=["GET"])
def show_registration():
    """Show user registration page."""

    return render_template("registration.html")


@app.route("/registration", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")
    first_name = request.form.get("password")
    last_name = request.form.get("password")
    join_date = datetime.now()

    user = crud.get_user_by_email(email)

    if user:
        flash('A user already exists with that email. Try again.')

    else:
        crud.create_user(email, password, first_name, last_name, join_date)
        flash('User was created sucessfully. Please log in.')

    return redirect('/')


@app.route("/authenticate", methods=["GET"])
def show_login():
    """Show user login page."""

    return render_template("login.html")


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
            return redirect('/')

        # If user password does not match, flash error message
        else:
            flash("Invalid password.")

    # If user does not exist, flash error message
    else:
        flash("User does not exist.")

    return redirect('/authenticate')


@app.route("/logout", methods=["GET"])
def logout():
    """Handle user logout."""

    user_id = session.get("user_id")

    if user_id == None:
        flash("There is no user logged in to logout.")
    
    else:
        session["user_id"] = None
        flash("User has been successfully logged out.")

    return redirect('/')


#-----------------------------------------------------------------------------#
#- SEARCH ROUTES -------------------------------------------------------------#
#-----------------------------------------------------------------------------#

@app.route("/search", methods=["GET"])
def search():
    """Search."""

    # Get search_string input from search form
    raw_search_string = request.args["search_string"]

    # Surround raw_search_string with % as a wildcard
    search_string = f"%{raw_search_string}%"

    # Case insensitive search on recipe titles
    results = Recipe.query.filter(Recipe.title.ilike(search_string)).all()

    return render_template('all_recipes.html', recipes=results)


#-----------------------------------------------------------------------------#


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)