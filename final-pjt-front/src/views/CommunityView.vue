<template>
  <div id="community-view">
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
  created() {
    this.getCommunities()
  },
  methods: {
    getCommunities() {
      this.$store.dispatch('getCommunities')
    }
  }
}
</script>

<style>
#community-view {
  padding-top: 90px;
  background-color: black;
  color: white;
}
</style>