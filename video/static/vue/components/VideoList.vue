<template>
  <div id="videolist">
    <ul>
      <li v-for="video in videos">
        <video-item v-bind:video="video" v-bind:id="video.id">
        </video-item>
      </li>
    </ul>
  </div>
</template>

<script>
import VideoItem from './VideoItem.vue'

export default {
  components: {
    VideoItem
  },
  data: function () {
    return {
      videos: [
        { text: 'Learn Vue' },
        { text: 'Do hard things' }
      ]
    }
  }
}
</script>
