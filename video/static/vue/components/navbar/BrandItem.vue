<template>
  <div>
    <router-link to="/" class="navbar-brand">
      <img v-bind:src="getBrandImage" width="30" height="30" class="d-inline-block align-top" alt="">
      {{ getTitle }}
    </router-link>
    <router-link to="/login">Login</router-link>

  </div>
</template>

<script>
export default {
  computed: {
    getTitle() {
      return this.$store.state.brand.title;
    },
    getBrandImage() {
      return this.$store.state.brand.image;
    }
  }
}
</script>
