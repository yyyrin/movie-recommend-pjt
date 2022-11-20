<template>
  <div>
    <h1>CommunityArticleCommentList</h1>
    {{ comments }}
    <CommunityArticleComment
      v-for="comment in comments"
      :comment="comment"
      :key="comment.id"
    />
  </div>
</template>

<script>
import CommunityArticleComment from '@/components/Community/CommunityArticleComment'

export default {
  name: 'CommunityArticleCommentList',
  components: {
    CommunityArticleComment,
  },
  props: {
    article_id: Number,
  },
  computed: {
    comments() {
      return this.$store.state.comments
      // return this.$store.state.comments.filter((comment) => {
      //   return comment.article_id === this.article_id;
      // })
    }
  }
}
</script>

<style>

</style>