<template>
  <div id="app">
    <!-- <router-link :to="{ name: 'signup' }">Signup First~~</router-link> -->
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR&display=swap');
#app {
  font-family: 'IBM Plex Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}
/* font-family: 'Roboto Condensed', sans-serif;
@font-face {
  font-family: 'IBMPlexSansKR-Regular';
  src: url(./assets/font/IBMPlexSansKR-Regular.tff) format("woff");
  font-weight: normal;
  font-style: normal;
} */

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
