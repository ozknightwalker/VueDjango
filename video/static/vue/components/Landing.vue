<template>
  <div class="container">
      <div class="row">
        <div class="col-sm-6 offset-sm-3">
          <div id="publisher">

          </div>
        </div>
      </div>
      <div class="row">
          <div class="col-sm-12" id="subscribers"></div>
      </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      session: OT.initSession(apiKey, sessionId),
      publisher: OT.initPublisher('publisher', {mirror: false, facingMode: 'user'})
    };
  },
  methods: {
    connect: function() {
      this.session.connect(token, function(error) {
        if (error) {
          console.error('Failed to connect', error);
        }
      });
    },
    sessionConnected: function(event) {
      // Initialize a Publisher, and place it into the element with id="publisher"
      this.session.publish(this.publisher, function(error) {
        if (error) {
          console.error('Failed to publish', error);
        }
      });
    },
    streamCreated: function(event) {
      // Create a container for a new Subscriber, assign it an id using the streamId, put it inside
      // the element with id="subscribers"
      debugger;
      let subContainer = document.createElement('div');
      subContainer.id = 'stream-' + event.stream.streamId;
      document.getElementById('subscribers').appendChild(subContainer);

      // Subscribe to the stream that caused this event, put it inside the container we just made
      this.session.subscribe(event.stream, subContainer, function(error) {
        if (error) {
          console.error('Failed to subscribe', error);
        }
      });
    },
  },
  mounted: function() {
    let _this = this;
    _this.session.on({
      // This function runs when session.connect() asynchronously completes
      sessionConnected: _this.sessionConnected,

      // This function runs when another client publishes a stream (eg. session.publish())
      streamCreated: _this.streamCreated
    });
    _this.connect();
  }
};
</script>
