<template>
  <div class="title">
    <span class="md-title">{{ text }}</span>
  </div>
</template>

<script>
export default {
  name: 'Title',
  props: ['text']
}
</script>

<style lang="scss" scoped>
  .title {
    display: flex;
    margin-top: 32px;
    margin-left: 16px;
  }
</style>
