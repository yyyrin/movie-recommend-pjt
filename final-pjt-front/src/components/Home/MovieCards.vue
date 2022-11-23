<template>
  <div id="movie-cards">
    <div>
      <!-- {{ movies }} -->
    </div>
    <div class="movie-genres row row-cols-1 row-cols-md-5 g-3 center">
      <MovieCard
        v-for="movie in movies.slice(0, 5)"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/Home/MovieCard.vue'
import _ from 'lodash'

export default {
  name: 'MovieCards',
  components: {
    MovieCard
  },
  computed: {
    movies() {
      // return this.$store.state.movies
      return _.orderBy(this.$store.state.movies, 'vote_average', 'desc')
    }
  }
}
</script>

<style>
#movie-cards {
  width: 90%;
  border-style: none;
  /* margin-left: auto;
  margin-right: auto; */
}
.movie-genres {
  padding: 50;
}
</style>