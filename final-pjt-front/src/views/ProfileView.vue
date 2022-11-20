<template>
  <div id="ProfileView">
    <nav-bar></nav-bar>
    <h1>MY PROFILE</h1>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'

export default {
  name: 'ProfileView',
  components: {
    NavBar
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