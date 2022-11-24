<template>
  <div>
    <OneLineReviewList
      :movie_id="movie_id"
      :reviews="reviews"
    />
    <CreateOneLineReview
      :movie="movie"
    />
  </div>
</template>

<script>
import OneLineReviewList from '@/components/MovieDetail/OneLineReviewList'
import CreateOneLineReview from '@/components/MovieDetail/CreateOneLineReview'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'OneLineReviewView',
  props: {
    movie_id: Number,
    movie: Object,
  },
  data() {
    return {
      reviews: null,
    }
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
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/`,
      })
      .then((res) => {
        this.reviews = res.data.review_set
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>