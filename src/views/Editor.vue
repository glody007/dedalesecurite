<template>
  <div id="main">
    <div id="editor">
    </div>
  </div>
</template>

<script>

import EditorJS from '@editorjs/editorjs'
import Header from '@editorjs/header'
import Paragraph from 'editorjs-paragraph-with-alignment'
import ImageTool from '@editorjs/image'
import ImageKit from "imagekit-javascript"

let imagekit = new ImageKit({
    urlEndpoint: "https://ik.imagekit.io/tlr7lkiwqbj",
    publicKey: "public_7BOsJo+gJzQeU+O7WgThIpcpIc4=",
    authenticationEndpoint: "api/auth/uploadendpoint"
})

let upload = (file) => {
  return new Promise((resolve, reject) => {
      imagekit.upload({
          file: file,
          fileName: "abc1.jpg",
          tags: ["tag1"]
      }, function(err, result) {
            if (result) resolve(result.url)
            else reject(new Error('upload failed'))
      })
    })
    .then(url => {
      return {
                success: 1,
                file: { url: url }
              }
    })
    .catch(err => {
      console.log(err)
      return { success: 0 }
    })
}

const editor = new EditorJS({
  holder: 'editor',
  tools: {
    paragraph: {
      placeholder: 'Entrer un titre',
      class: Paragraph,
      inlineToolbar: true
    },
    header: {
      class: Header,
      config: {
        placeholder: 'Enter a header',
        levels: [1, 2, 3, 4],
        defaultLevel: 3
      }
    },
    image: {
      class: ImageTool,
      config: {
        uploader: {
          uploadByFile (file) {
            return upload(file)
          },
          uploadByUrl (url) {
            return upload(url)
          }
        }
      }
    }
  }
})

export default {
  name: 'editor',
  components: {

  },
  methods: {

  }
}
</script>

<style lang="scss">

</style>
