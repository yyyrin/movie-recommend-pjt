<template>
  <div id="community-comment-list" class="py-3">
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
      // console.log(this.$store.state.comments.comment_set)
      return this.$store.state.comments.comment_set.filter((comment) => {
        return comment.article === this.article_id;
      })
    }
  }
}
</script>

<style>
#community-comment-list {
  width: 950px;
  margin: 0 auto;
  display: block;
}
</style>