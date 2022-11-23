<template>
  <div id="home">
    <nav-bar></nav-bar>
    <!-- <MovieSlide/> -->
    <!-- 1. 추천영화 -->
    <section>
      <div id="recommend-cards" style="background-color: rgb(27, 27, 27)">
        <div class="title d-flex justify-content-between mx-5">
          <h1 tabindex="0" class="title-area">
            <span class="label">추천 영화</span>
          </h1>
          <a href="">더보기</a>
        </div>
        <MovieCards/>
      </div>
    </section>

    <!-- 2.  -->
    <section>
      <div id="recommend-cards" style="background-color: rgb(27, 27, 27)">
        <div class="title d-flex justify-content-between mx-5">
          <h1 tabindex="0" class="title-area">
            <span class="label">추천 영화</span>
          </h1>
          <a href="">더보기</a>
        </div>
        <MovieCards/>
      </div>
    </section>

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
  margin: 30px 180px 30px 180px;
  padding: 20px;
}

.title {
  padding-left: 50;
  padding-right: 50;
}
</style>