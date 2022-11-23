<template>
  <div id="movie-cards">
    <!-- <div>
      {{ movies }}
    </div> -->
    <div class="row row-cols-1 row-cols-md-5 g-3 center py-2">
      <MovieCard
        v-for="movie in movies.slice(0, 5)"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/Home/MovieCard.vue'
// import _ from 'lodash'

const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'MovieGenreCards',
  data() {
    return {
      movies: null,
    }
  },
  props: {
    genre: String,
  },
  components: {
    MovieCard
  },
  created() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/search/${this.genre}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
    })
    .then((res) => {
      this.movies = res.data
    })
  },
  // methods: {
  //   movies() {
  //     // return this.$store.state.movies
  //     return _.orderBy(this.movies.filter((movie) => {
  //       console.log(movie.genre)
  //       return movie.genre === this.genre
  //     }), 'vote_average', 'desc')
  //   }
  // }
}
</script>

<style>
#movie-cards {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}

</style>