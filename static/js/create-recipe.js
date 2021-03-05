"use strict";


// Button to add an ingredient
const addIngredientButton = $('#add-ingredient');
addIngredientButton.on('click', addIngredient);

function addIngredient() {
  const newIngredientNum = parseInt($('#num-ingredient').val()) + 1;
  const newIngredientInput = "<input type='text' id='ingredient-item-" + newIngredientNum + "'><br>";
  
  $('#ingredient-input-list').append(newIngredientInput);

  $('#num-ingredient').val(newIngredientNum);
}


// Button to remove an ingredient
const removeIngredientButton = $('#remove-ingredient');
removeIngredientButton.on('click', removeIngredient);

function removeIngredient() {
    const ingredientInputListLength = $('#num-ingredient').val();

    if (ingredientInputListLength > 1) {
    $('#ingredient-item-' + ingredientInputListLength).remove();
    $('#num-ingredient').val(ingredientInputListLength - 1);
    }
}