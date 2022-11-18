<template>
  <div>
    <h1>OneLineReviewView</h1>
    <hr>
    <OneLineReviewList/>
  </div>
</template>

<script>
import OneLineReviewList from '@/components/MovieDetail/OneLineReviewList'

export default {
  name: 'OneLineReviewView',
  components: {
    OneLineReviewList
  },
  // 작성 중
  // created() {
  //   this.getReviews()
  // },
  // methods: {
  //   getReviews() {
  //     this.$store.dispatch('getReviews')
  //   }
  // }
}
</script>

<style>

</style>