<template>
  <div>
    <!-- <p>{{ review }}</p> -->
    <p>별점 : {{ review.rate }}</p>
    <p>한줄 리뷰 : {{ review.content }}</p>
    <!-- <p>좋아요한 사람들 수: {{ like_count }}</p> -->
    
    <div style="float: right; margin-top:15px;">
      <button class=" btn btn-outline-danger waves-effect mb-4" @click="likeReview">
        좋아요 ♥ {{ count }}
      </button>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'OneLineReviewItem',
  data() {
    return {
      count: this.review.like_user?.length
    }
  },
  props: {
    review: Object,
  },
  // computed: {
  //   like_count() {
  //     return this.review.like_user?.length
  //   }
  // },
  methods: {
    // likeReview() {
    //   const movie_id = this.$route.params.id
    //   const review_id = this.review.id
      // const payload = [Number(movie_id), Number(review_id)]


      // this.$store.dispatch('likeReview', payload)

      // this.count += 1
      // this.$router.go(this.$router.currentRoute)
    // }
    likeReview() {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/reviews/${this.review.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        if (res.data === 1) {
          this.count += 1
        } else if (res.data === 0) {
          this.count -= 1
        }
        this.$router.go(this.$router.currentRoute)
      })
    },
  }
}
</script>

<style>

</style>