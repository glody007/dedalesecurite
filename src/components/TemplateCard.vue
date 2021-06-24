<template>
  <md-card md-with-hover>
    <md-ripple>
      <md-card-header>
        <div class="md-title">{{ name }}</div>
        <div class="md-subhead">Template existant</div>
      </md-card-header>

      <md-card-content>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed accusantium quasi non.
      </md-card-content>
    </md-ripple>
  </md-card>
</template>

<script>
export default {
  name: 'TemplateCard',
  props: ['name']
}
</script>
