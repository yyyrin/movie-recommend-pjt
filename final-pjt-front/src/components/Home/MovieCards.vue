<template>
  <div>
    <div class="row row-cols-1 row-cols-md-3 g-5 center p-5">
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

</style>