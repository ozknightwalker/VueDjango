<template>
  <div class="container">
      <div class="row">
        <div class="col-sm-6 offset-sm-3">
          <div id="publisher">

          </div>
        </div>
        <div class="col-sm-3">
          <div id="subscribers"></div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  mounted: function() {

    let session = OT.initSession(apiKey, sessionId);
    // Initialize a Publisher, and place it into the element with id="publisher"
    let publisher = OT.initPublisher('publisher', null, e => {
      if (e) {
        console.log('error init!');
      }
    });
    publisher.on({
      streamCreated: e => {
        console.log('started streaming', e);
        session.subscribe(e.stream, 'subscriber', null, e => {
          if (e) {
            console.log(e);
          }
        })
      },
      streamDestroyed: e => {
        console.log('stop streaming', e);
      }
    });

    session.connect(token, error => {
      if (session.capabilities.publish == 1) {
        session.publish(publisher);
      } else {
        console.log(error);
      }
    });
  }
};
</script>
