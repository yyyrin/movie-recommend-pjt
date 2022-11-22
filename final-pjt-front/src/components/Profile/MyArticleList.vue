<template>
  <div class="my-article-list">
    <h1>My Article List</h1>
    <!-- <router-link :to="{ name: my_profile }"><h1>My ArticleList</h1></router-link> -->
    <ol class="list-group list-group-numbered">
      <MyArticleItem
        v-for="article in articles"
        :key="article.id"
        :article="article"
      />
    </ol>
  </div>
</template>

<script>
import MyArticleItem from '@/components/Profile/MyArticleItem'

export default {
  name: 'MyArticleList',
  props: {
    myInfo: Object,
  },
  components: {
    MyArticleItem,
  },
  computed: {
    articles() {
      return this.myInfo?.articles
    }
  },
}
</script>

<style>

</style>