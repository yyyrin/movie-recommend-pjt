<template>
  <div id="genre-view">
    <nav-bar></nav-bar>
    <h1>GenreView</h1>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'

export default {
  name: 'GenreView',
  components: {
    NavBar
  },
}
</script>

<style>
 #genre-view {
  background-color: black;
  color: white;
 }
</style>