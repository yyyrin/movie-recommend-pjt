<template>
  <div id="movie-cards">
    <div>
      <!-- {{ movies }} -->
    </div>
    <div class="movie-genres row row-cols-1 row-cols-md-5 g-3 center">
      <MovieCard
        v-for="movie in movies?.slice(0, leng)"
        :key="movie?.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/Home/MovieCard.vue'

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieCards',
  components: {
    MovieCard
  },
  data() {
    return {
      movies: null
    }
  },
  created() {
    this.getmovies()
  },
  computed: {
    leng() {
      if (this.movies?.length>5) {
        return 5
      }
      else {
        return this.movies?.length
      }
    }
  },
  methods: {
    getmovies() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/recommand/`,
        headers: {Authorization: `Token ${this.$store.state.token}`}
      })
        .then((res) => {
          this.movies = res.data
        })
        .catch(()=> {})
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