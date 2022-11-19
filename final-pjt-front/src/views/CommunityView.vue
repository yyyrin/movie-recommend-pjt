<template>
  <div>
    <nav-bar></nav-bar>
    <h1>CommunityView</h1>
    <CommunityCards/>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import CommunityCards from '@/components/Community/CommunityCards'

export default {
  name: 'CommunityView',
  components: {
    NavBar,
    CommunityCards
  },
  methods: {
    getCommunities() {
      this.$store.dispatch('getCommunities')
    }
  }
}
</script>

<style>

</style>