<template>
  <div class="container">
    <div class="md-layout md-gutter ">
      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
        <span class="md-title title">Template</span>
      </div>

      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
        <md-switch @change="onSwitch" v-model="templateProtected">templateProtected</md-switch>
      </div>
    </div>

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
              <div class="md-layout-item md-medium-size-80 md-small-size-50 md-xsmall-size-33">
                <TemplateDocument :template="template" class="element"/>
              </div>
            </div>
          </md-tab>
          <md-tab id="tab-datas" md-label="Donnees">
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-80 md-small-size-80 md-xsmall-size-33">
                <Datas :template="template" class="element"/>
              </div>
            </div>
          </md-tab>
          <md-tab id="tab-qr-code" md-label="Documents et QR Codes">
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-80 md-small-size-80 md-xsmall-size-33">
                <DocumentQrCode :template="template" class="element"/>
              </div>
            </div>
          </md-tab>
        </md-tabs>
      </div>
    </div>
    <md-snackbar md-position="center" :md-duration="Infinity" :md-active.sync="error" md-persistent>
      <span>Une erreur est survenue!</span>
      <md-button class="md-primary" @click="fetchTemplate">réessayez</md-button>
    </md-snackbar>
  </div>
</template>

<script>
import Title from '@/components/Title.vue'
import TemplateDocument from '@/components/TemplateDocument.vue'
import Datas from '@/components/Datas.vue'
import DocumentQrCode from '@/components/DocumentQrCode.vue'
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
    error: true,
    templateProtected: true
  }),
  components: {
    Title, TemplateDocument, Datas, DocumentQrCode
  },
  created () {
    this.fetchTemplate()
  },
  watch: {
    '$route': 'fetchTemplate'
  },
  methods: {
    onSwitch () {
      console.log(this.templateProtected)
    },
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
  .title {
    display: flex;
    margin-top: 10px;
    margin-left: 16px;
  }
</style>
