<template>
  <div>
    <nav-bar></nav-bar>
    <MovieCards/>
    <h1>HomeView</h1>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import MovieCards from '@/components/Home/MovieCards'

export default {
  name: 'HomeView',
  components: {
    NavBar,
    MovieCards
  },
  computed: {
    isLogIn() {
      return this.$store.getters.isLogIn
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style>

</style>