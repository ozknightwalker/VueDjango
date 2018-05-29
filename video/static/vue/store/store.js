import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    brand: {
      title: "Testing",
      image: "/static/img/navbar/bootstrap-solid.svg"
    },
    auth: {
      id: null
    },
  },
  getters: {
    is_authenticated: state => {
      return state.auth.id !== null;
    }
  }
});
