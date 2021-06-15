import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ImageKit from 'imagekitio-vue'

import './filters'

Vue.config.productionTip = false

Vue.use(ImageKit, {
  urlEndpoint: 'https://ik.imagekit.io/tlr7lkiwqbj',
  publicKey: 'public_7BOsJo+gJzQeU+O7WgThIpcpIc4=',
  authenticationEndpoint: 'api/auth/uploadendpoint'
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
