<template>
  <div class="container">
    <nav class="navbar navbar-expand-sm navbar-light">
      <div class="container-fluid">
        <router-link to="/" style="display: inline-block;text-decoration:none;">
          <a class="navbar-brand" href="#">DEDALE SECURITE</a>
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggler" aria-controls="navbarToggler" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarToggler">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">

          </ul>
          <router-link to="login">
            <button class="btn btn-lg" type="button">Login</button>
          </router-link>

          <router-link to="registration">
            <b-button pill size="lg" variant="primary" type="button">Sign Up</b-button>
          </router-link>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style>
navbar-brand {
    color: blue;
}
</style>
