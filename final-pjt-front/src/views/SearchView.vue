<template>
  <div>
    <nav-bar></nav-bar>
    <h1>SearchView</h1>
    <input type="text"  @input="search" v-model="keyword">
    <p>{{movies}}</p>
    <p>{{actors}}</p>
    <p>{{director}}</p>
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
    }
  },
}
</script>

<style>

</style>