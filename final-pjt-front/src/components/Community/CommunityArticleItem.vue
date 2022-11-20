<template>
  <div>
    <router-link :to="{ name: 'community_article_detail', params: { id: article.id } }">
      <li class="list-group-item">
        {{ article.title }}
      </li>
    </router-link>
  </div>
</template>

<script>
// import axios from 'axios'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityArticleItem',
  props: {
    article: Object,
    // name: String,
  },
}
</script>

<style>

</style>