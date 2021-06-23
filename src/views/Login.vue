<template>
  <div>
    <NavBar class="mb-5"/>
    <b-row>
      <b-col md="4" offset-md="4" sm="6" offset-sm="3" cols="10" offset="1">
        <b-card title="Login" class="py-3 px-3">
          <b-form novalidate @submit="onSubmit" @reset="onReset">
            <b-form-group
              id="input-group-email"
              label="Email address:"
              label-for="email"
              class="mt-4"
            >
              <b-form-input
                id="email"
                v-model="form.email"
                type="email"
                placeholder="Enter email"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-invalid-feedback :state="emailValidated">
              Addresse email invalide.
            </b-form-invalid-feedback>

            <b-form-group
              id="input-group-password"
              label="Your Password:"
              label-for="password"
              class="mt-4"
            >
              <b-form-input
                id="password"
                v-model="form.password"
                type="password"
                placeholder="Enter password"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-invalid-feedback :state="passwordValidated">
              Le mot de passe doit avoir au moins 6 characteres.
            </b-form-invalid-feedback>
            <b-form-invalid-feedback :state="noAuthError" class="text-center">
              Email ou mot de passe incorrect.
            </b-form-invalid-feedback>

            <div class="text-center mt-4" v-if="loading">
              <b-spinner variant="primary"></b-spinner>
            </div>
            <div class="d-grid gap-2 mt-4" v-else>
              <b-button pill type="submit" variant="primary">Login</b-button>
            </div>
          </b-form>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import $backend from '../backend'

export default {
  name: 'login',
  components: {
    NavBar
  },
  data () {
    return {
      form: {
        email: '',
        password: ''
      },
      noAuthError: true,
      noSubmitted: true,
      loading: false
    }
  },
  computed: {
    validated () {
      return this.emailValidated && this.passwordValidated
    },
    emailValidated () {
      return this.form.email.match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/) ||
             this.noSubmitted
    },
    passwordValidated () {
      return this.form.password.length >= 6 || this.noSubmitted
    }
  },
  methods: {
    onSubmit (event) {
      event.preventDefault()
      this.noSubmitted = false
      if (this.validated) {
        this.loading = true
        $backend.login(this.form)
          .then(response => {
            this.$store.commit('loginSuccess', response.data)
            this.loading = false
            this.$router.push('dashboard')
          })
          .catch(error => {
            if (error.response.status === 401) this.noAuthError = false
            this.loading = false
          })
      }
    },
    onReset (event) {
      event.preventDefault()
      // Reset our form values
      this.form.email = ''
      this.form.password = ''
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>

<style lang="scss">

</style>
