<template>
  <div>
    <hr>
    <OneLineReviewList
      :movie_id="movie_id"
    />
    <!-- <p>{{ movieId }}</p> -->
  </div>
</template>

<script>
import OneLineReviewList from '@/components/MovieDetail/OneLineReviewList'

export default {
  name: 'OneLineReviewView',
  props: {
    movie_id: Number,
  },
  components: {
    OneLineReviewList
  },
  created() {
    this.getReviews()
  },
  methods: {
    getReviews() {
      this.$store.dispatch('getReviews')  // this.movieId
    }
  }
}
</script>

<style>

</style>