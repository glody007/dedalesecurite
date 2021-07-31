<template>
  <div class="container">
    <md-table v-model="listDatas" md-card @md-selected="onSelect">
      <md-table-toolbar>
        <h1 class="md-title">Donnees associer au template</h1>
        <div class="md-toolbar-section-end">
          <md-button
            class="md-primary md-raised"
            @click="showDialogAdd=true">
            <md-icon>add</md-icon>
            Ajouter
          </md-button>
        </div>
      </md-table-toolbar>

      <md-table-row slot="md-table-row" slot-scope="{ item }" md-selectable="single" class="md-primary">
        <md-table-cell v-for="key in keys" :key="key" :md-label="key" :md-sort-by="key">{{ item[key] }}</md-table-cell>
      </md-table-row>
    </md-table>
    <DialogAddDatas
      :active="showDialogAdd"
      :datas_model="datas_model"
      :templateId="template.id"
      @cancel="showDialogAdd = false"
      @saved="onSaved"/>
  </div>
</template>

<script>
import DialogAddDatas from '@/components/DialogAddDatas.vue'

export default {
  name: 'Datas',
  props: ['template', 'listDatas'],
  data: () => ({
    selected: null,
    keys: [],
    datas_model: null,
    showDialogAdd: false
  }),
  components: {
    DialogAddDatas
  },
  created () {
    this.datas_model = JSON.parse(this.template.datas_model)
    for (const key in this.datas_model) this.keys.push(key)
  },
  methods: {
    onSelect (item) {
      this.selected = item
    },
    onSaved (datas) {
      this.showDialogAdd = false
      this.fetchListDatas()
    },
    fetchListDatas () {
      this.$emit('fetchListDatas')
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
