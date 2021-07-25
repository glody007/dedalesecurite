<template>
  <div>
    <NavBar/>
    <b-row class="background">
      <b-col md="4" offset-md="4" sm="6" offset-sm="3" cols="10" offset="1">
        <b-card title="Registration" class="px-3">
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
              id="input-group-name"
              label="Your Name:"
              label-for="name"
              class="mt-4"
            >
              <b-form-input
                id="name"
                v-model="form.name"
                placeholder="Enter name"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-invalid-feedback :state="nameValidated">
              Le nom est obligatoire.
            </b-form-invalid-feedback>

            <b-form-group
              id="input-group-name"
              label="Your phone number:"
              label-for="number"
              class="mt-4"
            >
              <b-form-input
                id="number"
                v-model="form.phone_number"
                type="number"
                placeholder="Enter number"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-invalid-feedback :state="phoneNumberValidated">
              Le numero de telephone est obligatoire.
            </b-form-invalid-feedback>

            <b-form-group
              id="input-group-organisation"
              label="Your Organisation:"
              label-for="organisation"
              class="mt-4"
            >
              <b-form-input
                id="organisation"
                v-model="form.organisation"
                placeholder="Enter your organisation"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-invalid-feedback :state="organisationValidated">
              Le nom de l'organisation est obligatoire.
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
                placeholder="Enter your password"
              ></b-form-input>
            </b-form-group>
            <b-form-invalid-feedback :state="passwordValidated">
              Le mot de passe doit avoir au moins 6 characteres.
            </b-form-invalid-feedback>

            <b-form-group
              id="input-group-password-confirm"
              label="Confirm your Password:"
              label-for="password-confirm"
              class="mt-4"
            >
              <b-form-input
                id="password-confirm"
                v-model="form.passwordConfirm"
                type="password"
                placeholder="Confirm your password"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-invalid-feedback :state="confirmationPasswordValidated">
              Le mot de passe doit etre identique
            </b-form-invalid-feedback>
            <b-form-invalid-feedback :state="noRegistrationError" class="text-center">
              Email ou numero de telephone déjà utilisé.
            </b-form-invalid-feedback>

            <div class="text-center mt-4" v-if="loading">
              <b-spinner variant="primary"></b-spinner>
            </div>
            <div class="d-grid gap-2 mt-4" v-else>
              <b-button pill type="submit" variant="primary">Submit</b-button>
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
  name: 'registration',
  components: {
    NavBar
  },
  data () {
    return {
      form: {
        email: '',
        name: '',
        phone_number: '',
        organisation: '',
        password: '',
        passwordConfirm: ''
      },
      noRegistrationError: true,
      noSubmitted: true,
      loading: false
    }
  },
  computed: {
    validated () {
      return this.emailValidated &&
             this.nameValidated &&
             this.phoneNumberValidated &&
             this.organisationValidated &&
             this.passwordValidated &&
             this.confirmationPasswordValidated
    },
    emailValidated () {
      return this.form.email.match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/) ||
            this.noSubmitted
    },
    passwordValidated () {
      return this.form.password.length >= 6 || this.noSubmitted
    },
    phoneNumberValidated () {
      return this.form.phone_number.match(/^!*([0-9]!*){10,}/) ||
             this.noSubmitted
    },
    confirmationPasswordValidated () {
      return this.form.passwordConfirm === this.form.password || this.noSubmitted
    },
    nameValidated () {
      return this.form.name.length >= 1 || this.noSubmitted
    },
    organisationValidated () {
      return this.form.organisation.length >= 1 || this.noSubmitted
    }
  },
  methods: {
    onSubmit (event) {
      event.preventDefault()
      this.noSubmitted = false
      if (this.validated) {
        this.loading = true
        this.form.nom = this.form.name
        $backend.register(this.form)
          .then(response => {
            if (response.status === 202) this.noRegistrationError = false
            else {
              this.$store.commit('loginSuccess', response.data)
              this.$router.push('dashboard')
            }
            this.loading = false
          })
          .catch(error => {
            console.log(error)
            this.loading = false
          })
      }
    },
    onReset (event) {
      event.preventDefault()
      // Reset our form values
      this.form.email = ''
      this.form.name = ''
      this.form.organisation = ''
      this.form.password = ''
      this.form.passwordConfirm = ''
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>

<style lang="scss">
.background {
  min-height: 100vh;
  background-image: url('~@/assets/img/fond.svg');
}
</style>
