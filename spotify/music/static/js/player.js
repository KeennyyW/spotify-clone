
songUrl = window.songUrl
artist = window.artist
songName = window.track


document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.play-button').forEach(button => {
          button.addEventListener('click', function () {
            console.log('Hello World')

          console.log(songUrl, songName, artist)


          })
  })
})