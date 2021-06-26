<template>
  <div>
    <md-dialog-confirm
      :md-active.sync="active"
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
    value: null
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
