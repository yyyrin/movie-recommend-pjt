<template>
  <div id="movie-detail-view">
    <nav-bar></nav-bar>
    <!-- 1. movie detail section -->
    <section class="movie-detail">
      <div id="movie-detail-carousel" class="carousel slide" data-bs-touch="false">
        <div class="carousel-inner">
          <!-- Carousel-기본 -->
          <div class="carousel-item active" data-bs-interval="false">
            <!-- movie detail -->
            <article class="d-flex justify-content-between mx-5 my-4 px-5 py-3">
              <!-- 포스터 제외 -->
              <br>
              <div style="margin:80px; text-align:left;">
                <div style="font-size: 60px">{{ movie?.title }}</div>
                <br><br><br>
                <!-- tag button -->
                <span>
                  <button type="button" class="btn btn-outline-secondary btn-sm m-1" disabled>{{ movie?.release_date.substr(0, 4) }}</button>
                  <button type="button" class="btn btn-outline-secondary btn-sm m-1" disabled>{{ movie?.runtime }}분</button>
                  <span v-for="(genre, index) in genres" :key="`g-${index}`">
                    <router-link :to="{ name: 'search', params: {keyword: `${genre.name}`} }">
                      <button type="button" class="btn btn-outline-secondary btn-sm m-1">
                        {{genre?.name}}
                      </button>
                    </router-link>
                  </span>
                </span>

                <br><br>
                <!-- director, actor info -->
                <div>
                  감독 &nbsp; &nbsp;
                  <span v-for="(director, index) in directors" :key="`d-${index}`">
                      <router-link :to="{ name: 'search', params: {keyword: `${director.name}`} }">
                        {{director?.name}} &nbsp;
                      </router-link>
                    </span>
                </div>
                <div>
                  출연 &nbsp; &nbsp;
                  <span v-for="(actor, index) in actors" :key="`a-${index}`">
                    <router-link :to="{ name: 'search', params: {keyword: `${actor.name}`} }">
                      {{ actor?.name }} &nbsp;
                    </router-link>
                  </span>
                </div>
                <br>
                <!-- 줄거리 -->
                <p style="width:600px; word-break:keep-all;">
                  {{ movie?.overview }}
                </p>
                <p>평점{{movie?.vote_average.toFixed(2)}}({{movie?.vote_count}}명이 평가했습니다.)</p>
                <!-- 별점 -->
                <div class="my-3">
                  <!-- 별점 & 리뷰 -->
                  <div class="mx-2">
                      <span
                        class="star"
                        v-for="index in 5"
                        :key="index"
                      >
                        <span v-if="index < (movie?.vote_average)/2+0.5">
                          <img src="@/assets/full3.png" alt="" height="30px;">
                        </span>
                        <span v-if="index >= (movie?.vote_average)/2+1">
                          <img src="@/assets/empty3.png" alt="" height="30px;">
                        </span>
                        <span v-if="index*2 >(movie?.vote_average) && (index-1)*2 <(movie?.vote_average)">
                          <img src="@/assets/middle3.png" alt="" height="30px;">
                        </span>
                      </span>
                  </div>
                </div>
              </div>
              <!-- movie poster -->
              <div>
                <img :src="movieURL" alt="movie_poster" style="height: 700px; ">
              </div>
            </article>
          </div>
          <!-- Carousel trailer -->
          <div v-if="logic" class="carousel-item" data-bs-interval="false">
            <div >
              <iframe :src=movie?.trailer style="display:block; width:100vw; height: 100vh"></iframe> 
            </div>
          </div>
        </div>
        <!-- Carousel button -->
        <button class="carousel-control-prev" type="button" data-bs-target="#movie-detail-carousel" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#movie-detail-carousel" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </section>

    <br><br>
    <hr>
    <br><br>

    <!-- 2. 한줄리뷰 리스트 -->
    <div class="one-line-review-list">
    <OneLineReviewView
      :movie_id = "movie?.id"
      :movie = "movie"
    />
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import axios from 'axios'
import OneLineReviewView from '@/views/OneLineReviewView'

const API_URL = 'http://127.0.0.1:8000'
//const API_KEY = 'API_KEY 입력 필요'
//const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'MovieDetailView',
  components: {
    NavBar,
    OneLineReviewView
  },
  data() {
    return {
      movie: null,
      genres: [],
      actors: [],
      directors: [],
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
          // console.log(res.data)
          this.movie = res.data
          for (const id of res.data.genres){
            axios({
              method: 'get',
              url: `${API_URL}/api/v1/urname/${Number(id)}`
            })
              .then((res) => {
                this.genres.push(res.data)
              })
              .catch((err) => {
                this.$router.push('/404')
                console.log(err)
              })
            }
            for (const id of res.data.actors){
            axios({
              method: 'get',
              url: `${API_URL}/api/v1/urname/${Number(id)}`
            })
              .then((res) => {
                this.actors.push(res.data)
              })
              .catch((err) => {
                this.$router.push('/404')
                console.log(err)
              })
            }
            for (const id of res.data.director){
            axios({
              method: 'get',
              url: `${API_URL}/api/v1/urname/${Number(id)}`
            })
              .then((res) => {
                this.directors.push(res.data)
              })
              .catch((err) => {
                this.$router.push('/404')
                console.log(err)
              })
            }
            })
            .catch((err) => {
              this.$router.push('/404')
              console.log(err)
            })
      
    },
    getGenre(query) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/urname/${Number(query)}`
      })
        .then((res) => {
          this.genres.push(res.data)
        })
        .catch((err) => {
          this.$router.push('/404')
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
        return `https://image.tmdb.org/t/p/w500/${posterPath}`
      }
    },
    logic() {
      if (this.movie?.trailer==="[]") {
        return 0
      }else {
        return 1
      }
    }
  }
}
</script>

<style>
#movie-detail-view {
  padding-top: 90px;
  background-color: black;
  color: white;
}
a {
  text-decoration: none;
  color: white;
}
#movie-detail-view a:hover {
  color: #FF6800;
}
img {
  border-style: none;
}
hr {
  width:85%;
  text-align: center;
  margin:auto;
}
</style>