"use strict";

const ingredient_button = $('#ingredient-button');
ingredient_button.on('click', () => {
  alert('Handled with jQuery!');
});


// $('.add').on('click', add);
// $('.remove').on('click', remove);

// function add() {
//     const new_chq_no = parseInt($('#total_chq').val()) + 1;
//     const new_input = "<input type='text' id='new_" + new_chq_no + "'>";
    
//     $('#new_chq').append(new_input);

//     $('#total_chq').val(new_chq_no);
// }

// function remove() {
//     const last_chq_no = $('#total_chq').val();

//     if (last_chq_no > 1) {
//     $('#new_' + last_chq_no).remove();
//     $('#total_chq').val(last_chq_no - 1);
//     }
// }