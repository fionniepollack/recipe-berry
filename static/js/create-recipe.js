"use strict";

//----------------------------------------------------------------------------//
//- INGREDIENT BUTTONS -------------------------------------------------------//
//----------------------------------------------------------------------------//

// Button to add an ingredient
const addIngredientButton = $('#add-ingredient');
addIngredientButton.on('click', addIngredient);

function addIngredient() {
  const newIngredientNum = parseInt($('#num-ingredient').val()) + 1;
  // const newIngredientInput = "<input type='text' name='ingredients' id='ingredient-item-"
  //                            + newIngredientNum
  //                            + "'><br id='ingredient-br-"
  //                            + newIngredientNum
  //                            + "'>";
  
  const newIngredientInput = `<input type='text' name='ingredients' id='ingredient-item-${newIngredientNum}'>
                              <input type='text' name='measurements' id='measurement-item-${newIngredientNum}'>
                              <br id='ingredient-br-${newIngredientNum}'>`;
  
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
    $('#ingredient-br-' + ingredientInputListLength).remove();
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
  // console.log("Running addInstruction..."); 
  const newInstructionNum = parseInt($('#num-instruction').val()) + 1;

  console.log("newInstructionNum = " + newInstructionNum)

  const newInstructionInput = "<input type='text' name='instruction_items' id='instruction-item-" + newInstructionNum + "'><br id='instruction-br-" + newInstructionNum + "'>";

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
    $('#instruction-br-' + instructionInputListLength).remove();
    $('#num-instruction').val(instructionInputListLength - 1);
    }
}