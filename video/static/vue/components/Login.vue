<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-4 offset-sm-4">
        <form method="post" v-on:submit.prevent="formSubmit($event)">
          <div class="form-group">
            <label for="usernameField">Username</label>
            <input name="username" type="text" class="form-control" id="usernameField" aria-describedby="usernameHelp" placeholder="Enter username" v-model="login.username">
            <small id="usernameHelp" class="form-text text-muted">We'll never share your username with anyone else.</small>
          </div>
          <div class="form-group">
            <label for="passwordField">Password</label>
            <input name="password" type="password" class="form-control" id="passwordField" placeholder="Password" v-model="login.password">
          </div>
          <button type="submit" class="btn btn-primary">Login</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import BrandItem from './navbar/BrandItem.vue';

export default {
  data: function() {
    return {
      login: {
        username: '',
        password: '',
      }
    };
  },
  components: {
    BrandItem
  },
  methods: {
    formSubmit(e) {
      this.$http.post('/api-auth/login/', new FormData(e.target), {
        headers: {
          'X-CSRFToken': this.$cookies.get('csrftoken')
        }
      }).then(response => {
          // success
        }, response => {
          // error
        })
    },
  }
};
</script>
