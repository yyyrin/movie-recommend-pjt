<template>
  <div>
    <!-- Button trigger modal -->
    <div>
      <button type="button" class="create-community-btn btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#create-community-modal">
        생성
      </button>
    </div>

    <!-- Modal -->
    <div class="modal fade right" id="create-community-modal" tabindex="-1" role="dialog" aria-labelledby="createModalLabel" aria-hidden="true" data-backdrop="false">
      <div class="modal-dialog">
        <!-- content -->
        <div class="modal-content">
          <!--Header-->
          <div class="modal-header p-2">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>

          <!-- Body -->
          <div class="modal-body d-flex flex-column mb-3">
            <!-- 커뮤니티명 -->
            <div class="mb-3">
              <label for="name" class="col-form-label d-flex justify-content-start">커뮤니티명</label>
              <input type="text" class="form-control" style="width:466px;" id="name" placeholder="커뮤니티명을 입력해주세요" v-model.trim="name">
            </div>
            <!-- 썸네일 -->
            <div class="mb-3">
              <label for="community-thumbnail" class="col-form-label d-flex justify-content-start">썸네일</label>
              <input type="text" class="form-control" style="width:466px;" id="community-thumbnail" placeholder="이미지 주소를 입력해주세요" v-model.trim="thumbnail">
            </div>
          </div>

          <!-- Footer -->
          <div class="modal-footer justify-content-center">
            <button type="button" class="btn btn-warning" style="color:white;" @click="createCommunity">생성</button>
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
  name: 'CreateCommunity',
  data() {
    return {
      name: null,
      thumbnail: null,
    }
  },
  methods: {
    createCommunity() {
      const name = this.name
      const thumbnail = this.thumbnail
      if (!name) {
        alert('커뮤니티명을 입력해주세요')
        return
      } else if (!thumbnail) {
        alert('썸네일을 넣어주세요')
        return
      }
      const badwords = this.$store.state.bad
      let flag = 1 
      badwords.forEach(word=>{
        if (name.indexOf(`${word}`) > -1 ){
          alert('바르고 고운말!')
          flag = 0
          return
        }
      })
      if (flag === 1){
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/community/`,
          data: {
            name: name,
            thumbnail: thumbnail,
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
    }
  }
}
</script>

<style>
.create-community-btn {
  background-color: #FF6800;
  border-color: #FF6800;
  color: white;
}
</style>