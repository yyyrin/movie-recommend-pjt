<template>
  <div id="one-line-review-item">
    <div class="bubble sb14">
      <div class="d-flex">
        <div class="m-2">
          <!-- 프로필 사진 & username -->
          <div class="profile-box" style="background: white;">
            <router-link  :to="{ name: 'profile', params: { username: review?.user.username } }">
              <img class="profile" style="height:50px; width: 50px;" :src=review?.user.img_path @error="replacing">
              <p style="text-align:center;">{{ review?.user.username }}</p>
            </router-link><br>
          </div>
        </div>
          <!-- <div style="text-align:center">
            <router-link :to="{ name: 'profile', params: { username: review?.user.username } }">{{ review?.user.username }}</router-link>
          </div> -->
        <!-- 별점 & 리뷰 -->
        <div class="mx-2">
          <span>{{ review.rate }}</span>
          <p style="font-size:25px;">{{ review.content }}</p>
        </div>
        <!-- 수정, 삭제, 좋아요 -->
        <div class="ms-auto mx-3 my-1">
          <div class="btn-group dropend d-flex flex-column mb-5" style="text-align:center;">
            <button type="button" class="btn btn-link dropdown-toggle btn-sm" data-bs-toggle="dropdown" aria-expanded="false">
              EDIT
            </button>
            <ul class="dropdown-menu dropdown-menu-dark">
              <li><PutOneLineReview :review="review"/></li>
              <li><a class="dropdown-item" @click="deleteReview">삭제</a></li>
            </ul>
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
        if (res.data.result === 1) {
          this.count += 1
        } else if (res.data.result === 0) {
          this.count -= 1
        }
        // this.$router.go(this.$router.currentRoute)
      })
    },
  }
}
</script>

<style>
.bubble {
  width: 600px;
  margin: 50px auto;
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