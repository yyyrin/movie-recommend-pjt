<template>
  <div>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#edit-profile-modal">
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
            <label for="text">pw : </label>
            <input type="text" id="password" v-model.trim="password">
            <!-- <p>username: {{ userInfo?.user.username }}</p> -->
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
  },
  data() {
    return {
      // img_path: null,
      password: null,
    }
  },
  methods: {
    editProfile() {
      // const img_path = this.user.img_path
      // console.log(this.password)

      const password = this.userInfo.user.password
      if (!password) {
        alert('비밀번호를 입력해주세요')
        return
      }
      axios({
        method: 'put',
        url: `${API_URL}/accounts/profile/${this.$route.params.username}/`,
        data: {
          // img_path: img_path,
          password: password,
          },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        alert('회원정보 수정 완료')
        this.$router.go(this.$router.currentRoute)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getOriginalProfile() {
      // this.img_path = this.user.img_path
      this.password = this.userInfo?.user.password
    },
  },
  created() {
  this.getOriginalProfile()
  }
}
</script>

<style>

</style>