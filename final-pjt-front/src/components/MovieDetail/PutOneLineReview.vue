<template id="put-one-line-review">
  <div>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#put-one-line-review-modal">
      수정
    </button>

    <!-- Modal -->
    <div class="modal fade" id="put-one-line-review-modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>제목, 포스터 넣을 공간</p>
            <!-- <p>제목 : {{ movie?.title }}</p>
            <p>포스터 : {{ movie?.poster_path }}</p> -->
            <p>별점 넣을 공간</p>
            <label for="text">별점 : </label>
            <input type="number" min="1" max="10" id="rate" v-model="rate">
            <div class="mb-3">
              <label for="message-text" class="col-form-label">한줄리뷰</label>
              <textarea class="form-control" id="message-text" v-model.trim="content"></textarea>
            </div>
          </div>
          <div class="modal-footer">
            <!-- <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button> -->
            <button type="button" class="btn btn-primary" @click="fetchReview">등록</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'PutOneLineReview',
  props: {
    review: Object,
  },
  data() {
    return {
      rate: null,
      content: null,
    }
  },
  methods: {
    fetchReview() {
      const rate = this.rate
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      const badwords = this.$store.state.bad
      let flag = 1 
      badwords.forEach(word=>{
        if (content.indexOf(`${word}`) > -1 ){
          alert('바르고 고운말!')
          flag = 0
          return
        }
      })
      if (flag === 1){
        axios({
          method: 'put',
          url: `${API_URL}/api/v1/movies/${this.$route.params.id}/reviews/${this.review.id}/`,
          data: {
            rate: rate,
            content: content,
            },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
          this.$router.go(this.$router.currentRoute)
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    getOriginalReview() {
      this.rate = this.review.rate
      // console.log(this.rate)
      this.content = this.review.content
    }
  },
  created() {
    this.getOriginalReview()
    // console.log('created!')
  }
}
</script>

<style>
#put-one-line-review {
  color: black;
}
</style>