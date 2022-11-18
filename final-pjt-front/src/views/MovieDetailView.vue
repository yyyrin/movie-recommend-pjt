<template>
  <div>
    <nav-bar></nav-bar>
    <h1>Detail</h1>
    <p>영화 번호 : {{ movie?.id }}</p> 
    <!-- <p>장르 : {{ movie?.genre }}</p> -->
    <p>제목 : {{ movie?.title }}</p>
    <p>개봉일: {{ movie?.release_date }}</p>
    <p>내용 : {{ movie?.overview }}</p>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  components: {
    NavBar,
  },
  data() {
    return {
      movie: null,
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}`
      })
        .then((res) => {
          console.log(res)
          this.movie = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>