"use strict";

// Button to delete a recipe
const deleteRecipeButton = $('#delete-recipe');
deleteRecipeButton.on('click', deleteRecipe);

function deleteRecipe() {
  $.get('/status', { order: 123 }, (res) => {
    $('#order-status').html(res);
  });
}

// check if user in session and author match
// if they click delete
// delete recipe from database