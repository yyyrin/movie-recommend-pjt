<template>
  <div>
    <h2>선호영화를고르세오</h2>
    <h3>{{4-choosen.length}}개 남았습니다</h3>
    <hr>
    <br>
    <div class="movie-cards">
      <div class="row row-cols-1 row-cols-md-5 g-3 center">
        <CheckMovieCard
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
          @choosed="getData"
        />
      </div>
    </div>
  </div>
</template>

<script>
import CheckMovieCard from '@/components/Home/CheckMovieCard.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'GenreView',
  components: {
    CheckMovieCard
  },
  data() {
    return {
      choosen: []
    }
  },
  computed: {
    movies() {
      // return this.$store.state.movies
      return this.$store.state.movies
    }
  },
  methods: {
    getData: function(movie){
      if (this.choosen.indexOf(movie.id)> -1) {
        this.choosen.splice(this.movies.indexOf(movie.id),1)
      }else if (this.choosen.length<4){
        this.choosen.push(movie.id)
      }
      if (this.choosen.length === 4){
        const params = this.choosen.join(' ')
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/preference/${params}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
          this.$router.push({ name: 'home' })
        })
        .catch((err) => {
          console.log(err)
        })
        alert('선호 영화 조사완료!')
      }
      console.log(this.choosen)
    }
  }
}
</script>

<style>
 #genre-view {
  background-color: black;
  color: white;
  padding-top: 90px;
 }
</style>