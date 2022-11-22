<template>
  <div class="article-list">
    <h1>Article List</h1>
    <!-- <router-link :to="{ name: my_profile }"><h1>My ArticleList</h1></router-link> -->
    <ol class="list-group list-group-numbered">
      <ArticleItem
        v-for="article in articles"
        :key="article.id"
        :article="article"
      />
    </ol>
  </div>
</template>

<script>
import ArticleItem from '@/components/Profile/ArticleItem'

export default {
  name: 'ArticleList',
  props: {
    userInfo: Object,
  },
  components: {
    ArticleItem,
  },
  computed: {
    articles() {
      return this.userInfo?.articles
    }
  },
}
</script>

<style>

</style>