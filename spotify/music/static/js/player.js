
songUrl = await window.songUrl
artist = await window.artist
songName = await window.track


document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.play-button').forEach(button => {
          button.addEventListener('click', function () {
            console.log('Hello World')

          console.log(songUrl, songName, artist)


          })
  })
})