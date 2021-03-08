"use strict";

// Button to create a favorite recipe
const favoriteRecipeButton = $('#favorite-recipe');
favoriteRecipeButton.on('click', favoriteRecipe);


// Button to delete a favorite recipe
const unfavoriteRecipeButton = $('#unfavorite-recipe');
unfavoriteRecipeButton.on('click', unfavoriteRecipe);


function favoriteRecipe() {
  const recipeId = $('#recipe-id').val();

  const formInputs = {};

  $.post(`/recipes/favorite/${recipeId}`, formInputs, (response) => {
    alert(response);
    favoriteRecipeButton.hide();
    unfavoriteRecipeButton.show();
  });
}

function unfavoriteRecipe() {
  const recipeId = $('#recipe-id').val();

  const formInputs = {};

  $.post(`/recipes/unfavorite/${recipeId}`, formInputs, (response) => {
    alert(response);
    favoriteRecipeButton.show();
    unfavoriteRecipeButton.hide();
  });
}