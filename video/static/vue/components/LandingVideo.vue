<template>
  <div class="container">
      <div class="row">
        <div class="col-sm-6 offset-sm-3">
          <div id="publisher">

          </div>
          <button class="btn btn-success" type="button" name="button" v-on:click.prevent="startStream" v-bind:disabled="!is_connected">Start</button>
          <button class="btn btn-warning" type="button" name="button" v-on:click.prevent="endStream" v-bind:disabled="enableEnd">End</button>

          <button class="btn" type="button" name="button" v-on:click="toggleMute">Mute</button>
          <button class="btn" type="button" name="button" v-on:click="toggleVideo">Video</button>
        </div>
      </div>
      <div class="row">
          <div class="col-sm-12" id="subscribers"></div>
      </div>
  </div>
</template>

<script>
export default {
  computed: {
    enableEnd: function() {
      return !this.is_started;
    },
  },
  data: function() {
    return {
      is_connected: false,
      is_started: false,
      mute: false,
      video: false,
      session: OT.initSession(apiKey, sessionId),
      publisher: OT.initPublisher('publisher', {mirror: false}),
    };
  },
  methods: {
    toggleMute: function() {
      this.mute = !this.mute;
      this.publisher.publishAudio(this.mute);
    },
    toggleVideo: function() {
      this.video = !this.video;
      this.publisher.publishVideo(this.video);
    },
    connect: function() {
      this.session.connect(token, function(error) {
        if (error) {
          console.error('Failed to connect', error);
        }
      });
    },
    startStream: function() {
      let _this = this;
      if (!_this.is_connected || _this.is_started || _this.session.capabilities.publish != 1) {
        return;
      }
      _this.session.publish(_this.publisher, function(error) {
        if (error) {
          console.error('Failed to publish', error);
        }
      });
    },
    endStream: function() {
      let _this = this;
      if (!_this.is_connected || !_this.is_started) {
        return;
      }
      _this.session.unpublish(_this.publisher);
    },
    sessionConnected: function(event) {
      // Initialize a Publisher, and place it into the element with id="publisher"
      this.is_connected = true;
    },
    streamCreated: function(event) {
      // Create a container for a new Subscriber, assign it an id using the streamId, put it inside
      // the element with id="subscribers"
      // let _this = this;
      // let subContainer = document.createElement('div');
      // _this.is_started = true;
      // subContainer.id = 'stream-' + event.stream.streamId;
      // document.getElementById('subscribers').appendChild(subContainer);
      //
      // // Subscribe to the stream that caused this event, put it inside the container we just made
      // this.session.subscribe(event.stream, subContainer, function(error) {
      //   if (error) {
      //     console.error('Failed to subscribe', error);
      //   }
      // });
    },
    streamDestroyed: function() {
      let _this = this;
      _this.is_started = false;
    },
    accessAllowed: function() {
      this.connect();
    },
    accessDenied: function() {
      console.warn('Please allow Media Input!');
    },
  },
  mounted: function() {
    let _this = this;
    // if there is a media input device
    if (OT.checkSystemRequirements() != 1) {
      console.log('No Media Input Available');
    } else {
      _this.session.on({
        // This function runs when session.connect() asynchronously completes
        sessionConnected: _this.sessionConnected,

        // This function runs when another client publishes a stream (eg. session.publish())
        // streamCreated: _this.streamCreated,
        // connectionCreated: e => {},
        // This function runs when a user connects to the session
      });
      _this.publisher.on({
        accessAllowed: _this.accessAllowed,
        accessDenied: _this.accessDenied,
        // This function runs when a publisher starts streaming
        streamCreated: _this.streamCreated,
        // This function runs when publisher ends the stream
        streamDestroyed: _this.streamDestroyed,
      });
    }
  }
};
</script>
