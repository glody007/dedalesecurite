<template>
  <div id="main">
    <div ref="quill"></div>
  </div>
</template>

<script>

import ImageKit from 'imagekit-javascript'
import Quill from 'quill'

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
    this.editor.getModule('toolbar').addHandler('image', this.selectLocalImage)
  },
  methods: {
    saveToServer (file) {
      imagekit.upload({
        file: file,
        fileName: 'file.jpg'
      }, this.uploadCallback)
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

</style>
