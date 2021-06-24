<template>
  <div class="page-container">
    <md-app md-mode="reveal">
     <md-app-toolbar class="md-primary">
       <md-button class="md-icon-button" @click="menuVisible = !menuVisible">
         <md-icon>menu</md-icon>
       </md-button>
       <span class="md-title">Tableau de bord</span>

       <div class="md-toolbar-section-end">
         <md-button class="md-icon-button">
           <md-icon>more_vert</md-icon>
         </md-button>
       </div>
     </md-app-toolbar>

     <md-app-drawer :md-active.sync="menuVisible">
       <md-toolbar class="md-transparent" md-elevation="0">Navigation</md-toolbar>

       <md-list>
         <md-list-item>
           <md-icon>home</md-icon>
           <span class="md-list-item-text">Acceuil</span>
         </md-list-item>

         <md-list-item>
           <md-icon>menu</md-icon>
           <span class="md-list-item-text">Mes templates</span>
         </md-list-item>
       </md-list>
     </md-app-drawer>

      <md-app-content>
        <router-view/>
      </md-app-content>
    </md-app>
  </div>
</template>

<script>

export default {
  name: 'dashboard',
  data: () => ({
    menuVisible: false
  }),
  components: {

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
</style>
