<template>
  <div id="YourProfileView">
    <nav-bar></nav-bar>
    <h1>PROFILE</h1>
    <!-- <ProfileInto/> -->
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'

export default {
  name: 'YourProfileView',
  components: {
    NavBar,
  },

}
</script>

<style>
#ProfileView {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #FF6800;
}
</style>