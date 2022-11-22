<template>
  <div id="MyProfileView">
    <nav-bar></nav-bar>
    <h1>MY PROFILE</h1>
    <MyProfileInto
      :myInfo="myInfo"
    />
    <hr>
    <MyArticleList
      :myInfo="myInfo"
    />
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import MyProfileInto from '@/components/Profile/MyProfileInto'
import MyArticleList from '@/components/Profile/MyArticleList'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    NavBar,
    MyProfileInto,
    MyArticleList
  },
  data() {
    return {
      myInfo: null,
    }
  },
  created() {
    this.getUserInfo()
  },
  methods: {
    getUserInfo() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/my/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        // console.log(res)
        this.myInfo = res.data
        // console.log(this.myInfo)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}
</script>

<style>
#ProfileView {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #FF6800;
}
</style>