$(document).ready(function () {
    $.get('https://jsonplaceholder.typicode.com/users', function (data) {
        for (let i = 0; i < data.length; i++) {
            const userName = data[i].name;
            $('#user_list').append('<li>' + userName + '</li>');
        }
    });
});
