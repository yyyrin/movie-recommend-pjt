<template>
  <div>
    <h1>OneLineReviewList</h1>
    <OneLineReviewItem
      v-for="review in reviews"
      :review="review"
      :key="review.id"
    />
    <!-- 리뷰 쓰는 form도 생성하기! -->
  </div>
</template>

<script>
import OneLineReviewItem from '@/components/MovieDetail/OneLineReviewItem'

export default {
  name: 'OneLineReviewList',
  components: {
    OneLineReviewItem,
  },
  computed: {
    reviews() {
      return this.$store.state.reviews
    }
  }
}
</script>

<style>

</style>