"""Server for recipe berry app."""

from flask import Flask, render_template, request, flash, session, redirect, url_for
from jinja2 import StrictUndefined
from datetime import datetime, date
import statistics
from random import choice, randint, sample

from model import connect_to_db, User, Recipe
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

FEATURED_RECIPE = {"recipes" : [], "date" : date(1970, 1, 1)}


#-----------------------------------------------------------------------------#
#- HOMEPAGE ------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

@app.route("/")
def homepage():
    """Show homepage."""

    # If current date is FR date
        # Fetch FR recipe ids
    # Else
        # Get all recipes
        # Get 3 random recipes
        # Update FR date to today, current date
        # Update FR recipe ids

    global FEATURED_RECIPE

    current_date = date.today()

    if FEATURED_RECIPE["date"] == current_date:
        # print("***********INSIDE IF STATEMENT*************")
        featured_recipes = FEATURED_RECIPE["recipes"]
        # for recipe_id in recipe_ids:
        #     recipe = crud.get_recipe_by_id(recipe_id)
        # print(f"***********{recipe_id}*************")

    else:
        # print("***********INSIDE ELSE STATEMENT*************")
        FEATURED_RECIPE["date"] = current_date
        recipes = crud.get_recipes()

        # Get 3 random recipes
        # Use sample to avoid duplicates
        featured_recipes = sample(recipes, 3)
        # for recipe in featured_recipes:
        #     FEATURED_RECIPE["recipe_id"] = recipe.recipe_id
        FEATURED_RECIPE["recipes"] = featured_recipes
        # print(f"***********{recipe.recipe_id}*************")

    return render_template("homepage.html", featured_recipes=featured_recipes)


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
    """Show recipe details for a particular recipe."""

    recipe = crud.get_recipe_by_id(recipe_id)

    ratings = crud.get_ratings()
    rating_values = [rating.rating_value for rating in ratings]
    average_rating = statistics.mean(rating_values)

    user_id = session.get("user_id")

    if user_id != None:
        user_rating = crud.get_rating_by_user_and_recipe(user_id, recipe_id)
        is_favorite = crud.get_favorite_by_user_and_recipe(user_id, recipe_id)

    else:
        user_rating = None
        is_favorite = None

    return render_template("recipe_details.html",
                           recipe=recipe,
                           average_rating=average_rating,
                           user_rating=user_rating,
                           is_favorite=is_favorite)


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

    if request.method == "GET":

        cuisines = crud.get_cuisines()
        categories = crud.get_categories()
        ingredients = crud.get_ingredients()

        if session.get("user_id") == None:
            flash("Please log in to create a new recipe.")
            return redirect('/')

        return render_template("create_recipe.html",
                               cuisines=cuisines,
                               categories=categories,
                               ingredients=ingredients)

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

        # Get ingredient, measurement, and instruction items in a dictionary
        # If flat is False, returns all items as a list
        request_dict = request.form.to_dict(flat=False)

        for ingredient, measurement in zip(request_dict["ingredients"], request_dict["measurements"]):
            ingredient_object = crud.create_ingredient(ingredient)
            crud.create_recipe_ingredient(recipe.recipe_id, ingredient_object.ingredient_id, measurement)
        
        for step_num, instruction in enumerate(request_dict["instructions"]):
            crud.create_recipe_step(recipe.recipe_id, step_num + 1, instruction)

        # Get images from create recipe form
        for image in request_dict["images"]:
            image_object = crud.create_image(image)
            crud.create_recipe_image(recipe.recipe_id, image_object.image_id)

        if recipe:
            flash('Congrats! A new recipe was created.')

        else:
            flash('Error.')

        return redirect('/create_recipe')


@app.route("/recipes/<recipe_id>", methods=["POST"])
def archive_recipe(recipe_id):
    """Archive a recipe."""

    recipe = crud.archive_recipe(recipe_id)

    flash(f"You successfully deleted the {recipe.title} recipe from your account.")

    return redirect('/profile')


@app.route("/recipes/rating/<recipe_id>", methods=["POST"])
def rate_recipe(recipe_id):
    """Rate a recipe."""

    rating_value = request.form.get("rating_value")

    user_id = session.get("user_id")

    rating = crud.create_rating(rating_value, user_id, recipe_id)

    recipe = crud.get_recipe_by_id(recipe_id)

    flash(f"You successfully submitted a rating for the {recipe.title} recipe.")

    return redirect(f'/recipes/{recipe_id}')


@app.route("/recipes/favorite/<recipe_id>", methods=["POST"])
def create_favorite(recipe_id):
    """Create a favorite recipe."""

    user_id = session.get("user_id")

    crud.create_favorite(user_id, recipe_id)

    recipe = crud.get_recipe_by_id(recipe_id)

    return f"You added the {recipe.title} recipe to your Favorites."


@app.route("/recipes/unfavorite/<recipe_id>", methods=["POST"])
def delete_favorite(recipe_id):
    """Delete a favorite recipe."""

    user_id = session.get("user_id")

    crud.delete_favorite(user_id, recipe_id)

    recipe = crud.get_recipe_by_id(recipe_id)

    return f"You removed the {recipe.title} recipe to your Favorites."


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

    if session.get("user_id") == None:
        flash("Please log in to view your account.")
        return redirect('/')

    else:
        user_id = session.get("user_id")

        user = crud.get_user_by_id(user_id)

        return render_template("user_details.html", user=user)


@app.route("/profile/favorites")
def show_user_favorites():
    """Show favorite recipes for the logged in user."""

    if session.get("user_id") == None:
        flash("Please log in to view your account.")
        return redirect('/')

    else:
        user_id = session.get("user_id")

        user = crud.get_user_by_id(user_id)

        return render_template("user_favorite_recipes.html", user=user)


@app.route("/registration", methods=["GET"])
def show_registration():
    """Show user registration page."""

    return render_template("registration.html")


@app.route("/registration", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
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
            session["first_name"] = user.first_name
            flash(f"Welcome, {user.first_name}!")
            return redirect('/')

        # If user password does not match, flash error message
        else:
            flash("The password you entered is invalid. Please try again.")

    # If user does not exist, flash error message
    else:
        flash("The email address you entered has not been registered with Recipe Berry."
              "Please create a new account to start cooking with Recipe Berry.")

    return redirect('/authenticate')


@app.route("/logout", methods=["GET"])
def logout():
    """Handle user logout."""

    user_id = session.get("user_id")
    first_name = session.get("first_name")

    if user_id == None:
        flash("There is no user logged in to logout.")
    
    else:
        session["user_id"] = None
        session["first_name"] = None
        flash(f"Goodbye, {first_name}. Hope to cook with you again soon.")

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