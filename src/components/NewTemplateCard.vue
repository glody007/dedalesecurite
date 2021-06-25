<template>
  <router-link :to="{ name: 'new-template' }" style="display: inline-block;text-decoration:none;">
    <md-card class="md-primary" md-with-hover>
      <md-ripple>
        <md-card-header>
          <div class="md-title">Nouveau</div>
          <div class="md-subhead">Cliquer pour creer un nouveau template</div>
        </md-card-header>

        <md-card-content class="contenu">
          <md-icon class="md-size-3x">add</md-icon>
        </md-card-content>
      </md-ripple>
    </md-card>
  </router-link>
</template>

<script>
export default {
  name: 'NewTemplateCard'
}
</script>

<style lang="scss" scoped>
  .contenu {
    display: flex;
    justify-content: center;
  }
</style>
