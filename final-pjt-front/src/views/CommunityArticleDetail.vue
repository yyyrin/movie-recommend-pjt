<template>
  <div id="community-article-detail">
    <nav-bar></nav-bar>
    <!-- {{ article }} -->

    <div id="whole-body" class="py-1">
      <!-- article -->
      <div id="article-body">
        <!-- article-head -->
        <div class="post-tit-info">
          <h2 class="article-title py-5">{{ article?.title }}</h2>
          <!-- username, img -->
          <div class="writer mx-5" style="">
            <div class="d-flex justify-content-between">
              <span>
                <router-link  :to="{ name: 'profile', params: { username: article?.user.username } }" height="10px;">
                  <img :src=article?.user.img_path height="30">
                </router-link>
                <p id="article-detail-username"><router-link :to="{ name: 'profile', params: { username: article?.user.username } }" style="font-size:11px; color: #999;">{{ article?.user.username }}</router-link></p>
              </span>

              <div class="d-flex flex-column">
                <!-- 삭제 or 신고 -->
                <button class="btn btn-outline-danger btn-sm waves-effect mb-4" v-show="is_active" @click="deleteArticle">삭제</button>
                <button class="btn btn-outline-danger btn-sm waves-effect mb-4" v-show="is_active1" @click="reportArticle">신고</button>
                <span class="date d-flex align-items-end" style="font-size:11px; color: #999; margin-left=5px;">{{ articleCreatedAt }}</span>
              </div>
            </div>
          </div>
        </div>
        <!-- article-content -->
        <div class="posting">
          <div style="font-size: 15px; line-height: 1.3;">
            <div class="p-5">
              <img :src="`${ article?.imagepath }`" alt="">
              <div id="contentArea" class="my-3">{{ article?.content }}</div>
            </div>
          </div>
          <!-- 좋아요 -->
          <div style="float: right; margin-top:15px; margin-right: 15px;">
            <button class=" btn btn-outline-danger waves-effect mb-4" :count= count @click="likeArticle">
              <!-- {{ count }} 이렇게 하면 값이 안 나옴.. 왜지 -->
              좋아요 ♥ {{ count }}
            </button>
          </div>
        </div>
      </div>
    </div>

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
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${this.$route.params.community_id}/article/${this.$route.params.article_id}/`,
      })
      .then((res) => {
        this.article = res.data
        this.count = this.article?.like_users.length
      })
      .catch(err => {
        this.$router.push('/404')
        console.log(err)
      })
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
        this.$router.push('/404')
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
      .then(() => {
      })
      .catch((err) => {
        this.$router.push('/404')
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
      if (this.article?.user.pk === this.$store.state.pk) {
        return 1
      }else{
        return 0
      }
    },
    is_active1() {
      if (this.article?.user.pk != this.$store.state.pk) {
        return 1
      }else {
        return 0
      }
    }
  },
}
</script>

<style>
#community-article-detail {
  padding-top: 90px;
  color: white;
}
#whole-body {
  width: 1080px;
  margin: 0 auto;
  display: block;
  margin-bottom: 70px;
}
#article-body {
  background-color: rgb(27, 27, 27);
  border-radius: 5px;
  display: block;
}
#article-detail-username {
  margin-bottom: -1px;
}
.post-tit-info {
  position: relative;
  width: 1080px;
  padding: 34px 0 14px 0;
  border-bottom: 1px solid #e5e5e5;
  clear: both;
}
.article-title {
  padding: 11px 0 0 0;
  font-size: 40px;
  line-height: 1.2;
  letter-spacing: -1px;
}
.writer {
  position: relative;
  padding: 8px 0 0;
  font-size: 13px;
  color: #999;
  z-index: 2;
}
</style>