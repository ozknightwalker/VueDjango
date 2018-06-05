<template>
  <div class="row">
    <div class="col" v-for="room in rooms">
        <room-item v-bind:room="room" v-bind:id="room.id" />
    </div>
  </div>
</template>

<script>
import RoomItem from './RoomItem.vue';

export default {
  components: {
    RoomItem
  },
  data: function() {
    return {
      rooms: []
    };
  },
  methods: {
    fetchRooms: function() {
      let _this = this;
      this.$http.get('/api/rooms/', {})
        .then(response => {
          _this.rooms = response.data;
        }).catch(e => {
          console.error(e);
        });
    },
  },
  mounted: function() {
    this.fetchRooms();
  },
};
</script>
