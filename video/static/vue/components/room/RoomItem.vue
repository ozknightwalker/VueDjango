<template>
  <div class="card">
    <div class="card-body">
      <h4 class="card-title">{{ room.name }}</h4>
      <router-link :to="{ name: '/room', params: {id: room.id} }" class="btn btn-primary">Join</router-link>
    </div>
  </div>
</template>

<script>
export default {
  props: ['room']
}
</script>
