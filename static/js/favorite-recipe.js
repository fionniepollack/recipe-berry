"use strict";

// const recipeId = parseInt($('#recipe-id').val());

// Button to favorite a recipe
const favoriteRecipeButton = $('#favorite-recipe');
favoriteRecipeButton.on('click', favoriteRecipe);

function favoriteRecipe() {
  $.post('/new-order',
  {'user': $(user-id), 'recipe': $(recipe-id)},
  function(response) {
    alert(response);
  });
}