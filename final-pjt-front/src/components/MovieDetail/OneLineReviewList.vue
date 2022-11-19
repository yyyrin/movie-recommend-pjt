<template>
  <div class="one-line-reveiw-list">
    {{ reviews }}
    <OneLineReviewItem
      v-for="review in reviews"
      :review="review"
      :key="review.id"
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
  props: {
    movie_id: Number
  },
  computed: {
    reviews() {
      // return this.$store.state.reviews
      // 영화 id와 일치하는 리뷰만 필터링 하는 방법 연구 중
      return this.$store.state.reviews.filter((review) => {
        return review.movie === this.movie_id;
      })
    }
  }
}
</script>

<style>

</style>