<template>
  <div>
    <nav-bar></nav-bar>
    <MovieCards/>
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
      if (this.isLogIn) {
        this.$store.dispatch('getMovies')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'login' })
      }
    }
  }
}
</script>

<style>

</style>