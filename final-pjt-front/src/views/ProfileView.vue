<template>
  <div id="ProfileView">
    <nav-bar></nav-bar>

    <!-- 프로필 전체 -->
    <div id="profile-view">
      <!-- 프로필 상단 -->
      <div id="upper-profile" class="my-5">
        <img :src="userInfo?.user.img_path" height="100">
        <!-- <p>유저 이미지 변경 나중에 : {{ userInfo?.user.img_path }}</p> -->
        <p>{{ userInfo?.user.username }}</p>
        <!-- 회원정보수정 -->
        <EditProfile
          :userInfo="userInfo"
          :is_active1="is_active1"
        />
        <button class="btn btn-outline-danger waves-effect btn-sm mb-4" v-show="is_active" @click="report">신고</button>
      </div>

      <hr>
      <div id="bottom-profile" class="my-2">
        <span @click="Article_Review1" style="font-size:30px">Article &nbsp;</span>
        <span style="font-size:30px">|</span>
        <span @click="Article_Review2" style="font-size:30px">&nbsp; Review </span>
        <div class="">
          <ArticleList v-if="logic == 1" :userInfo="userInfo"/>
          <ReviewList v-if="logic == 0" :userInfo="userInfo"/>
        </div>
      </div>
    </div>
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
      logic: 1,
    }
  },
  created() {
    this.getUserInfo()
  },
  methods: {
    getUserInfo() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${this.$route.params.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.userInfo = res.data
        if (this.userInfo.user.username === this.$store.state.username) {
          this.is_active = 0
          this.is_active1 = 1
        }
        // console.log(this.myInfo.reviews)
      })
      .catch((err) => {
        this.$router.push('/404')
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
      .then(() => {
      })
      .catch((err) => {
        this.$router.push('/404')
        console.log(err)
      })      
    },
    Article_Review1() {
      this.logic = 1
    },
    Article_Review2() {
      this.logic = 0
    }
  },
}
</script>

<style>
#ProfileView {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
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
#profile-view {
  width: 1080px;
  margin: 0 auto;
}
#upper-profile {
  width: 700px;
  margin: 0 auto;
}
</style>