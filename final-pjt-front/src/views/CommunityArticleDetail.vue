<template>
  <div>
    <nav-bar></nav-bar>
    <h1>CommunityArticleDetail</h1>
    <p>글 번호: {{ article?.id }}</p>
    <p>제목: {{ article?.title }}</p>
    <p>내용: {{ article?.content }}</p>
    <p>이미지: {{ article?.imagepath }}</p>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000' 

export default {
  name: 'CommunityArticleDetail',
  components: {
    NavBar,
  },
  data() {
    return {
      article: null
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${this.$route.params.community_id}/article/${this.$route.params.article_id}/`,
      })
      .then((res) => {
        // console.log(res)
        this.article = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>