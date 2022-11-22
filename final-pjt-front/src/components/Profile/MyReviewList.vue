<template>
  <div class="my-review-list">
    <h1>My Review List</h1>
    <hr>
    <!-- {{ myInfo }} -->
    <ol class="list-group list-group-numbered">
      <MyReviewItem
        v-for="review in reviews"
        :key="review.id"
        :review="review"
      />
    </ol>
  </div>
</template>

<script>
import MyReviewItem from '@/components/Profile/MyReviewItem'

export default {
  name: 'MyArticleList',
  props: {
    myInfo: Object,
  },
  components: {
    MyReviewItem,
  },
  computed: {
    reviews() {
      return this.myInfo?.reviews
    }
  },
}
</script>

<style>

</style>