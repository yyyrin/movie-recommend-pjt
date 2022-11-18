<template>
  <div>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      리뷰 등록
    </button>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <!-- <h1 class="modal-title fs-5" id="exampleModalLabel">한줄리뷰</h1> -->
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>제목, 포스터 넣을 공간</p>
            <!-- <p>제목 : {{ movie?.title }}</p>
            <p>포스터 : {{ movie?.poster_path }}</p> -->
            <p>별점 넣을 공간</p>
            <label for="text">별점 : </label>
            <input type="text" id="rate" v-model="rate">
            <div class="mb-3">
              <label for="message-text" class="col-form-label">한줄리뷰</label>
              <textarea class="form-control" id="message-text" v-model.trim="content"></textarea>
            </div>
          </div>
          <div class="modal-footer">
            <!-- <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button> -->
            <button type="button" class="btn btn-primary" @click="createReview">등록</button>
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
  name: 'CreateOneLineReview',
  data() {
    return {
      rate: null,
      content: null,
    }
  },
  methods: {
    createReview() {
      const rate = this.rate
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/reviews/`,
        data: {
          rate: rate,
          content: content,
          },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // console.log(res)
        this.$router.push({ name: 'movie_detail' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>