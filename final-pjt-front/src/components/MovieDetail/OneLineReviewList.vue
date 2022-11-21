<template>
  <div class="one-line-reveiw-list">
    <OneLineReviewItem
      v-for="review in reviews"
      :review="review"
      :key="review.id"
    />
  </div>
</template>

<script>
import OneLineReviewItem from '@/components/MovieDetail/OneLineReviewItem'

export default {
  name: 'OneLineReviewList',
  components: {
    OneLineReviewItem,
  },
  props: {
    movie_id: Number,
    reviews: Array
  },
  computed: {
    getreviews() {
      // 영화 id와 일치하는 리뷰만 필터링 하는 방법 연구 중
      // console.log(this.reviews)
      return this.reviews.filter((review) => {
        return review.movie.id === this.movie_id;
      })
    }
  }
}
</script>

<style>

</style>