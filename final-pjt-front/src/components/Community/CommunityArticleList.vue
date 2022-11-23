<template>
  <div class="community-article-list">
    <CommunityArticleItem
        v-for="article in articles"
        :key="article.id"
        :article="article"
        :community_id="community.id"
        :community_user_id="community.user.pk"
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
    community: Object,
  },
  computed: {
    articles() {
      // return this.$store.state.articles.article_set
      return this.$store.state.articles.article_set.filter((article) => {
        return article.community.id === this.community?.id
      })
    }
  },
}
</script>

<style>

</style>