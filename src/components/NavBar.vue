<template>
  <div class="container">
    <nav class="navbar navbar-expand-sm navbar-light">
      <div class="container-fluid">
        <router-link to="/">
          <a class="navbar-brand" href="#" style="display: inline-block;text-decoration:none; color:black;">DEDALE SECURITE</a>
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggler" aria-controls="navbarToggler" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarToggler">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">

          </ul>
          <router-link v-if="!loggedin" to="login">
            <button class="btn btn-lg" type="button">Login</button>
          </router-link>

          <router-link v-if="!loggedin" to="registration">
            <b-button pill size="lg" variant="primary" type="button">Sign Up</b-button>
          </router-link>

          <router-link v-if="loggedin" to="dashboard">
            <b-button pill size="lg" variant="primary" type="button">Dashboard</b-button>
          </router-link>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  computed: {
    loggedin () {
      if (this.$store.state.token) return true
      return false
    }
  }
}
</script>
