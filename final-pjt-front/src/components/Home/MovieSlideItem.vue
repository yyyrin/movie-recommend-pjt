<template>
  <div>
    <router-link>
      <slide>
          <img :src="movieURL" alt="movie_poster">
        </slide>
    </router-link>
  </div>
</template>

<script>
import Slide from 'vue-carousel-3d'
import 'swiper/dist/css/swiper.css'

export default {
  name: 'MovieSlideItem',
  components: {
    // Carousel3d,
    Slide,
  },
  props: {
    movie: Object,
  },
  computed: {
    movieURL() {
      const posterPath = this.movie?.poster_path
      // null값 check
      if (!posterPath && typeof posterPath === 'object') {
        return '@/assets/basic_profile.png'
      } else {
        return `https://image.tmdb.org/t/p/w500/${posterPath}`  // 여기서 get 오류가 나는데..?
      }
    }
  }
}
</script>

<style>

</style>