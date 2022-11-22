<template>
  <div class="review-list">
    <h1>Review List</h1>
    <hr>
    <!-- {{ myInfo }} -->
    <ol class="list-group list-group-numbered">
      <ReviewItem
        v-for="review in reviews"
        :key="review.id"
        :review="review"
      />
    </ol>
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