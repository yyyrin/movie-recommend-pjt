<template>
  <div id="community-comment">
    <div class="bubble sb14">
      <div class="d-flex">
        <div class="m-2 d-flex justify-content-around">
          <div>
            <div style="text-align: center;">{{ comment.content }}</div>
            <div>
              <button class="btn btn-danger waves-effect mb-1 btn-sm" v-show="is_active" @click="deleteComment">삭제</button>
              <button class="btn btn-danger waves-effect mb-1 btn-sm" v-show="is_active1" @click="reportComment">신고</button>
            </div>
          </div>
            <!-- <router-link  :to="{ name: 'profile', params: { username: comment?.user.username } }">
              <p style="text-align:center; color: white;">{{ comment?.user.username }}</p>
            </router-link><br> -->
        </div>
      </div>
    </div>

    <!-- {{ comment }} -->
    <!-- <p>댓글 내용: {{ comment.content }}</p>
    <p>작성자 id: {{ comment.user }}</p> -->
    <!-- <button class="btn btn-outline-danger waves-effect mb-1 btn-sm" v-show="is_active" @click="deleteComment">삭제</button>
    <button class="btn btn-outline-danger waves-effect mb-1 btn-sm" v-show="is_active1" @click="reportComment">신고</button> -->
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
  data() {
    return {
     is_active: 1,
     is_active1: 0
    }
  },
  created() {
    if (this.comment.user != this.$store.state.pk) {
          this.is_active = 0
          this.is_active1 = 1
    }
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
    },
    reportComment() {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/report/${this.comment.user}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
      })
      .catch((err) => {
        console.log(err)
      })      
    },
  },
}
</script>

<style>
/* #community-comment {
  background-color: rgb(19, 17, 17);
} */
</style>