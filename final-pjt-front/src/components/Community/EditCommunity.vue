<template>
  <div>
    <!-- Button trigger modal -->
    <div style="margin-right:5px;">
      <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#edit-community-modal" @click="getOriginalCommunity">
        :
      </button>
    </div>

    <!-- Modal -->
    <div class="modal fade right" id="edit-community-modal" tabindex="-1" role="dialog" aria-labelledby="editModalLabel" aria-hidden="true" data-backdrop="false">
      <div class="modal-dialog">
        <!-- content -->
        <div class="modal-content">
          <!--Header-->
          <div class="modal-header p-3">
            <h1 class="modal-title fs-5" id="exampleModalLabel">커뮤니티 수정</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>

          <!-- Body -->
          <div class="modal-body d-flex flex-column mb-3">
            <!-- 커뮤니티명 -->
            <div class="mb-3">
              <label style="font-size: 18px;" for="community-name" class="col-form-label d-flex justify-content-start">커뮤니티명</label>
              <input class="form-control" type="text" aria-label="default input example" id="community-name" style="width:466px;" placeholder="커뮤니티명을 입력해주세요" v-model.trim="name">
            </div>
            <!-- 썸네일 -->
            <div class="mb-3">
              <label style="font-size: 18px;" for="community-thumbnail" class="col-form-label d-flex justify-content-start">썸네일 주소</label>
              <input type="text" class="form-control" style="width:466px;" id="community-thumbnail" placeholder="이미지 주소를 입력해주세요" v-model="thumbnail">
            </div>
          </div>
    
          <!-- Footer -->
          <div class="modal-footer justify-content-between">
            <button class="btn btn-outline-danger waves-effect" @click="deleteCommunity">삭제</button>
            <!-- <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button> -->
            <button type="button" class="btn btn-warning" style="color:white;" @click="putCommunity">저장</button>
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
  name: 'EditCommunity',
  data() {
    return {
      thumbnail: null,
      name: null,
    }
  },
  props: {
    community: Object,
  },
  methods: {
    deleteCommunity() {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/community/${this.community.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        alert('삭제가 완료되었습니다.')
        this.$router.push({ name: 'community' })
        // 새로고침하지 않으면 창이 이상함..왜 이러지
        this.$router.go(this.$router.currentRoute)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    putCommunity() {
      const thumbnail = this.thumbnail
      const name = this.name
      if (!name) {
        alert('커뮤니티명을 입력해주세요')
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
          method: 'put',
          url: `${API_URL}/api/v1/community/${this.$route.params.id}/`,
          data: {
            thumbnail: thumbnail,
            name: name,
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    getOriginalCommunity() {
      this.thumbnail = this.community.thumbnail
      this.name = this.community.name
    }
  }
}
</script>

<style>

</style>