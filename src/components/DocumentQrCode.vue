<template>
  <div class="container">
    <div class="md-layout info">
      <span class="">
        Selectionnez un ou plusieurs elements du tableau pour generer des documents ou de QR code de verification.
      </span>
    </div>
    <md-table v-model="listDatas" md-card @md-selected="onSelect">
      <md-table-toolbar>
        <h1 class="md-title">Donnees associer au template</h1>
      </md-table-toolbar>

      <md-table-toolbar slot="md-table-alternate-header" slot-scope="{ count }">
        <div class="md-toolbar-section-start">{{ getAlternateLabel(count) }}</div>

        <div class="md-toolbar-section-end">
          <md-button
            class="md-primary md-raised"
            @click="showDialogClicked">
            <md-icon>
              qr_code_2
            </md-icon>
            Generer
          </md-button>
        </div>
      </md-table-toolbar>

      <md-table-row slot="md-table-row" slot-scope="{ item }" md-selectable="multiple" class="md-primary">
        <md-table-cell v-for="key in keys" :key="key" :md-label="key" :md-sort-by="key">{{ item[key] }}</md-table-cell>
      </md-table-row>
    </md-table>
    <DialogGenerateQrCode
      :active="showDialogAdd"
      :items="this.selected"
      :keys="this.keys"
      :templateNom="this.template.nom"
      :template="this.template"
      @cancel="showDialogAdd = false"/>
  </div>
</template>

<script>
import DialogGenerateQrCode from '@/components/DialogGenerateQrCode.vue'

export default {
  name: 'DocumentQrCode',
  props: ['template', 'listDatas'],
  data: () => ({
    selected: null,
    keys: [],
    datas_model: null,
    error: false,
    loading: true,
    showDialogAdd: false
  }),
  components: {
    DialogGenerateQrCode
  },
  created () {
    this.datas_model = JSON.parse(this.template.datas_model)
    for (const key in this.datas_model) this.keys.push(key)
  },
  methods: {
    showDialogClicked () {
      window.scrollTo(0, 0)
      this.showDialogAdd = true
    },
    getAlternateLabel (count) {
      return `Vous avez choisi ${count}`
    },
    onSelect (item) {
      this.selected = item
    }
  }
}
</script>

<style lang="scss" scoped>
.info {
  padding-left: 32px;
  padding-bottom: 32px;
}
</style>
