<template>
  <div>
    <NavBar />

    <div class="main">
      <b-container>
        <b-row align-h="center" class="first-section">
          <img src="@/assets/img/fond.svg" class="background" alt="background">
          <b-col col cols="12" md="10" class="text-center">
            <h2>Securisez vos documents et rendez la vérification instantanée avec un QR Code</h2>
          </b-col>
          <b-col col cols="12" class="text-center">
            <router-link to="registration">
              <b-button class="register" variant="primary" type="button">Enregistrement</b-button>
            </router-link>
          </b-col>
        </b-row>

        <b-row align-h="center" class="mb-5">
          <b-col col cols="12" class="text-center">
            <h2>Comment ça marche</h2>
          </b-col>
        </b-row>

        <b-row class="justify-content-md-center">
          <b-col col cols="12" sm="2" class="mb-1">
            <b-row align-v="center" align-h="center" class="justify-content-xs-center">
              <img src="@/assets/img/1.png" class="number" alt="2">
            </b-row>
          </b-col>
          <b-col col cols="12" sm="10" class="text-center mb-2">
            <h3 class="step">Créer simplement un document modèle avec des placeholders</h3>
          </b-col>
          <b-col col  cols="12">
            <img src="@/assets/img/new-template.png" alt="Creation template">
          </b-col>
        </b-row>

        <b-row align-h="center">
          <b-col col cols="4" class="text-center">
            <img src="@/assets/img/connexion-3.png" class="connexion" alt="connexion">
          </b-col>
        </b-row>

        <b-row class="justify-content-md-center">
          <b-col col cols="12" sm="2" class="mb-1">
            <b-row align-v="center" align-h="center" class="justify-content-xs-center">
              <img src="@/assets/img/2.png" class="number" alt="2">
            </b-row>
          </b-col>
          <b-col col cols="12" sm="10" class="text-center mb-2">
            <h3 class="step">Un formulaire est générer automatiquement à partir des placeholders</h3>
          </b-col>
          <b-col col cols="12">
            <img src="@/assets/img/form.png" alt="Formulaire generer automatiquement">
          </b-col>
        </b-row>

        <b-row align-h="center">
          <b-col col cols="12" md="8" class="text-center">
            <img src="@/assets/img/connexion-1.png" class="connexion" alt="connexion">
          </b-col>
        </b-row>

        <b-row class="justify-content-md-center">
          <b-col col cols="12" sm="2" class="mb-1">
            <b-row align-v="center" align-h="center" class="justify-content-xs-center">
              <img src="@/assets/img/3.png" class="number" alt="3">
            </b-row>
          </b-col>
          <b-col col cols="12" sm="10" class="text-center mb-2">
            <h3 class="step">Générer seulement les Qr codes de verification ou le document complet</h3>
          </b-col>
          <b-col col cols="12">
            <img src="@/assets/img/generate-pdf.png" alt="Boutons de generation de pdf avec qr codes">
          </b-col>
        </b-row>

        <b-row align-h="center">
          <b-col col cols="12" md="8" class="text-center">
            <img src="@/assets/img/connexion-2.png" class="connexion" alt="connexion">
          </b-col>
        </b-row>

        <b-row class="justify-content-md-center">
          <b-col col cols="12" sm="2" class="mb-1">
            <b-row align-v="center" align-h="center" class="justify-content-xs-center">
              <img src="@/assets/img/4.png" class="number" alt="4">
            </b-row>
          </b-col>
          <b-col col cols="12" sm="10" class="text-center mb-2">
            <h3 class="step">Générer un document avec Qr code de verification et tout les placeholders remplacer par les données</h3>
          </b-col>
          <b-col col cols="12">
            <img src="@/assets/img/document-with-qr.png" alt="Document contenant les qr codes de verification">
          </b-col>
        </b-row>

        <b-row align-h="center">
          <b-col col cols="4" class="text-center">
            <img src="@/assets/img/triple-arrow.png" class="connexion" alt="connexion">
          </b-col>
        </b-row>

        <b-row align-h="center" class="my-5">
          <b-col col cols="12" class="text-center">
            <router-link to="registration">
              <b-button class="register" variant="primary" type="button">Enregistrement</b-button>
            </router-link>
          </b-col>
        </b-row>
      </b-container>
    </div>

    <div class="footer">
      <b-container>
        <b-row align-h="between">
          <b-col col cols="4" class="text-center">
            <b-row align-h="center">
              <h3 class="footer-title">Made by</h3>
            </b-row>
            <p class="footer-body">Tech-alchemist</p>
          </b-col>
          <b-col col cols="4" class="text-center">
            <b-row align-h="center">
              <h3 class="footer-title">Company</h3>
            </b-row>
            <p class="footer-body">Dedale</p>
          </b-col>
          <b-col col cols="4" class="text-center">
            <b-row align-h="center">
              <h3 class="footer-title">Contacts</h3>
            </b-row>
            <p class="footer-body">
              dedalesecurite@gmail.com <br>
              +243 9970 28 901
            </p>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'home',
  components: {
    NavBar
  }
}
</script>

<style lang="scss" scoped>
  @import url('https://fonts.googleapis.com/css2?family=Open+Sans&family=Roboto:ital,wght@0,100;1,100&display=swap');
  .first-section {
    min-height: 70vh;
    margin-bottom: 10vh;
    overflow: hidden;
    position: relative;
  }
  .background {
    position: absolute;
    opacity: 0.3;
  }
  .register {
    width: 300px;
    height: 100px;
    font-size: 30px;
    position: relative;
  }
  h2 {
    font-size: 50px;
    font-family: 'Roboto', sans-serif;
  }
  .main {
    min-height: 100vh;
    margin-top: 10vh;
  }
  .number {
    width: 100px;
  }
  .step {
    font-size: 35px;
    font-family: 'Open Sans', sans-serif;
  }
  .footer {
    min-height: 30vh;
    padding-top: 5vh;
    background-color: #007bff;
  }
  .footer-title {
    font-family: 'Open Sans', sans-serif;
    color: #000066;
  }
  .footer-body {
    font-family: 'Open Sans', sans-serif;
    color: white;
  }
</style>
