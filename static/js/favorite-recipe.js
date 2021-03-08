"use strict";

// Button to favorite a recipe
const favoriteRecipeButton = $('#favorite-recipe');
favoriteRecipeButton.on('click', favoriteRecipe);

const unfavoriteRecipeButton = $('#unfavorite-recipe');


function favoriteRecipe() {
  console.log('STARTING favoriteRecipe')
  const recipeId = $('#recipe-id').val();

  const formInputs = {};

  $.post(`/recipes/favorite/${recipeId}`, formInputs, (response) => {
    alert(response);
    favoriteRecipeButton.hide();
    unfavoriteRecipeButton.show();
  });

  console.log('ENDING favoriteRecipe')
}