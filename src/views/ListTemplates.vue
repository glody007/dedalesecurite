<template>
  <div class="container">
    <Title text="Mes templates" />
    <div class="md-layout md-gutter">
      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
        <NewTemplateCard />
      </div>
      <div v-for="template in templates" :key="template.name" class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
        <TemplateCard :name="template.name" />
      </div>
    </div>
  </div>
</template>

<script>
import Title from '@/components/Title.vue'
import NewTemplateCard from '@/components/NewTemplateCard.vue'
import TemplateCard from '@/components/TemplateCard.vue'

export default {
  name: 'ListTemplates',
  data: () => ({
    templates: [
      { 'name': 'certificat' },
      { 'name': 'diplome' },
      { 'name': 'brevet' },
      { 'name': 'affectation' },
      { 'name': 'feuille de route' }
    ]
  }),
  components: {
    Title, NewTemplateCard, TemplateCard
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
