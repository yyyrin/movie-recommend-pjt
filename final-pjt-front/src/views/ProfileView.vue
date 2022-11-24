<template>
  <div id="ProfileView">
    <nav-bar></nav-bar>
    <img :src="userInfo?.user.img_path" height="100">
    <!-- <p>유저 이미지 변경 나중에 : {{ userInfo?.user.img_path }}</p> -->
    <p>사용자: {{ userInfo?.user.username }}</p>
    <!-- 회원정보수정 -->
    <EditProfile
      :userInfo="userInfo"
      :is_active1="is_active1"
    />

    <button class="btn btn-outline-danger waves-effect mb-4" v-show="is_active" @click="report">신고</button>
    <hr>
    <!-- <router-link :to="{ name: 'my_article' }"><h3>My Article List</h3></router-link> -->
    <ArticleList :userInfo="userInfo"/>
    <ReviewList :userInfo="userInfo"/>
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import EditProfile from '@/components/Profile/EditProfile'
import ArticleList from '@/components/Profile/ArticleList'
import ReviewList from '@/components/Profile/ReviewList'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    NavBar,
    EditProfile,
    ArticleList,
    ReviewList,
  },
  data() {
    return {
      userInfo: null,
      is_active: 1,
      is_active1: 0,
    }
  },
  created() {
    this.getUserInfo()
  },
  methods: {
    getUserInfo() {
      console.log(this.$route.params.username)
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${this.$route.params.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        // console.log(res)
        this.userInfo = res.data
        if (this.userInfo.user.username === this.$store.state.username) {
          this.is_active = 0
          this.is_active1 = 1
        }
        // console.log(this.myInfo.reviews)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    report() {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/report/${this.userInfo.user.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        // console.log(res)
        console.log(res.data)
        // console.log(this.myInfo.reviews)
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
  padding-top: 90px;
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