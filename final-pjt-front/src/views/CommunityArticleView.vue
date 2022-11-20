<template>
  <div class="community-article-view">
    <nav-bar></nav-bar>
    <p>이름: {{ community?.name }}</p>
    <p>썸네일 넣을 자리: {{ community?.thumbnail }}</p>
    <router-link :to="{ name: 'community_article_create' }">
      [CREATE]
    </router-link>
    <ul class="list-group list-group-flush">
      <CommunityArticleList
        :community_id="community?.id"
      />
    </ul>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import CommunityArticleList from '@/components/Community/CommunityArticleList'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000' 

export default {
  name: 'CommunityArticleView',
  components: {
    NavBar,
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

</style>