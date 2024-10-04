document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.play-button').forEach(button => {
    button.addEventListener('click', function () {
      console.log(window.songUrl, window.artist, window.track);
      let songName = window.track;
      let artistName = window.artist;
      let songUrl = window.songUrl;

      let playBtn = document.querySelector('.play-button');
      let seekSlider = document.querySelector('.seek_slider');
      let currentTimeDisplay = document.querySelector('.current-time');
      let totalTimeDisplay = document.querySelector('.total-duration');

      let isPlaying = false;
      let updateTimer;
      let curr_track = document.createElement('audio');

      let displayArtistName = document.querySelector('.track-artist');
      let displaySongName = document.querySelector('.track-title');


      loadTrack(songUrl);

      function loadTrack(songUrl) {
        clearInterval(updateTimer);


        curr_track.src = songUrl;
        curr_track.load();

        displayArtistName.textContent = artistName;
        displaySongName.textContent = songName;


        curr_track.addEventListener('loadedmetadata', () => {
          totalTimeDisplay.textContent = formatTime(curr_track.duration);
        });


        updateTimer = setInterval(setUpdate, 1000);

      }


      function playPauseTrack() {
        if (!isPlaying) {
          playTrack();
        } else {
          pauseTrack();
        }
      }

      function playTrack() {
        curr_track.play();
        isPlaying = true;
        playBtn.textContent = 'Pause';
      }

      function pauseTrack() {
        curr_track.pause();
        isPlaying = false;
        playBtn.textContent = 'Play';
      }


      function setUpdate() {
        if (!isNaN(curr_track.duration)) {
          let seekPosition = curr_track.currentTime * (100 / curr_track.duration);
          seekSlider.value = seekPosition;
          currentTimeDisplay.textContent = formatTime(curr_track.currentTime);
        }
      }


      function formatTime(seconds) {
        let minutes = Math.floor(seconds / 60);
        let secs = Math.floor(seconds % 60);
        if (secs < 10) secs = "0" + secs;
        return minutes + ":" + secs;
      }


      seekSlider.addEventListener('input', function () {
        let seekTo = curr_track.duration * (seekSlider.value / 100);
        curr_track.currentTime = seekTo;
      });



      playBtn.addEventListener('click', playPauseTrack);
    });
  });
});
