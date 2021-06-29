<template>
  <div class="container">
    <Title text="Mes templates" />
    <div class="md-layout md-gutter md-alignment-center-left">
      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
        <NewTemplateCard />
      </div>
      <div v-for="template in templates" :key="template.id" class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
        <TemplateCard :name="template.nom" :id="template.id"/>
      </div>
      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
        <div class="text-center mt-4" v-if="loading">
          <b-spinner variant="primary"></b-spinner>
        </div>
      </div>
      <md-snackbar md-position="center" :md-duration="Infinity" :md-active.sync="error" md-persistent>
        <span>Une erreur est survenue!</span>
        <md-button class="md-primary" @click="fetchTemplates">réessayez</md-button>
      </md-snackbar>
    </div>
  </div>
</template>

<script>
import Title from '@/components/Title.vue'
import NewTemplateCard from '@/components/NewTemplateCard.vue'
import TemplateCard from '@/components/TemplateCard.vue'
import $backend from '../backend'

export default {
  name: 'ListTemplates',
  data: () => ({
    templates: [],
    loading: false,
    error: false
  }),
  components: {
    Title, NewTemplateCard, TemplateCard
  },
  created () {
    this.fetchTemplates()
  },
  watch: {
    '$route': 'fetchTemplates'
  },
  methods: {
    fetchTemplates () {
      this.loading = true
      this.error = false
      $backend.fetchTemplates()
        .then(response => {
          this.loading = false
          this.templates = response.data.templates
        })
        .catch(error => {
          console.log(error)
          this.error = true
          this.loading = false
        })
    }
  }
}
</script>

<style lang="scss" scoped>
  .md-layout-item {
    min-height: 60px;
    margin-top: 16px;
    margin-bottom: 16px;
  }
</style>
