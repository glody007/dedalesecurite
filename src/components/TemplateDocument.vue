<template>
  <div id="main">
    <div ref="quill" class="md-layout-item md-xsmall-size-100">
    </div>
  </div>
</template>

<script>
import Quill from 'quill'

export default {
  name: 'templateDocument',
  props: ['template'],
  data () {
    return {
      content: {
        ops: []
      },
      editor: null,
      config: {
        modules: {
          toolbar: []
        },
        readOnly: true,
        placeholder: '',
        theme: 'snow'
      }
    }
  },
  components: {

  },
  mounted () {
    this.editor = new Quill(this.$refs.quill, this.config)
    this.editor.setContents(JSON.parse(this.template.document_model))
  }
}
</script>

<style lang="scss">
  .contenu {
    width: 200px
  }
</style>
