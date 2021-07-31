<template>
  <div class="container">
    <div class="md-layout md-gutter ">
      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
        <span class="md-title title">Template</span>
      </div>

      <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
        <md-switch @change="onSwitch" v-model="templateProtected">Proteger</md-switch>
      </div>
    </div>

    <div v-if="loading || loadingListDatas" class="md-layout-item md-xsmall-size-100">
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
                <Datas
                  :template="template"
                  :listDatas="listDatas"
                  @fetchListDatas="fetchListDatas"
                  class="element"/>
              </div>
            </div>
          </md-tab>
          <md-tab id="tab-qr-code" md-label="Documents et QR Codes">
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-80 md-small-size-80 md-xsmall-size-33">
                <DocumentQrCode
                  :template="template"
                  :listDatas="listDatas"
                  class="element"/>
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
    <md-snackbar md-position="center" :md-duration="4000" :md-active.sync="errorSwitch" md-persistent>
      <span>Une erreur est survenue! réessayez</span>
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
    loadingListDatas: true,
    error: true,
    errorSwitch: false,
    templateProtected: false,
    listDatas: []
  }),
  components: {
    Title, TemplateDocument, Datas, DocumentQrCode
  },
  created () {
    this.fetchTemplateAndDatas()
  },
  watch: {
    '$route': 'fetchTemplateAndDatas'
  },
  methods: {
    onSwitch () {
      this.loading = true
      this.errorSwitch = false
      $backend.setTemplateProtection(this.$route.params.id, {
        protected: this.templateProtected
      })
        .then(response => {
          this.loading = false
        })
        .catch(error => {
          console.log(error)
          this.errorSwitch = true
          this.loading = false
        })
    },
    fetchTemplateAndDatas () {
      this.fetchTemplate()
        .then(response => {
          this.fetchListDatas()
        })
    },
    fetchTemplate () {
      this.loading = true
      this.error = false
      return $backend.fetchTemplate(this.$route.params.id)
        .then(response => {
          this.loading = false
          this.template = response.data
          this.templateProtected = this.template.protected
        })
        .catch(error => {
          console.log(error)
          this.error = true
          this.loading = false
        })
    },
    fetchListDatas () {
      this.loadingListDatas = true
      this.error = false
      $backend.fetchListDatas(this.template.id)
        .then(response => {
          this.loading = false
          return response.data['list datas'].map((element) => {
            const values = JSON.parse(element.values)
            values.id = element.id
            return values
          })
        })
        .then(datas => {
          this.loadingListDatas = false
          this.listDatas = datas
        })
        .catch(error => {
          console.log(error)
          this.error = true
          this.loadingListDatas = false
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
