<template>
  <div id="one-line-review-item">
    <div class="bubble sb14">
      <div class="d-flex">
        <div class="m-2">
          <!-- 프로필 사진 & username -->
          <div class="profile-box" style="background: white;">
            <router-link  :to="{ name: 'profile', params: { username: review?.user.username } }">
              <img class="profile" style="height:50px; width: 50px;" :src=review?.user.img_path >
              <p style="text-align:center; color: white;">{{ review?.user.username }}</p>
            </router-link><br>
          </div>
            <router-link  :to="{ name: 'profile', params: { username: review?.user.username } }">
              <p style="text-align:center; color: white;">{{ review?.user.username }}</p>
            </router-link><br>
        </div>
          <!-- <div style="text-align:center">
            <router-link :to="{ name: 'profile', params: { username: review?.user.username } }">{{ review?.user.username }}</router-link>
          </div> -->
        <!-- 별점 & 리뷰 -->
        <div class="mx-2">
          <label for="text">별점 : </label>
                  <span
                    class="star"
                    v-for="index in 5"
                    :key="index"
                    @click="check(index)"
                  >
                    <span v-if="index < (review?.rate)/2-0.5">
                      <img src="@/assets/full2.png" alt="" height="30px;">
                    </span>
                    <span v-if="index >= (review?.rate)/2">
                      <img src="@/assets/empty2.png" alt="" height="30px;">
                    </span>
                    <span v-if="index == (review?.rate)/2-0.5">
                      <img src="@/assets/middle2.png" alt="" height="30px;">
                    </span>
                  </span>
          <p style="font-size:25px;">{{ review.content }}</p>
        </div>

        <!-- 수정, 삭제, 좋아요 -->
        <div class="ms-auto mx-3 my-1">
          <div class="btn-group dropend d-flex flex-column mb-5" style="text-align:center;">
            <button type="button" class="btn btn-link dropdown-toggle btn-sm" data-bs-toggle="dropdown" aria-expanded="false">
              EDIT
            </button>
            <ul class="dropdown-menu dropdown-menu-dark">
              <li>
                <a class="dropdown-item" data-bs-toggle="modal" data-bs-target="#put-one-line-review-modal">수정</a>
              </li>
              <li><a class="dropdown-item" @click="deleteReview">삭제</a></li>
            </ul>
          </div>

          <!-- 수정 Modal -->
          <div class="modal fade right" id="put-one-line-review-modal" tabindex="-1" aria-labelledby="putModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <!-- content -->
              <div class="modal-content">
                <!-- header -->
                <div class="modal-header p-2">
                  <p class="heading px-2" style="font-size:30px; center; color: white; padding-top: 16px;">
                    한줄리뷰 수정
                  </p>
                  <button type="button" class="btn-close mx-2" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <!-- Body -->
                <div class="modal-body">
                  <div class="row">
                    <p style="font-size:25px;">{{ movie?.title }}</p>
                    <!-- <div style="text-align: center;">
                      <img :src="movieURL" alt="movie_poster" style="width: 180px;">
                    </div> -->
                    <!-- 별점 -->
                    <div class="my-3">
                      <!-- <label for="text">별점 : </label> -->
                      <input class="d-none" type="number" min="1" max="10" id="rate" v-model="rate">
                      <div class="inner">
                        <div class="star-rating">
                          <span
                            class="star"
                            v-for="index in 5"
                            :key="index"
                            @click="check(index)"
                          >
                            <span v-if="index < score-0.5">
                              <img src="@/assets/full1.png" alt="" height="30px;">
                            </span>
                            <span v-if="index >= score">
                              <img src="@/assets/empty1.png" alt="" height="30px;">
                            </span>
                            <span v-if="index == score-0.5">
                              <img src="@/assets/middle1.png" alt="" height="30px;">
                            </span>
                          </span>
                        </div>
                      </div>
                    </div>
                    <!-- 요기까지 별점 -->

                    <div class="mb-3">
                      <label for="message-text" class="col-form-label align-self-start" style="text-align: left;">나의 한줄리뷰</label>
                      <textarea class="form-control" id="message-text" v-model.trim="content" style="resize: none;"></textarea>
                    </div>
                  </div>
                </div>
                <!-- footer -->
                <div class="modal-footer justify-content-center">
                  <button type="button" class="btn btn-warning" style="color:white;" @click="fetchReview">등록</button>
                </div>
              </div>
            </div>
          </div>

          <div style="float: right text-align:center;">
            <button class=" btn btn-danger waves-effect btn-sm m-1" :count = count @click="likeReview">
              ♥ {{ count }}
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- <p>좋아요한 사람들 수: {{ like_count }}</p> -->
    <br><br>

  </div>
</template>

<script>
import axios from 'axios'
// import PutOneLineReview from '@/components/MovieDetail/PutOneLineReview'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'OneLineReviewItem',
  data() {
    return {
      count: this.review.like_user?.length,
      rate: null,
      content: null,
      score: 0,
    }
  },
  // components: {
  //   PutOneLineReview
  // },
  props: {
    movie: Object,
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
    check(index) {
      if (this.score == index+1) {
        this.score = index + 0.5
      } else if (this.score == index - 0.5) {
        this.score = index + 0.5
      } else {
      this.score = index+1;
      }
      this.rate = (this.score-1)*2
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
        if (res.data.result === 1) {
          this.count += 1
        } else if (res.data.result === 0) {
          this.count -= 1
        }
        // this.$router.go(this.$router.currentRoute)
      })
    },
    getOriginalReview() {
      this.rate = this.review.rate
      // console.log(this.rate)
      this.content = this.review.content
      // this.rate = (this.score-1)*2
      // 값이 제대로 안 나옴.. 뭐지
      this.score = parseInt(this.review.rate / 2) + 1
    },
  },
  created() {
    this.getOriginalReview()
    // console.log('created!')
  },
}
</script>

<style>
#one-line-review-item {
  height: 140px;
}

.bubble {
  width: 600px;
  margin-left: 20px;
  margin-top: 30px;
  margin-bottom: 30px;
  border-radius: 15px;
  background: #FF6800;
  color: black;
  padding: 10px;
  text-align: left;
  color: white;
  font-weight: 900;
  position: relative;
}
.sb14:before {
  content: "";
  width: 0px;
  height: 0px;
  position: absolute;
  border-left: 15px solid transparent;
  border-right: 15px solid #FF6800;
  border-top: 15px solid #FF6800;
  border-bottom: 15px solid transparent;
  left: -16px;
  top: 0px;
}
.profile-box {
  width: 50px;
  height: 50px;
  border-radius: 70%;
  overflow: hidden;
}
.profile-img {
  object-fit: cover;
}
</style>