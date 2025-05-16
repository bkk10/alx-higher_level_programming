$(document).ready(function () {
    $('#load_posts').click(function () {
        const userId = $('#user_id').val();

        // Clear previous list
        $('#post_list').empty();

        // Fetch posts for the user
        $.get(`https://jsonplaceholder.typicode.com/posts?userId=${userId}`, function (data) {
            for (let i = 0; i < data.length; i++) {
                const postTitle = data[i].title;
                $('#post_list').append('<li>' + postTitle + '</li>');
            }
        });
    });
});
