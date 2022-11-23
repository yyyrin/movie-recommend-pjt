<template>
  <div>
    <!-- Button trigger modal -->
    <button v-show="is_active1" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#edit-profile-modal">
      회원정보 수정
    </button>

    <!-- Modal -->
    <div class="modal fade" id="edit-profile-modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <!-- <h1 class="modal-title fs-5" id="exampleModalLabel">한줄리뷰</h1> -->
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <!-- <p>{{ userInfo }}</p> -->
            <p>사용자 프로필 사진 넣을 자리</p>
            <!-- <p>{{ userInfo?.user.img_path }}</p> -->
            <label for="text">새로운 이미지 경로 : </label>
            <input type="text" id="img_path" v-model.trim="img_path">
            <!-- <p>username: {{ userInfo?.user.username }}</p> -->
          </div>
          <div>
            <p>미리보기</p>
            <img :src="img_path" alt="img_path" height="100">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="editProfile">저장</button>
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
  name: 'EditProfile',
  props: {
    userInfo: Object,
    is_active1: Number
  },
  data() {
    return {
      img_path: null,
    }
  },
  methods: {
    editProfile() {
      // const img_path = this.user.img_path
      // console.log(this.img_path)

      let img_path = this.img_path
      if (!img_path) {
        img_path = 123
      }
      axios({
        method: 'put',
        url: `${API_URL}/accounts/profile/${this.userInfo.user.id}/img/`,
        data: {
          // img_path: img_path,
          img_path: img_path,
          },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        alert('회원정보 수정 완료')
        this.$store.commit('GET_IMG_PATH', img_path)
        this.$router.go(this.$router.currentRoute)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getOriginalProfile() {
      // this.img_path = this.user.img_path
      this.img_path = this.userInfo?.user.img_path
      console.log(this.img_path)
    },
  },
  created() {
  this.getOriginalProfile()
  console.log(this.img_path)
  }
}
</script>

<style>

</style>