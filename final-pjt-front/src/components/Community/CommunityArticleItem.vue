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