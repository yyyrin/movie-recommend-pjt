<template>
  <div id="community-view">
    <nav-bar></nav-bar>
    <h1>CommunityView</h1>
    <router-link :to="{ name: 'check' }">임시 선호영화 링크</router-link>
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
  background-color: black;
  color: white;
}
</style>