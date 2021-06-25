<template>
  <router-link :to="{ name: 'template', params: { id: id }}" style="display: inline-block;text-decoration:none;">
    <md-card md-with-hover>
      <md-ripple>
        <md-card-header>
          <div class="md-title">{{ name }}</div>
          <div class="md-subhead">Template existant</div>
        </md-card-header>

        <md-card-content>
          Cliquer pour modifier le template, creer des nouveaux documents a partir du template et generer des nouveaux Qr code de verification.
        </md-card-content>
      </md-ripple>
    </md-card>
  </router-link>
</template>

<script>
export default {
  name: 'TemplateCard',
  props: ['name', 'id']
}
</script>
