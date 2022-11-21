<template>
  <div>
    <nav-bar></nav-bar>
    <h1>CommunityArticleDetail</h1>
    <p>글 번호: {{ article?.id }}</p>
    <p>제목: {{ article?.title }}</p>
    <p>작성시간: {{ articleCreatedAt }}</p>
    <p>수정시간: {{ articleUpdatedAt }}</p>

    <button class="btn btn-outline-danger waves-effect mb-4" @click="deleteArticle">삭제</button>

    <p>내용: {{ article?.content }}</p>
    <p>이미지: {{ article?.imagepath }}</p>

    <!-- 좋아요 button -->
    <div style="float: right; margin-top:15px;">
      <button class=" btn btn-outline-danger waves-effect mb-4" @click="likeArticle">
        <!-- {{ count }} 이렇게 하면 값이 안 나옴.. 왜지 -->
        좋아요 ♥ {{ this.article?.like_users.length }}
      </button>
    </div>
    <br><br><br>
    <hr>
    <hr>

    <CommunityArticleCommentView
      :article_id="article?.id"
      :community_id="article?.community.id"
    />
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import axios from 'axios'
import CommunityArticleCommentView from '@/views/CommunityArticleCommentView'

const API_URL = 'http://127.0.0.1:8000' 

export default {
  name: 'CommunityArticleDetail',
  components: {
    NavBar,
    CommunityArticleCommentView,
  },
  data() {
    return {
      article: null,
      count: this.article?.like_users.length,
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
    },
    deleteArticle() { 
      // this.$store.commit('DELETE_ARTICLE', this.article?.id)
      // this.$router.push({ name: 'community_article' })
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/community/${this.$route.params.community_id}/article/${this.$route.params.article_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        alert('삭제가 완료되었습니다.')
        this.$router.push({ name: 'community_article' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    likeArticle() {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/community/${this.$route.params.community_id}/article/${this.$route.params.article_id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        if (res.data === 1) {
          this.count += 1
        } else if (res.data === 0) {
          this.count -= 1
        }
        this.$router.go(this.$router.currentRoute)
      })
    }
  },
  computed: {
    articleCreatedAt() {
      const createdAt = new Date(this.article?.created_at).toLocaleString()
      return createdAt
    },
    articleUpdatedAt() {
      const updatedAt = new Date(this.article?.updated_at).toLocaleString()
      return updatedAt
    }
  },
}
</script>

<style>

</style>