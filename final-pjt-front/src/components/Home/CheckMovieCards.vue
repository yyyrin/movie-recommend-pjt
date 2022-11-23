<template>
  <div class="movie-cards">
    <div class="row row-cols-1 row-cols-md-5 g-3 center">
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
  name: 'CheckMovieCards',
  components: {
    MovieCard
  },
  computed: {
    movies() {
      // return this.$store.state.movies
      return this.$store.state.movies
    }
  }
}
</script>

<style>

</style>