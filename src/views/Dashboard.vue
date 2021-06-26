<template>
  <div class="page-container">
    <md-app md-mode="reveal">
     <md-app-toolbar class="md-primary">
       <md-button class="md-icon-button" @click="menuVisible = !menuVisible">
         <md-icon>menu</md-icon>
       </md-button>
       <span class="md-title">Tableau de bord</span>
     </md-app-toolbar>

     <md-app-drawer :md-active.sync="menuVisible" md-persistent="mini">
       <md-toolbar class="md-transparent" md-elevation="0">DEDALE SECURITE</md-toolbar>

       <md-list>
         <router-link :to="{ name: 'home' }">
           <md-list-item>
             <md-icon>home</md-icon>
             <span class="md-list-item-text">Acceuil</span>
           </md-list-item>
         </router-link>

         <router-link :to="{ name: 'list-templates' }">
           <md-list-item>
             <md-icon>view_list</md-icon>
             <span class="md-list-item-text">Mes templates</span>
           </md-list-item>
         </router-link>

         <router-link :to="{ name: 'new-template' }">
           <md-list-item>
             <md-icon>add</md-icon>
             <span class="md-list-item-text">Creer un template</span>
           </md-list-item>
         </router-link>

         <md-list-item @click="logoutClicked = true">
           <md-icon>logout</md-icon>
           <span class="md-list-item-text">Déconnexion</span>
         </md-list-item>
       </md-list>
     </md-app-drawer>

      <md-app-content>
        <DialogDeconnexion
          :active="logoutClicked"
          @cancel="logoutClicked = false"
          @agreed="logoutClicked = false"/>
        <router-view/>
      </md-app-content>
    </md-app>
  </div>
</template>

<script>
import DialogDeconnexion from '@/components/DialogDeconnexion.vue'

export default {
  name: 'dashboard',
  data: () => ({
    menuVisible: false,
    logoutClicked: false
  }),
  components: {
    DialogDeconnexion
  },
  methods: {

  }
}
</script>

<style lang="scss" scoped>
  .md-app {
    min-height: 100vh;
  }
  .md-drawer {
    width: 230px;
  }
  .md-list-item-text {
    color: black;
  }
</style>
