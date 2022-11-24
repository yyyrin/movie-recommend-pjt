<template>
  <div id="community-article-view">
    <nav-bar></nav-bar>

    <div id="community-body" class="py-1">
      <div id="front-img">
        <img :src="`${ community?.thumbnail }`" alt="커뮤니티명" width="1080px" height="280px" style="vertical-align:top; object-fit:cover">
      </div>

      <div id="community-info" class="py-1 d-flex">
        <div class="p-2 w-100">{{ community?.name }}</div>
        <div class="p-2 flex-shrink-1">
          <EditCommunity :community="community"/>
        </div>
      </div>
      <CommunityArticleList :community="community"/>
      <!-- article create -->
      <div id="create-article-btn" class="d-flex justify-content-end">
        <router-link :to="{ name: 'create_community_article' }">
          <v-btn fab x-large>
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import EditCommunity from '@/components/Community/EditCommunity'
import CommunityArticleList from '@/components/Community/CommunityArticleList'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000' 

export default {
  name: 'CommunityArticleView',
  components: {
    NavBar,
    EditCommunity,
    CommunityArticleList,
  },
  data() {
    return {
      community: null,
    }
  },
  // computed: {
  //   isLogIn() {
  //     return this.$store.getters.isLogIn
  //   }
  // },
  created() {
    this.getCommunityDetail()
    this.getArticles()
  },
  methods: {
    getCommunityDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${this.$route.params.community_id}/`
      })
      .then((res) => {
        // console.log(res)
        this.community = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getArticles() {
      this.$store.dispatch('getArticles', `${this.$route.params.community_id}`)
      // axios({
      //   method: 'get',
      //   url: `${API_URL}/api/v1/community/${this.$route.params.community_id}/`,
      // })
      // .then((res) => {
      //   console.log(res)
      // })
      // .catch((err) => {
      //   console.log(err)
      // })
    }
  },
}
</script>

<style>
#community-article-view {
  color: white;
  padding-top: 90px;
}
#community-body {
  width: 1080px;
  margin: 0 auto;
  display: block;
}
#front-img {
  position: relative;
  width: 1080px;
  max-height: 400px;
}
#community-info {
  width: 1080px;
  margin: 20px auto 20px;
  border: 1px solid white;
  box-sizing: border-box;
  font-size: 28px;
  font-weight: bold;
}
#create-article-btn {
  margin-left: 75%;
  position: fixed;
  bottom: 40px;
}
</style>