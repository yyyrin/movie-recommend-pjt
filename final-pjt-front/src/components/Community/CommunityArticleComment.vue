<template>
  <div>
    <h1>CommunityArticleComment</h1>
    <p>댓글 내용: {{ comment.context }}</p>
    <p>작성자 id: {{ comment.user_id }}</p>
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