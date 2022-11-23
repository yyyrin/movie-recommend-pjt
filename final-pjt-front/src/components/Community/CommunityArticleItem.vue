<template>
  <div>
    <router-link  :to="{ name: 'profile', params: { username: article?.user.username } }">
        <img :src=article?.user.img_path height="50"></router-link>
    <p>작성자: <router-link :to="{ name: 'profile', params: { username: article?.user.username } }">{{ article?.user.username }}</router-link></p>
    <router-link
      :to="{ name: 'community_article_detail',
      params: { community_id: community_id, article_id: article.id } }">
      <li class="list-group-item">
        <p>{{ article.title }}</p>
      </li>
    </router-link>
    <button class="btn btn-outline-danger waves-effect mb-4" v-show="is_active" @click="deleteArticle">삭제</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityArticleItem',
  props: {
    article: Object,
    community_id: Number,
    community_user_id: Number,
  },
  methods: {
    deleteArticle() { 
      // this.$store.commit('DELETE_ARTICLE', this.article?.id)
      // this.$router.push({ name: 'community_article' })
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/community/${this.community_id}/article/${this.article.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        alert('삭제가 완료되었습니다.')
        this.$router.go({ name: 'community_article' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  computed: {
    is_active() {
      if (this.community_user_id === this.$store.state.pk) {
        return 1
      }else{
        return 0
      }
    },    
  }
}
</script>

<style>

</style>