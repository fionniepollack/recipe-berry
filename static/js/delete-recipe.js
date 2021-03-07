"use strict";

const recipeId = parseInt($('#recipe-id').val());

// Button to delete a recipe
const deleteRecipeButton = $('#delete-recipe');
deleteRecipeButton.on('click', deleteRecipe);

function deleteRecipe() {
  $.ajax({
    url: `/recipes/${recipeId}`,
    type: 'DELETE',
    success: function(response) {
        window.location.href = response.data;
    }
  });
}

// check if user in session and author match
// if they click delete
// delete recipe from database