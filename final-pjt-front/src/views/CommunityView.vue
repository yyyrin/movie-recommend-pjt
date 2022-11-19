<template>
  <div>
    <nav-bar></nav-bar>
    <h1>CommunityView</h1>
    <CreateCommunity/>
    <CommunityCards/>
  </div>
</template>
                 
<script>
import NavBar from '@/components/templates/NavBar'
import CreateCommunity from '@/components/Community/CreateCommunity'
import CommunityCards from '@/components/Community/CommunityCards'

export default {
  name: 'CommunityView',
  components: {
    NavBar,
    CreateCommunity,
    CommunityCards,
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