<template>
  <div>
    <p>{{ review }}</p>
    <p>별점 : {{ review.rate }}</p>
    <p>한줄 리뷰 : {{ review.content }}</p>
    <!-- <p>좋아요한 사람들 수: {{ like_count }}</p> -->

    <!-- 수정 -->
    <PutOneLineReview
      :review="review"
    />

    <!-- 삭제 -->
    <button class="btn btn-outline-danger waves-effect mb-4" @click="deleteReview">삭제</button>

    <!-- 좋아요 기능 -->
    <div style="float: right; margin-top:15px;">
      <button class=" btn btn-outline-danger waves-effect mb-4" @click="likeReview">
        좋아요 ♥ {{ count }}
      </button>
    </div>
    <br><br>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import PutOneLineReview from '@/components/MovieDetail/PutOneLineReview'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'OneLineReviewItem',
  data() {
    return {
      count: this.review.like_user?.length
    }
  },
  components: {
    PutOneLineReview
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
    deleteReview() {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/reviews/${this.review.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        alert('삭제가 완료되었습니다.')
        this.$router.go(this.$router.currentRoute)
      })
      .catch((err) => {
        console.log(err)
      })
    },
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