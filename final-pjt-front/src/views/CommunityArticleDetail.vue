<template>
  <div>
    <nav-bar></nav-bar>
    <!-- {{ article }} -->
    <h1>CommunityArticleDetail</h1>
    <p>글 번호: {{ article?.id }}</p>
    <p>제목: {{ article?.title }}</p>
    <p>작성시간: {{ articleCreatedAt }}</p>
    <p>수정시간: {{ articleUpdatedAt }}</p>
    <p>작성자: <router-link :to="{ name: 'profile', params: { username: article?.user.username } }">{{ article?.user.username }}</router-link></p>
    <router-link  :to="{ name: 'profile', params: { username: article?.user.username } }">
        <img :src=article?.user.img_path height="50"></router-link>

    <!-- 삭제 -->
    <button class="btn btn-outline-danger waves-effect mb-4" v-show="is_active" @click="deleteArticle">삭제</button>
    <button class="btn btn-outline-danger waves-effect mb-4" v-show="is_active1" @click="reportArticle">신고</button>

    <p>내용: {{ article?.content }}</p>
    <p>이미지: {{ article?.imagepath }}</p>

    <!-- 좋아요 button -->
    <div style="float: right; margin-top:15px;">
      <button class=" btn btn-outline-danger waves-effect mb-4" :count= count @click="likeArticle">
        <!-- {{ count }} 이렇게 하면 값이 안 나옴.. 왜지 -->
        좋아요 ♥ {{ count }}
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
      count: 0,
    }
  },
  created() {
    console.log('11')
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
        this.count = this.article?.like_users.length
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
        if (res.data.result === 1) {
          this.count += 1
        } else if (res.data.result === 0) {
          this.count -= 1
        }
        // this.$router.go(this.$router.currentRoute)
      })
    },
    reportArticle() {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/report/${this.article.user.pk}/`,
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
  computed: {
    articleCreatedAt() {
      const createdAt = new Date(this.article?.created_at).toLocaleString()
      return createdAt
    },
    articleUpdatedAt() {
      const updatedAt = new Date(this.article?.updated_at).toLocaleString()
      return updatedAt
    },
    is_active() {
      if (this.article.user.pk === this.$store.state.pk) {
        return 1
      }else{
        return 0
      }
    },
    is_active1() {
      if (this.article.user.pk != this.$store.state.pk) {
        return 1
      }else {
        return 0
      }
    }
  },
}
</script>

<style>

</style>