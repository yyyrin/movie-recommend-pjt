<template>
  <div>
    <nav-bar></nav-bar>

    <div id="search-view">

      <!-- 1. search bar -->
      <div id="search-bar" class="my-5 mx-5 d-flex justify-content-center" style="width:900px;">
        <img src="@/assets/search.png" height="50px" class="mx-2" alt="">
        <input class="form-control form-control-lg" type="text" placeholder="장르, 감독, 배우로 찾아보세요" aria-label=".form-control-lg example" id="search" @input="search" v-model="keyword" autocomplete="off">
        <!-- <input type="search" id="search" @input="search" v-model="keyword" autocomplete="off" class="input-search"> -->
        <!-- <input type="text" id="search" autocomplete="off" class="input-search"/> -->
      </div>
      
      <!-- 2. 검색 결과 -->
      <div id="search-results" class="m-5">
        <!-- 2-1. 배우 검색 결과 -->
        <div id="actor-search-results" class="d-flex justify-content-center">
          <span v-for="(actor, index) in actors" :key="`a-${index}`">
            <div class="mx-4" @click="change(actor.name)">
            <!-- <span @click="change(actor.name)"> -->
              <img :src="`https://image.tmdb.org/t/p/w500/${actor?.profile_path}`" @error="change_path" style="height: 150px; overflow: hidden;"><br>
              <button type="button" class="btn btn-light btn-sm m-1">
                {{ actor?.name }}
              </button>      
            </div>
          </span>
        </div>

        <hr>
        <br><br>

        <!-- 2-2. 감독 검색 결과 -->
        <div id="director-search-results" class="d-flex justify-content-center">
          <span v-for="(direct, index) in director" :key="`d-${index}`">
            <div class="mx-4" @click="change(direct.name)">
              <img :src="`https://image.tmdb.org/t/p/w500/${direct?.profile_path}`" @error="change_path" style="height: 150px; overflow: hidden;">    
              <button type="button" class="btn btn-light btn-sm m-1">
                {{ direct?.name }}
              </button>
            </div>
          </span>
        </div>

        <hr>
        <br><br>

        <div class="movie-recommend row row-cols-1 row-cols-md-6 g-3 center">
          <MovieCard
            v-for="(movie, index) in movies"
            :key="`m-${index}`"
            :movie="movie"
          />
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import NavBar from '@/components/templates/NavBar'
import MovieCard from '@/components/Home/MovieCard.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SearchView',
  components: {
    NavBar,
    MovieCard
  },
  data() {
    return {
      keyword: this.$route.params.keyword,
      movies: null,
      actors: null,
      director: null,
    }
  },
  created() {
    axios({
        method: 'get',
        url: `${API_URL}/api/v1/search/${this.keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.movies = res.data
      })
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/actors/${this.keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.actors = res.data
      })
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/directors/${this.keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.director = res.data
      })
  },
  methods: {
    search: function(event){
      this.keyword = event.target.value
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/search/${this.keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.movies = res.data
      })
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/actors/${this.keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.actors = res.data
      })
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/directors/${this.keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.director = res.data
      })
    },
    change: function(val){
      this.keyword = val
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/search/${this.keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.movies = res.data
      })
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/actors/${this.keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.actors = res.data
      })
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/directors/${this.keyword}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.director = res.data
      })
    },
    change_path(e) {
      e.target.src =""
      e.target.style = "  width=100px;"
    }
  },
}
</script>

<style>

#search-view {
  padding-top: 90px;
  width: 1080px;
  margin: 0 auto;
}
#search-bar {
  border-color: white;
}
.search-results {
  margin: 30px 120px 30px 120px;
  color: white;
  width: 1200px;
  /* text-align: center; */
}
#actor-search-results {
  margin: 30px 120px 30px 120px;
  background-color: rgb(27, 27, 27);
  padding: 20px;
}
#director-search-results {
  margin: 30px 120px 30px 120px;
  background-color: rgb(27, 27, 27);
  padding: 20px; 
}
.movie-recommend {
  margin: 30px 120px 30px 120px;
  background-color: rgb(27, 27, 27);
  padding: 20px;
}
</style>