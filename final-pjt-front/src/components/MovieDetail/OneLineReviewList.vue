<template>
  <div class="one-line-reveiw-list">
    <OneLineReviewItem
      v-for="(review, index) in reviews"
      :review="review"
      :key="index"
    />
    <CreateOneLineReview/>
  </div>
</template>

<script>
import OneLineReviewItem from '@/components/MovieDetail/OneLineReviewItem'
import CreateOneLineReview from '@/components/MovieDetail/CreateOneLineReview'

export default {
  name: 'OneLineReviewList',
  components: {
    OneLineReviewItem,
    CreateOneLineReview,
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