<template>
  <div>
    <h1>CommunityArticleCommentView</h1>
    <CommunityArticleCommentList
      :article_id="article_id"
    />
    {{ community_id }}<br>
    {{ article_id }}
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
      // const ids = {community_id: this.community_id, article_id: this.article_id}
      // console.log(ids)
      const community_id = this.community_id
      const article_id = this.article_id
      // console.log(community_id)
      this.$store.dispatch('getComments', {community_id, article_id})
    }
  }
}
</script>

<style>

</style>