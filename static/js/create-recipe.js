"use strict";

//----------------------------------------------------------------------------//
//- INGREDIENT BUTTONS -------------------------------------------------------//
//----------------------------------------------------------------------------//

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


//----------------------------------------------------------------------------//
//- INSTRUCTION BUTTONS ------------------------------------------------------//
//----------------------------------------------------------------------------//

// Button to add an instruction
const addInstructionButton = $('#add-instruction');
addInstructionButton.on('click', addInstruction);

function addInstruction() {
  console.log("Running addInstruction..."); 
  const newInstructionNum = parseInt($('#num-instruction').val()) + 1;

  console.log("newInstructionNum = " + newInstructionNum)

  const newInstructionInput = "<input type='text' id='instruction-item-" + newInstructionNum + "'><br>";

  console.log("Appending newInstructionInput: " + newInstructionInput)
  $('#instruction-input-list').append(newInstructionInput);

  $('#num-instruction').val(newInstructionNum);
}


// Button to remove an instruction
const removeInstructionButton = $('#remove-instruction');
removeInstructionButton.on('click', removeInstruction);

function removeInstruction() {
    const instructionInputListLength = $('#num-instruction').val();

    if (instructionInputListLength > 1) {
    $('#instruction-item-' + instructionInputListLength).remove();
    $('#num-instruction').val(instructionInputListLength - 1);
    }
}