<template>
  <div id="movie-detail-view">
    <nav-bar></nav-bar>
    <div>
      <h1>Detail</h1>
      <p>영화 번호 : {{ movie?.id }}</p> 
      <p>장르 번호 : {{ movie?.genres }}</p>
      <p>배우 번호 : {{ movie?.actors }}</p>
      <p>감독 번호 : {{ movie?.director }}</p>
      <p>제목 : {{ movie?.title }}</p>
      <p>런타임 : {{ movie?.runtime }}</p>
      <p>개봉일: {{ movie?.release_date }}</p>
      <p>내용 : {{ movie?.overview }}</p>
      <div>
        <img :src="movieURL" alt="movie_poster">
      </div>
    </div>
    <!-- 한줄리뷰 리스트 -->
    <div class="one-line-review-list">
    <OneLineReviewView
      :movie_id = "movie?.id"
    />
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import axios from 'axios'
import OneLineReviewView from '@/views/OneLineReviewView'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  components: {
    NavBar,
    OneLineReviewView
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
          // console.log(res)
          this.movie = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
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
 #movie-detail-view {
  background-color: black;
  color: white;
 }
</style>