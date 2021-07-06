<template>
  <div>
    <md-dialog :md-active.sync="active" :md-click-outside-to-close="false">
      <md-dialog-title>Generer</md-dialog-title>

      <div class="md-layout md-gutter md-alignment-center-left">
        <div id="document" @click="onGenerateDocumentClicked" class="md-layout-item md-medium-size-50 md-small-size-50 md-xsmall-size-100">
          <md-card class="md-accent card" md-with-hover>
            <md-ripple>
              <md-card-header>
                <div class="md-title">Documents</div>
                <div class="md-subhead">
                  Generer des documents contenant les QR Codes a partir du template avec les donnees selectionnees.
                </div>
              </md-card-header>
            </md-ripple>
          </md-card>
        </div>

        <div id="qr-code" @click="onGenerateQrCodeClicked"  class="md-layout-item md-medium-size-50 md-small-size-50 md-xsmall-size-100">
          <md-card class="md-accent card" md-with-hover>
            <md-ripple>
              <md-card-header>
                <div class="md-title">QR Codes</div>
                <div class="md-subhead">
                  Generer des QR Codes a partir des donnees selectionnees.
                </div>
              </md-card-header>
            </md-ripple>
          </md-card>
        </div>
      </div>

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
    },
    onGenerateDocumentClicked () {
    },
    onGenerateQrCodeClicked () {
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
  .card {
    margin: 16px;
    min-height: 30vh;
  }
</style>
