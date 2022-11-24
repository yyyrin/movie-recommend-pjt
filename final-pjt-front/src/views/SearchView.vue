<template>
  <div>
    <nav-bar></nav-bar>

    <!-- search bar -->
    <div class="search">
      <svg version="1.1" viewBox="0 0 142.358 24.582">
        <path id="search-path" fill="none" d="M131.597,14.529c-1.487,1.487-3.542,2.407-5.811,2.407
        c-4.539,0-8.218-3.679-8.218-8.218s3.679-8.218,8.218-8.218c4.539,0,8.218,3.679,8.218,8.218
        C134.004,10.987,133.084,13.042,131.597,14.529c0,0,9.554,9.554,9.554,9.554H0"/>
      </svg>
      <label for="search" class="search-label"></label>
      <input type="search" id="search" @input="search" v-model="keyword" autocomplete="off" class="input-search">
      <!-- <input type="text" id="search" autocomplete="off" class="input-search"/> -->
    </div>

    <hr>

    <span v-for="(actor, index) in actors" :key="`a-${index}`">
      <span @click="change(actor.name)">{{actor.name}}      </span>
    </span>
    <hr>
      <span v-for="(direct, index) in director" :key="`d-${index}`">
        <span @click="change(direct.name)">{{direct.name}}      </span>
      </span>
    <hr>
    <span v-for="(movie, index) in movies" :key="`m-${index}`">
      <router-link :to="{ name: 'movie_detail', params: { id: movie.id } }">|{{movie.title}}|</router-link>
    </span>
  </div>
</template>

<script>
import axios from 'axios'
import NavBar from '@/components/templates/NavBar'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SearchView',
  components: {
    NavBar
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
  },
}
</script>

<style lang="scss">
$brand: #b3c33a;
$speed: 0.5s;

body {
    color: $brand;
    background-color: #333;
}

.search {
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: -300px;
    margin-top: -54px;
    width: 600px;
}

svg {
    position: absolute;
    transform: translateX(-246px);
    width: 600px;
    height: auto;
    stroke-width: 8px;
    stroke: $brand;
    stroke-width: 1px;
    stroke-dashoffset: 0;
    stroke-dasharray: 64.6 206.305;
    transition: all 0.5s ease-in-out;
    stroke-linejoin: round;
    stroke-linecap: round;
}

.input-search {
    position: absolute;
    width: calc(100% - 148px);
    height: 64px;
    top: 0;
    right: 20px;
    bottom: 0;
    left: 0;
    border: none;
    background-color: transparent;
    outline: none;
    padding: 20px;
    font-size: 50px;
    color: $brand;
}

.search-label {
    position: absolute;
    display: block;
    width: 108px;
    height: 108px;
    top: 0;
    left: 50%;
    margin-left: -54px;
    z-index: 100;
    transition: $speed ease-in-out;
}

.isActive {
    .search-label {
        transform: translateX(246px);
    }
    svg {
        stroke-dashoffset: -65;
        stroke-dasharray: 141.305 66;
        transform: translateX(0);
    }
    &.full svg {
        stroke-dashoffset: -65;
        stroke-dasharray: 141.305 66;
        transform: translateX(0);
    }
}

.full {
    .search-label {
        transform: translateX(246px);
    }
    svg {
        stroke-dashoffset: 0;
        stroke-dasharray: 64.6 206.305;
        transform: translateX(0);
    }
}
</style>