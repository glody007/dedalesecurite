<template>
  <div>
    <md-dialog :md-active.sync="active" :md-click-outside-to-close="false">
      <md-dialog-title>Generer</md-dialog-title>

      <div v-if="generating" class="md-layout-item md-xsmall-size-100">
        <div class="text-center mt-4">
          <b-spinner variant="primary"></b-spinner>
        </div>
      </div>

      <div v-if="!generating" class="md-layout md-gutter md-alignment-center-left">
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

        <div v-if="!generating" id="qr-code" @click="onGenerateQrCodeClicked"  class="md-layout-item md-medium-size-50 md-small-size-50 md-xsmall-size-100">
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
    <div ref="quill" id="canvas"></div>
  </div>
</template>

<script>
import Quill from '../quill'
import pdfMake from 'pdfmake/build/pdfmake'
import pdfFonts from 'pdfmake/build/vfs_fonts'
import html2canvas from 'html2canvas'
pdfMake.vfs = pdfFonts.pdfMake.vfs

export default {
  name: 'DialogGenerateQrCode',
  props: ['active', 'items', 'keys', 'templateNom', 'template'],
  data: () => ({
    docDefinition: {
      content: [],
      styles: {
        header: {
          fontSize: 18,
          bold: true,
          alignment: 'right',
          margin: [0, 0, 0, 10]
        },
        subheader: {
          fontSize: 14,
          margin: [5, 0, 0, 20]
        },
        qrcode: {
          margin: [5, 5, 5, 5]
        },
        qrcodedoc: {
          margin: [5, 5, 5, 5]
        }
      }
    },
    header: {
      text: '',
      style: 'header'
    },
    main: [],
    editor: null,
    generating: false
  }),
  methods: {
    onCancel () {
      this.$emit('cancel')
    },
    onGenerateDocumentClicked () {
      this.generating = true
      this.header.text = ''
      this.main = []
      this.items.forEach((item, i) => {
        let columns = []
        this.prepocessEditorHtml(item)
        html2canvas(document.getElementById('canvas'), {
          useCORS: true,
          allowTaint: true
        }).then(canvas => {
          columns.push({
            stack: [
              {
                qr: `www.dedalesecurite.com/verify/${item.id}`,
                style: 'qrcodedoc'
              },
              {
                image: canvas.toDataURL(),
                width: 500,
                pageBreak: 'after'
              }
            ]
          })
          this.main.push({ columns: columns })
          if (i === this.items.length - 1) {
            this.docDefinition.content = [this.header, this.main]
            pdfMake.createPdf(this.docDefinition).open({}, window.frames['printPdf'])
            this.editor.setContents({})
            this.generating = false
          }
        })
      })
    },
    prepocessEditorHtml (item) {
      this.editor = new Quill(this.$refs.quill)
      const delta = JSON.parse(this.template.document_model)
      delta.ops.forEach((op, i) => {
        if (op.insert && op.insert.data) op.insert = item[op.insert.data]
      })
      this.editor.setContents(delta)
    },
    onGenerateQrCodeClicked () {
      this.generating = true
      this.header.text = this.templateNom
      this.main = []
      let columns = []
      this.items.forEach((item, i) => {
        if (i % 3 === 0) {
          columns = []
          this.main.push({ columns: columns })
        }
        columns.push({
          width: 'auto',
          stack: [
            { qr: `www.dedalesecurite.com/verify/${item.id}`, style: 'qrcode' },
            { text: item[this.keys[0]], style: 'subheader' }
          ]
        })
      })
      this.docDefinition.content = [this.header, this.main]
      pdfMake.createPdf(this.docDefinition).open({}, window.frames['printPdf'])
      this.generating = false
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
  #canvas {
    padding: 5px;
  }
</style>
