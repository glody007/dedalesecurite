<template>
  <div class="container">
    <Title :text="template.name" />
    <div class="md-layout md-gutter">
      <div class="md-layout-item md-medium-size-900 md-small-size-100 md-xsmall-size-100">
        <md-tabs>
          <md-tab id="tab-template" md-label="Template">
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-900 md-small-size-100 md-xsmall-size-100">
                <Editor class="element"/>
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
  </div>
</template>

<script>
import Title from '@/components/Title.vue'
import Editor from '@/components/Editor.vue'
import Datas from '@/components/Datas.vue'
import QrCode from '@/components/QrCode.vue'

export default {
  name: 'NewTemplate',
  data: () => ({
    template: { 'name': 'Template: certificat' }
  }),
  components: {
    Title, Editor, Datas, QrCode
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
    max-width: 900px
  }
</style>
