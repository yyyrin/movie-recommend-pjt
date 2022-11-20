<template>
  <div>
    <router-link
      :to="{ name: 'community_article_detail',
      params: { community_id: community_id, article_id: article.id } }">
      <li class="list-group-item">
        <p>{{ article.title }}</p>
      </li>
    </router-link>
  </div>
</template>

<script>

export default {
  name: 'CommunityArticleItem',
  props: {
    article: Object,
    community_id: Number,
  },
}
</script>

<style>

</style>