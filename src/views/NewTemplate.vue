<template>
  <div class="container">
    <Title text="Nouveau template" />
    <div class="md-layout md-gutter">
      <div class="md-layout-item md-xsmall-size-100">
        <Editor class="editor" />
      </div>
    </div>
  </div>
</template>

<script>
import Title from '@/components/Title.vue'
import Editor from '@/components/Editor.vue'

export default {
  name: 'NewTemplate',
  components: {
    Title, Editor
  }
}
</script>

<style lang="scss" scoped>
  .md-layout-item {
    display: flex;
    margin-top: 16px;
  }
</style>
