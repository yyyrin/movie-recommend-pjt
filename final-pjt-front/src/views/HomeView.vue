<template>
  <div id="home">
    <nav-bar></nav-bar>
    <!-- <MovieSlide/> -->
    <div id="recommend-cards">
      <p>추천 영화</p>
      <MovieCards/>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
// import MovieSlide from '@/components/Home/MovieSlide'
import MovieCards from '@/components/Home/MovieCards'

export default {
  name: 'HomeView',
  components: {
    NavBar,
    // MovieSlide,
    MovieCards,
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
#home {
  background-color: black;
  color: white;
}

#recommend-cards {
  margin: 20px;
}
</style>