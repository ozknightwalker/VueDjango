import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import { store } from './store/store';
import VueResource from 'vue-resource';
import VieCookies from 'vue-cookies';

import Login from './components/Login.vue';
import Landing from './components/Landing.vue';
import RoomDetails from './components/room/RoomDetails.vue';

Vue.use(VueRouter);
Vue.use(VueResource);
Vue.use(VieCookies);

var router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Landing
    },
    {
      path: '/login',
      component: Login,
      beforeEnter: (to, from, next) => {
        next(store.getters.is_authenticated);
      }
    },
    {
      path: '/room/:id',
      component: RoomDetails
    },
  ]
});

let app = new Vue({
    router,
    store: store,
    el: '#app',
    render: h => h(App)
});
