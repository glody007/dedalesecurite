<template>
  <div>
    <md-dialog :md-active.sync="active" :md-click-outside-to-close="false">
      <md-dialog-title>Generer</md-dialog-title>

      <md-dialog-actions>
        <md-button class="md-primary" @click="onCancel">Annuler</md-button>
      </md-dialog-actions>
    </md-dialog>
  </div>
</template>

<script>
export default {
  name: 'DialogGenerateQrCode',
  props: ['active', 'items'],
  data: () => ({
    keys: []
  }),
  created () {
    for (const key in this.datas_model) this.keys.push(key)
  },
  methods: {
    onCancel () {
      this.$emit('cancel')
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
