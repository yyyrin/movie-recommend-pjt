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
    </li>
  </div>
</template>

<script>
export default {
  name: 'MyArticleItem',
  props: {
    article: Object,
  },
}
</script>

<style>

</style>