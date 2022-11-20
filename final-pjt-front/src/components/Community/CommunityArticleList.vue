<template>
  <div>
    <h1>CommunityArticle</h1>
    <CommunityArticleItem
        v-for="article in articles"
        :key="article.id"
        :article="article"
      />
  </div>
</template>

<script>
import CommunityArticleItem from '@/components/Community/CommunityArticleItem'

export default {
  name: 'CommunityArticleList',
  components: {
    CommunityArticleItem,
  },
  props: {
    id: Number,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
}
</script>

<style>

</style>