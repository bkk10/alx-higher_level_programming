$(document).ready(function(){
    $('#add_item').click(function(){
        const new_item = $('<li>Item</li>');
        $('ul.my_list').append(new_item);
    })
});