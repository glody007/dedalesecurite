<template>
  <div id="main container">
    <div class="md-layout md-gutter ">
      <div class="button-save md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
        <md-button
          @click="addData"
          class="md-alignment-center-left
          button-save md-raised
          md-primary">
          Substituant simple
         </md-button>
      </div>
      <div class="button-save md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
         <md-button
           @click="addSecurized"
           class="md-alignment-center-left
           button-save md-raised
           md-accent">
           Substituant sécurisé
          </md-button>
      </div>
    </div>
    <div ref="quill"></div>
  </div>
</template>

<script>
import ImageKit from 'imagekit-javascript'
import Quill from '../quill'

let imagekit = new ImageKit({
  urlEndpoint: 'https://ik.imagekit.io/tlr7lkiwqbj',
  publicKey: 'public_7BOsJo+gJzQeU+O7WgThIpcpIc4=',
  authenticationEndpoint: 'api/auth/uploadendpoint'
})

export default {
  name: 'editor',
  data () {
    return {
      content: {
        ops: []
      },
      editor: null,
      config: {
        modules: {
          toolbar: [
            ['bold', 'italic', 'underline', 'strike'], // toggled buttons
            ['blockquote', 'code-block', 'image'],

            [{ 'header': 1 }, { 'header': 2 }], // custom button values
            [{ 'list': 'ordered' }, { 'list': 'bullet' }],
            [{ 'script': 'sub' }, { 'script': 'super' }], // superscript/subscript
            [{ 'indent': '-1' }, { 'indent': '+1' }], // outdent/indent
            [{ 'direction': 'rtl' }],

            [{ 'size': ['small', false, 'large', 'huge'] }], // custom dropdown
            [{ 'header': [1, 2, 3, 4, 5, 6, false] }],

            [{ 'color': [] }, { 'background': [] }], // dropdown with defaults from theme
            [{ 'font': [] }],
            [{ 'align': [] }],

            ['clean'] // remove formatting button
          ]
        },
        readOnly: false,
        placeholder: 'Ecrivez ici...',
        theme: 'snow'
      }
    }
  },
  components: {

  },
  mounted () {
    this.editor = new Quill(this.$refs.quill, this.config)
    this.editor.on('text-change', (delta, oldDelta, source) => {
      this.$emit('change', { document: JSON.stringify(this.editor.getContents()),
        datas: this.getDatas() })
    })
    this.editor.getModule('toolbar').addHandler('image', this.selectLocalImage)
  },
  methods: {
    saveToServer (file) {
      imagekit.upload({
        file: file,
        fileName: 'file.jpg'
      }, this.uploadCallback)
    },
    addData () {
      const range = this.editor.getSelection()
      let value = prompt('Entrer le nom de votre substituant')
      this.editor.insertEmbed(range.index, 'data', value)
    },
    addSecurized () {
      const range = this.editor.getSelection()
      let value = prompt('Entrer le nom de votre substituant sécurisé')
      this.editor.insertEmbed(range.index, 'securised', value)
    },
    getDatas () {
      const delta = this.editor.getContents()
      const datas = {}
      delta
        .filter((op) => {
          return op.insert.data || op.insert.securised
        })
        .map((op) => {
          if (op.insert.data) datas[op.insert.data] = 'string'
          else datas[op.insert.securised] = 'string'
        })
      return JSON.stringify(datas)
    },
    selectLocalImage () {
      const input = document.createElement('input')
      input.setAttribute('type', 'file')
      input.click()

      // Listen upload local image and save to server
      input.onchange = () => {
        const file = input.files[0]

        // file type is only image.
        if (/^image\//.test(file.type)) {
          this.saveToServer(file)
        } else {
          console.warn('You could only upload images.')
        }
      }
    },
    uploadCallback (err, result) {
      if (result) {
        const range = this.editor.getSelection()
        this.editor.insertEmbed(range.index, 'image', result.url)
      } else console.log(err)
    }
  }
}
</script>

<style lang="scss">
.data {
  color: white;
  background-color: blue;
  padding: 4px;
  border-radius: 2px;
}
.securised {
  color: white;
  background-color: red;
  padding: 4px;
  border-radius: 2px;
}
</style>
