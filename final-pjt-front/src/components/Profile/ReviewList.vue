<template>
  <div class="review-list">
    <h1>Review List</h1>
    <hr>
    <!-- {{ myInfo }} -->
      <div v-if="reviews" class="row row-cols-1 row-cols-md-5 g-3 center py-2">
        <ReviewItem
          v-for="review in reviews"
          :key="review.id"
          :review="review"
        />
      </div>
  </div>
</template>

<script>
import ReviewItem from '@/components/Profile/ReviewItem'

export default {
  name: 'ArticleList',
  props: {
    userInfo: Object,
  },
  components: {
    ReviewItem,
  },
  computed: {
    reviews() {
      return this.userInfo?.reviews
    }
  },
}
</script>

<style>

</style>