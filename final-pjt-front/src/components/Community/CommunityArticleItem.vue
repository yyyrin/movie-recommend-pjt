<template>
  <tr>
    <!-- username -->
    <td>
      <router-link  :to="{ name: 'profile', params: { username: article?.user.username } }">
        <img :src=article?.user.img_path height="50" class="my-2">
        <p>{{ article?.user.username }}</p>
      </router-link>
    </td>
    <!-- title -->
    <td>
      <router-link
        :to="{ name: 'community_article_detail',
        params: { community_id: community_id, article_id: article.id } }">
          <span>
            <span style="font-size:18px;">{{ article.title }}</span>
          </span>
      </router-link>
    </td>
    <!-- 삭제 -->
    <td>
      <button class="btn btn-outline-danger btn-sm waves-effect" v-show="is_active" @click="deleteArticle">X</button>
    </td>

    <!-- <router-link  :to="{ name: 'profile', params: { username: article?.user.username } }">
        <img :src=article?.user.img_path height="50"></router-link>
    <p>작성자: <router-link :to="{ name: 'profile', params: { username: article?.user.username } }">{{ article?.user.username }}</router-link></p> -->
    <!-- <router-link
      :to="{ name: 'community_article_detail',
      params: { community_id: community_id, article_id: article.id } }">
        <p>{{ article.title }}</p>
    </router-link> -->
  </tr>
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