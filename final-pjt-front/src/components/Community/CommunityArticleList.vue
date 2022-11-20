<template>
  <div class="community-article-list">
    <CommunityArticleItem
        v-for="(article, index) in articles"
        :key="index"
        :article="article"
        :community_id="community_id"
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
    community_id: Number,
  },
  computed: {
    articles() {
      // return this.$store.state.articles.article_set
      return this.$store.state.articles.article_set.filter((article) => {
        return article.id === this.community_id;
      })
    }
  },
}
</script>

<style>

</style>