<template>
  <div>
    <md-dialog :md-active.sync="active" :md-click-outside-to-close="false">
      <md-progress-bar v-if="loading" md-mode="indeterminate"/>
      <md-dialog-title>Associer des nouvelles donnees a votre template</md-dialog-title>

      <div class="form" v-if="form">
        <md-field v-for="key in keys" :key="key">
          <label :for="key">{{ key }}</label>
          <md-input :name="key" :id="key" v-model="form[key]"/>
          <span v-if="form[key] === ''" class="erreur">{{ key }} obligatoire</span>
        </md-field>
      </div>
      <span v-if="error" class="erreur">Une erreur est survenue veuillez réessayez</span>

      <md-dialog-actions>
        <md-button class="md-primary" @click="onCancel">Annuler</md-button>
        <md-button class="md-primary" @click="onSave" :disabled='disabled'>Enregistrer</md-button>
      </md-dialog-actions>
    </md-dialog>
  </div>
</template>

<script>
import $backend from '../backend'

export default {
  name: 'DialogAddDatas',
  props: ['active', 'datas_model', 'templateId'],
  data: () => ({
    keys: [],
    datas: null,
    form: null,
    loading: false,
    error: false
  }),
  created () {
    const form = {}
    for (const key in this.datas_model) {
      this.keys.push(key)
      form[key] = ''
    }
    this.form = form
  },
  computed: {
    disabled () {
      for (const key in this.form) {
        if (this.form[key] === '') return true
      }
      return false
    }
  },
  methods: {
    inputGroupId (key) {
      return `input-group-${key}`
    },
    onSave () {
      this.loading = true
      $backend.createDatas(this.templateId, {
        values: JSON.stringify(this.form)
      })
        .then(response => {
          this.loading = false
          this.clear()
          this.$emit('saved', response.data.datas)
        })
        .catch(error => {
          console.log(error)
          this.error = true
          this.loading = false
        })
    },
    onCancel () {
      this.clear()
      this.$emit('cancel')
    },
    clear () {
      this.error = false
      for (const key in this.form) this.form[key] = ''
    }
  }
}
</script>

<style lang="scss" scoped>
  .form {
    padding-left: 32px;
    padding-right: 32px;
  }
  .md-progress-bar {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
  }
  .erreur {
    margin-left: 32px;
    color: red;
  }
</style>
