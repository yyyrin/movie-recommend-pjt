<template>
  <div id="community-article-comment-view">
    <CommunityArticleCommentList
      :article_id="article_id"
    />
    <CreateCommunityArticleComment
      :community_id="this.community_id"
      :article_id="this.article_id"
    />
    
  </div>
</template>

<script>
import CommunityArticleCommentList from '@/components/Community/CommunityArticleCommentList'
import CreateCommunityArticleComment from '@/components/Community/CreateCommunityArticleComment'

export default {
  name: 'CommunityArticleCommentView',
  components: {
    CommunityArticleCommentList,
    CreateCommunityArticleComment
  },
  props: {
    article_id: Number,
    community_id: Number,
  },
  created() {
    this.getComments()
  },
  methods: {
    getComments() {
      const community_id = this.$route.params.community_id
      const article_id = this.$route.params.article_id
      const payload = [Number(community_id), Number(article_id)]
      // console.log(payload)
      this.$store.dispatch('getComments', payload)
    }
  }
}
</script>

<style>
#community-article-comment-view {
  background-color:rgb(27, 27, 27);
  width: 1080px;
  margin: 0 auto;
  display: block;
  margin-bottom: 40px;
  border-radius: 5px;
}
</style>