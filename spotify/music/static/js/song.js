
document.addEventListener('DOMContentLoaded', function () {

    window.artist = ""
    window.track = ""
    document.querySelectorAll('.play-button').forEach(button => {
        button.addEventListener('click', function () {
            window.track = this.getAttribute('data-track');
            window.artist = this.getAttribute('data-artist');
            const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
            console.log(track, artist);
            console.log("Hello");

            fetch('ajax', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrf
            },
            body: JSON.stringify({title: track, artist: artist})

        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.songUrl = data.song_url;
                    // const responseMassage = this.parentElement.querySelector('.responseMassage');
                    // responseMassage.textContent = songUrl;
                    console.log('Song Url: ', songUrl)

                }
                else {
                    console.error('Error fetching')
                }
            })
                // .catch(error => console.error('Error:', error));






        });
    });
});

