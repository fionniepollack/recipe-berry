"use strict";

//----------------------------------------------------------------------------//
//- INGREDIENT BUTTONS -------------------------------------------------------//
//----------------------------------------------------------------------------//

// Button to add an ingredient
const addIngredientButton = $('#add-ingredient');
addIngredientButton.on('click', addIngredient);

function addIngredient() {
  const newIngredientNum = parseInt($('#num-ingredient').val()) + 1;

  const newIngredientInput = `<input type='text' size="30" placeholder="Ingredient Name" name='ingredients' list='ingredients' id='ingredient-item-${newIngredientNum}'>
                              <input type='text' size="30" placeholder="Measurement Amount" name='measurements' id='measurement-item-${newIngredientNum}'>
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
    $('#measurement-item-' + ingredientInputListLength).remove();
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
  const newInstructionNum = parseInt($('#num-instruction').val()) + 1;

  const newInstructionInput = `<li id='instruction-item-${newInstructionNum}'>
                               <input type='text' size='120' name='instructions'>
                               <br>
                               </li>`;

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


//----------------------------------------------------------------------------//
//- IMAGE BUTTONS ------------------------------------------------------------//
//----------------------------------------------------------------------------//

// Button to add an image
const addImageButton = $('#add-image');
addImageButton.on('click', addImage);

function addImage() {
  const newImageNum = parseInt($('#num-image').val()) + 1;

  const newImageInput = `<input type='url' size='100' name='images' list='images' id='image-item-${newImageNum}'>
                              <br id='image-br-${newImageNum}'>`;
  
  $('#image-input-list').append(newImageInput);

  $('#num-image').val(newImageNum);
}


// Button to remove an image
const removeImageButton = $('#remove-image');
removeImageButton.on('click', removeImage);

function removeImage() {
    const imageInputListLength = $('#num-image').val();

    if (imageInputListLength > 1) {
    $('#image-item-' + imageInputListLength).remove();
    $('#image-br-' + imageInputListLength).remove();
    $('#num-image').val(imageInputListLength - 1);
    }
}