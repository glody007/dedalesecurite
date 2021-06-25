import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('token') || '',
  },
  mutations: {
    loginSuccess (state, data) {
      localStorage.setItem('token', data.auth_token)
      state.token = data.auth_token
    },
    logout (state) {
      localStorage.removeItem('token')
      state.token = ''
    }
  },
  actions: {

  }
})
