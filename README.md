# RECIPE BERRY
**Recipe Berry** is a full stack web application designed to help everyday chefs organize and manage their favorite recipes. This app aims to help simplify the search of culinary pursuits by providing a central destination to discover, create, favorite, and review recipes. Using The Meal DB API, data was gathered to generate a library of recipes for users to explore. Users can customize their favorite recipes and rate recipes within the community. Find inspiration for your next meal with Recipe Berry.

Recipe Berry is created with love, sweat, and tears by Fionnie Pollack. You can connect with Fionnie by by [email](mailto:fionniepollack@gmail.com), [LinkedIn](https://www.linkedin.com/in/fionniepollack/), or [Twitter](https://twitter.com/fionniepollack).

## Table of Contents

1. [Technologies](#technologies)
2. [Features](#features)
3. [Why Recipe Berry?](#why)
4. [Installation](#installation)
5. [Looking Ahead](#future)
6. [Acknowledgments](#credits)
7. [Author](#author)

## <a name="technologies"></a>Technologies

**Front-end:** [HTML5](http://www.w3schools.com/html/), [CSS](http://www.w3schools.com/css/), [Bootstrap](http://getbootstrap.com), [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [jQuery](https://jquery.com/), [AJAX](http://api.jquery.com/jquery.ajax/)

**Back-end:** [Python](https://www.python.org/), [Flask](http://flask.pocoo.org/), [Jinja2](http://jinja.pocoo.org/docs/dev/), [PostgreSQL](http://www.postgresql.org/), [SQLAlchemy](http://www.sqlalchemy.org/)

**Libraries:** [SQLAlchemy](https://www.sqlalchemy.org)

**APIs:** [TheMealDB](https://www.themealdb.com/api.php)

## <a name="features"></a>Features

- Displays recipes with recipe details and ratings (Initial database was created with The Meal DB API)
- Includes a dropdown feature to view recipes by cuisine and category
- Displays three featured recipes of the day on the homepage with image hover features to explore their recipe details
- Provides a text search for recipes by title
- Allows users to login and logout
- Allows guests to create a new account to access logged in features
- Allows logged in users to create and delete recipes, rate recipes, and save recipes to their favorites list
- Includes a responsive navigation bar to adjust to any screen size

## <a name="why"></a>Why Recipe Berry?

Recipe Berry was developed as my solo capstone project at Hackbright Academy. Inspired by my love for food and exploring various cuisines in the kitchen, I designed Recipe Berry to share my passion with others. Often finding it difficult to find recipes in one place, I was motivated to develop a central destination to store, manage, and organize all my favorite recipes. Recipe Berry is the virtual cookbook organizer I wish I had and I hope you enjoy using it too.

## <a name="installation"></a>Installation
If you would like to run Recipe Berry locally, please follow these instructions.

### Prerequisites:

- Install [PostgreSQL](https://www.postgresql.org/download/).
- Install [Python](https://www.python.org/downloads/).

### Set up Recipe Berry:

1. Clone this repository:

```$ git clone https://github.com/fionniepollack/recipe-berry.git```

2. Create a virtual environment and activate it:

 Mac:

    $ virtualenv env
    $ source env/bin/activate

 Windows:

    $ virtualenv env --always-copy
    $ source env/bin/activate

3. Install the dependencies:

```(env) $ pip install -r requirements.txt```

4. Create the database with the name `recipeberry`:

```(env) $ createdb recipeberry```

5. Seed the database:

```(env) $ python3 seed_database.py```

6. Start the server to run the app:

```(env) $ python3 server.py```

7. Finally, go to `http://localhost:5000/` in your browser to start using Recipe Berry!

## <a name="future"></a>Looking Ahead

Features

- Create an advanced search feature to search cuisines, categories, and ingredients
- Allow users to update authored recipes
- Allow users to filter recipes by rating

Other:

- More tests!

## <a name="credits"></a>Acknowledgments

Special thank you to my family, friends, mentors, and fellow Hackbright advisors and cohort-mates for the unwavering support, guidance, mentorship, and inspiration.

## <a name="author"></a>Author
Fionnie Pollack is a Software Engineer living in Knoxville, TN.
[Email](mailto:fionniepollack@gmail.com) | [LinkedIn](https://www.linkedin.com/in/fionniepollack/) | [Twitter](https://twitter.com/fionniepollack).

## Happy Cooking! 🍓
