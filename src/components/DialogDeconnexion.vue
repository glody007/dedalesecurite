<template>
  <div>
    <md-dialog-confirm
      :md-active.sync="active"
      :md-click-outside-to-close="false"
      md-title="Voulez-vous vous deconnecter de Dedale?"
      md-confirm-text="Oui"
      md-cancel-text="Non"
      @md-cancel="onCancel"
      @md-confirm="onConfirm" />
  </div>
</template>

<script>
export default {
  name: 'DialogDeconnexion',
  props: ['active'],
  data: () => ({

  }),
  methods: {
    onConfirm () {
      this.$emit('agreed')
      this.$store.commit('logout')
      this.$router.push({ name: 'login' })
    },
    onCancel () {
      this.$emit('cancel')
    }
  }
}
</script>
