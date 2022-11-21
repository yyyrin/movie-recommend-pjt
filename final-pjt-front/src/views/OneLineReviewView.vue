<template>
  <div>
    <hr>
    <OneLineReviewList
      :movie_id="movie_id"
    />
    <CreateOneLineReview/>
  </div>
</template>

<script>
import OneLineReviewList from '@/components/MovieDetail/OneLineReviewList'
import CreateOneLineReview from '@/components/MovieDetail/CreateOneLineReview'

export default {
  name: 'OneLineReviewView',
  props: {
    movie_id: Number,
  },
  components: {
    OneLineReviewList,
    CreateOneLineReview,
  },
  created() {
    this.getReviews()
  },
  methods: {
    getReviews() {
      this.$store.dispatch('getReviews')
    }
  }
}
</script>

<style>

</style>