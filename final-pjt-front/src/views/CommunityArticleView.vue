<template>
  <div class="community-article-view">
    <nav-bar></nav-bar>
    <h1>CommunityArticleView</h1>
    <ul class="list-group list-group-flush">
      <CommunityArticleList/>
    </ul>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import CommunityArticleList from '@/components/Community/CommunityArticleList'
// import axios from 'axios'

// const API_URL = 'http://127.0.0.1:8000' 

export default {
  name: 'CommunityArticleView',
  // data() {
  //   return {
  //     articles: null,
  //   }
  // },
  components: {
    NavBar,
    CommunityArticleList,
  },
  computed: {
    isLogIn() {
      return this.$store.getters.isLogin
    }
  },
  // created() {
  //   this.getArticles()
  // },
  // method: {
  //   getArticles() {
  //     axios({
  //       method: 'get',

  //     })
  //   }
  // },
  // computed: {
  //   articles() {
  //     return this.$store.state.articles
  //     // return this.$store.state.articles.filter((article) => {
  //     //   return article.community_id === 
  //     // })
  //   }
  // },
}
</script>

<style>

</style>