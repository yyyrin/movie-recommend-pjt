<template>
  <div class="article-list">
    <!-- <router-link :to="{ name: my_profile }"><h1>My ArticleList</h1></router-link> -->
      <div v-if="articles" class="row row-cols-1 row-cols-md-5 g-3 center py-2">
        <ArticleItem
          v-for="article in articles"
          :key="article?.id"
          :article="article"
      />
    </div>      
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