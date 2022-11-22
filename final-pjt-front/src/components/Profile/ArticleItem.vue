<template>
  <div>
    <li class="list-group-item">
      <!-- <p>{{ article }}</p> -->
      <p>커뮤니티명: {{ article.community.name }}</p>
      <p>title:
        <router-link :to="{ name: 'community_article_detail', params: { community_id: article.community.id, article_id: article.id } }">
          {{ article.title }}
        </router-link>
      </p>
      <p>좋아요 수: {{ article?.like_users.length }}</p>
    </li>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
}
</script>

<style>

</style>