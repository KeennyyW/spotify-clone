
songUrl = window.songUrl
artist = window.artist
songName = window.track


document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.play-button').forEach(button => {
          button.addEventListener('click', function () {
              console.log('Hello World')
              song_prefix = songUrl.replace(" C:\\VsCode\\spotify\\spotify-clone\\spotify", "");

          console.log(song_prefix, songName, artist)
              console.log('hello sdsds')

          })
  })
})