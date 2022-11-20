<template>
  <div id="movie-cards">
    <div class="row row-cols-1 row-cols-md-5 g-3 center p-5">
      <MovieCard
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/Home/MovieCard.vue'

export default {
  name: 'MovieCards',
  components: {
    MovieCard
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  }
}
</script>

<style>
#movie-cards {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}
</style>