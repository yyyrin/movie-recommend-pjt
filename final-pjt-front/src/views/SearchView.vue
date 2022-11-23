<template>
  <div>
    <nav-bar></nav-bar>
    <h1>SearchView</h1>
    <input type="text"  @input="search" v-model="keyword">
    <hr>
    <span v-for="(actor, index) in actors" :key="`a-${index}`">
      <span @click="change(actor.name)">{{actor.name}}      </span>
    </span>
    <hr>
      <div v-for="(direct, index) in director" :key="`d-${index}`">
        <span @click="change(direct.name)">{{direct.name}}      </span>
        <br>
      </div>
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

<style>

</style>