<template>
  <div class="container">
    <Title :text="template.nom" />
    <div v-if="loading" class="md-layout-item md-xsmall-size-100">
      <div class="text-center mt-4">
        <b-spinner variant="primary"></b-spinner>
      </div>
    </div>
    <div v-if="!loading && !error" class="md-layout md-gutter md-alignment-center-left">
      <div class="md-layout-item md-xsmall-size-100">
        <md-tabs>
          <md-tab id="tab-template" md-label="Template">
            <div class="md-layout">
              <div class="md-layout-item md-xsmall-size-33">
                <TemplateDocument :template="template" class="element"/>
              </div>
            </div>
          </md-tab>
          <md-tab id="tab-datas" md-label="Donnees">
            <Datas class="element"/>
          </md-tab>
          <md-tab id="tab-qr-code" md-label="QR Code">
            <QrCode class="element"/>
          </md-tab>
        </md-tabs>
      </div>
    </div>
    <md-snackbar md-position="center" :md-duration="Infinity" :md-active.sync="error" md-persistent>
      <span>Probleme de connection!</span>
      <md-button class="md-primary" @click="fetchTemplate">réessayez</md-button>
    </md-snackbar>
  </div>
</template>

<script>
import Title from '@/components/Title.vue'
import TemplateDocument from '@/components/TemplateDocument.vue'
import Datas from '@/components/Datas.vue'
import QrCode from '@/components/QrCode.vue'
import $backend from '../backend'

export default {
  name: 'NewTemplate',
  data: () => ({
    template: {
      nom: '',
      document_model: '{}',
      datas_model: '{}'
    },
    loading: true,
    error: true
  }),
  components: {
    Title, TemplateDocument, Datas, QrCode
  },
  created () {
    this.fetchTemplate()
  },
  watch: {
    '$route': 'fetchTemplate'
  },
  methods: {
    fetchTemplate () {
      this.loading = true
      this.error = false
      $backend.fetchTemplate(this.$route.params.id)
        .then(response => {
          this.loading = false
          this.template = response.data
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
    display: flex;
    margin-top: 16px;
  }
  .element {
    margin-left: 0px;
    margin-right: 0px;
    padding-right: 0px;
    padding-left: 0px;
    min-height: 100vh;
  }
</style>
