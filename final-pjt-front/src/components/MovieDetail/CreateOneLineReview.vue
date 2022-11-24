<template id="create-one-line-review">
  <div>
    <!-- Button trigger modal -->
    <button id="create-review" type="button" class="btn btn-primary m-3" data-bs-toggle="modal" data-bs-target="#create-review-modal">
      리뷰 등록
    </button>

    <!-- Modal -->
    <div class="modal fade right" id="create-review-modal" tabindex="-1" role="dialog" aria-labelledby="createModalLabel" aria-hidden="true" data-backdrop="false">
      <div class="modal-dialog">
        <!-- content -->
        <div class="modal-content">
          <!--Header-->
          <div class="modal-header p-2" style="background-color: #FF6800;">
            <p class="heading px-2" style="font-size:30px; center; color: white; padding-top: 16px;">
              한줄리뷰 작성
            </p>
            <button type="button" class="btn-close mx-2" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>

          <!-- Body -->
          <div class="modal-body">
            <div class="row">
              <p style="font-size:25px;">{{ movie?.title }}</p>
              <div style="text-align: center;">
                <img :src="movieURL" alt="movie_poster" style="width: 180px;">
              </div>

              <!-- 별점 -->
              <!-- <label for="text">별점 : </label>
              <input type="number" min="1" max="10" id="rate" v-model="rate"> -->
              <!-- <div class="inner">
                <div class="star-rating">
                  <div
                    class="star"
                    v-for="index in 5"
                    :key="index"
                    @click="check(index)"
                  >
                    <span v-if="index < score">
                      <img src="@/assets/full1.png" alt="">
                    </span>
                    <span v-if="index >= score">
                      <img src="@/assets/empty.png" alt="">
                    </span>
                  </div>
                </div>
              </div> -->
              <!-- 별점 함수 끝-->
              
              <div class="mb-3">
                <label for="message-text" class="col-form-label align-self-start" style="text-align: left;">나의 한줄리뷰</label>
                <textarea class="form-control" id="message-text" v-model.trim="content" style="resize: none;"></textarea>
              </div>
            </div>
          </div>

          <!-- Footer -->
          <div class="modal-footer justify-content-center">
            <!-- <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button> -->
            <button type="button" class="btn btn-primary reveiw-save-button" style="color:white;" @click="createReview">등록</button>
          </div>
        </div>
        <!--/.Content-->
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
      // score: 0,
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    createReview() {
      console.log(this.movie)
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
          // 현재 경로에서 새로고침할 때 아래 코드 사용!
          this.$router.go(this.$router.currentRoute)
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    // check(index) {
    //   this.score = index + 1;
    // }
  },
  computed: {
    movieURL() {
      const posterPath = this.movie?.poster_path
      // null값 check
      if (!posterPath && typeof posterPath === 'object') {
        return '@/assets/basic_profile.png'
      } else {
        return `https://image.tmdb.org/t/p/w500/${posterPath}` 
      }
    }
  },

}
</script>

<style>
.modal {
  color: black;
}
#create-review {
  position: fixed;
  bottom: 15px;
}
#create-review {
  background-color: #FF6800;
  border-color: black;
}
.reveiw-save-button {
  background-color: #FF6800;
  border-color: #FF6800;
  color: white;
}
</style>