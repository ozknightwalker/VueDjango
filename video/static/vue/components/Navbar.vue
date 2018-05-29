<template>
  <nav class="navbar sticky-top navbar-dark bg-dark mb-2">
    <Brand-Item />
  </nav>
</template>

<script>
import BrandItem from './navbar/BrandItem.vue';

export default {
  components: {
    BrandItem
  }
};
</script>
