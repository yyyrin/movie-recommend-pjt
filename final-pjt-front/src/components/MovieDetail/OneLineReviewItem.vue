<template>
  <div>
    <p>별점 : {{ review.rate }}</p>
    <p>한줄 리뷰 : {{ review.content }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'OneLineReviewItem',
  props: {
    review: Object,
  }
}
</script>

<style>

</style>