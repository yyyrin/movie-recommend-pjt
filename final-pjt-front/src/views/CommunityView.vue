<template>
  <div id="community-view">
    <nav-bar></nav-bar>
    <!-- <h1>Community</h1> -->
    <br><br>
    <CreateCommunity/>
    <br><br>
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
  background-image: url("../assets/lionking.png");
  padding-top: 90px;
  /* background-color: black; */
  color: white;
}
h1 {
  font-size: 60px;
}
</style>