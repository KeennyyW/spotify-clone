// static/your_app/js/songs.js

$(document).ready(function() {
    $('.song-item').on('click', function() {
        var trackName = $(this).data('track-name');
        var artistName = $(this).data('artist-name');

        $.ajax({
            url: '/your-backend-url/',  // URL for your backend endpoint
            type: 'POST',
            data: {
                'track_name': trackName,
                'artist_name': artistName,
                'csrfmiddlewaretoken': '{{ csrf_token }}'  // You will need to manage CSRF token here
            },
            success: function(response) {
                console.log('Data sent successfully:', response);
                // Update the UI based on the response
            },
            error: function(xhr, status, error) {
                console.error('Error sending data:', error);
            }
        });
    });
});
