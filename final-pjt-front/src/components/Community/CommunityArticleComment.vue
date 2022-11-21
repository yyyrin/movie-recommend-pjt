<template>
  <div>
    <!-- {{ comment }} -->
    <p>댓글 내용: {{ comment.content }}</p>
    <p>작성자 id: {{ comment.user }}</p>
    <p>comment id: {{ comment.id }}</p>
    <p>article id: {{ comment.article }}</p>
    <button class="btn btn-outline-danger waves-effect mb-4" @click="deleteComment">삭제</button>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityArticleComment',
  props: {
    comment: Object,
  },
  methods: {
    deleteComment() {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/community/${this.$route.params.community_id}/article/${this.$route.params.article_id}/comments/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        alert('삭제가 완료되었습니다.')
        this.$router.go(this.$router.currentRoute)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
}
</script>

<style>

</style>