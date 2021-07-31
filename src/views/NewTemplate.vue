<template>
  <div class="container">
    <Title text="Nouveau template" />
    <div class="content">
      <div class="md-layout md-gutter ">
        <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
          <md-field>
            <label>Entrer le nom du template</label>
            <md-input v-model="template.nom"></md-input>
          </md-field>
        </div>

        <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
          <div class="button-save md-layout-item  md-xsmall-size-100">
            <div class="text-center mt-4" v-if="loading">
              <b-spinner variant="primary"></b-spinner>
            </div>
            <md-button
              v-else
              @click="createTemplate"
              :disabled="!templateNameValidated"
              class="md-alignment-center-left
              button-save md-raised
              md-primary
              register-button">
              <md-icon>save_alt</md-icon>
              Enregistrer le template
            </md-button>
          </div>
        </div>
      </div>
      <div class="md-layout md-gutter">
        <div class="md-layout-item md-xsmall-size-100">
          <Editor class="editor" @change="getModel"/>
        </div>
      </div>
    </div>
    <md-snackbar md-position="center" :md-duration="5000" :md-active.sync="error" md-persistent>
      <span>Probleme de connection!</span>
    </md-snackbar>
  </div>
</template>

<script>
import Title from '@/components/Title.vue'
import Editor from '@/components/Editor.vue'
import $backend from '../backend'

export default {
  name: 'NewTemplate',
  components: {
    Title, Editor
  },
  data: () => ({
    template: {
      nom: '',
      document_model: '{}',
      datas_model: '{}'
    },
    loading: false,
    error: false
  }),
  computed: {
    templateNameValidated () {
      return this.template.nom.length > 0
    }
  },
  methods: {
    createTemplate () {
      this.loading = true
      $backend.createTemplate(this.template)
        .then(response => {
          this.loading = false
          const templateId = response.data.template.id
          this.$router.push({ name: 'template', params: { id: templateId } })
        })
        .catch(error => {
          console.log(error)
          this.error = true
          this.loading = false
        })
    },
    getModel (model) {
      this.template.document_model = model.document
      this.template.datas_model = model.datas
    }
  }
}
</script>

<style lang="scss" scoped>
  .md-layout-item {
    display: flex;
    margin-top: 16px;
  }
  .content {
    margin-left: 16px;
  }
  .button-save {
    display: flex;
    justify-content: end;
  }
</style>
