<template>
  <div>
    <p>댓글 내용: {{ comment.content }}</p>
    <p>작성자 id: {{ comment.user }}</p>
    <p>comment id: {{ comment.id }}</p>
    <p>article id: {{ comment.article }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'CommunityArticleComment',
  props: {
    comment: Object,
  }
}
</script>

<style>

</style>