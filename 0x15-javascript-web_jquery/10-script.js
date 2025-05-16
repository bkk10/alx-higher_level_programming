$(document).ready(function(){
    $.get('https://jsonplaceholder.typicode.com/users/1', function(data){
        const userName = data.name;
        $('#user_name').text(userName);
    })
})