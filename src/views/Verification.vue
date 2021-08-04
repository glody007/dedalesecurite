<template>
  <div>
    <NavBar />
    <b-row>
      <b-col class="mt-5" md="6" offset-md="3" sm="6" offset-sm="3" cols="10" offset="1">
        <div class="text-center mt-4" v-if="loading">
          <b-spinner variant="primary"></b-spinner>
        </div>
        <b-card v-else bg-variant="warning" title="Information de verification" class="py-3 px-3 card">
          <b-row v-for="key in keys" :key="key">
              <span v-if="canViewInfo(key)" class="key mt-2">{{ key }} :</span>
              <span v-if="canViewInfo(key)" class="mt-1" :class="datas_model[key]">{{ values[key] }}</span>
          </b-row>
          <div v-if="!canView && templateProtected">
            <b-row align-h="center">
              <b-col cols="10">
                <p class="mt-5">*** Vous devez vous connecter pour avoir acces aux informations protégés</p>
              </b-col>
            </b-row>
            <b-row align-h="center">
              <b-col offset="2" offset-md="4">
                <router-link :to="{ name: 'login' }">
                  <b-button pill size="lg" type="button" variant="primary">Connexion</b-button>
                </router-link>
              </b-col>
            </b-row>
          </div>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import $backend from '../backend'

export default {
  name: 'verification',
  components: {
    NavBar
  },
  created () {
    this.fetchVerification()
  },
  watch: {
    '$route': 'fetchVerification'
  },
  data () {
    return {
      values: {},
      keys: [],
      verification: {},
      datas_model: {},
      canView: false,
      templateProtected: true,
      loading: false,
      erro: false
    }
  },
  methods: {
    fetchVerification () {
      this.loading = true
      this.error = false
      $backend.fetchVerification(this.$route.params.id)
        .then(response => {
          this.loading = false
          this.parse(response.data)
        })
        .catch(error => {
          console.log(error)
          this.error = true
          this.loading = false
        })
    },
    parse (data) {
      this.templateProtected = data.template.protected
      this.datas_model = JSON.parse(data.template.datas_model)
      for (const key in this.datas_model) {
        this.keys.push(key)
      }
      this.values = JSON.parse(data.datas.values)
      this.canView = data.can_view
    },
    canViewInfo (key) {
      if (this.datas_model[key] === 'string' || !this.templateProtected) return true
      return this.canView
    }
  }
}
</script>

<style>
.key {
  font-size: 20px;
}
.string {
  color: white;
  background-color: blue;
  padding: 4px;
  border-radius: 2px;
}
.securised {
  color: white;
  background-color: red;
  padding: 4px;
  border-radius: 2px;
}
</style>
