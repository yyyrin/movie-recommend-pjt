<template>
  <div>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#edit-community-modal" @click="getOriginalCommunity">
      수정
    </button>

    <!-- Modal -->
    <div class="modal fade" id="edit-community-modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">커뮤니티 수정</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>

          <div class="modal-body">
            <!-- 썸네일 -->
            <p>썸네일 수정 가능할 공간</p>
            <label for="community-thumbnail">썸네일 주소</label>
            <input type="text" id="community-thumbnail" v-model="thumbnail">
            <hr>
            <!-- <p>{{ community }}</p> -->
            <!-- 커뮤니티명 -->
            <label for="community-name" class="col-form-label">커뮤니티명</label>
            <input class="form-control" type="text" aria-label="default input example" id="community-name" v-model.trim="name">
          </div>

          <div class="modal-footer">
            <button class="btn btn-outline-danger waves-effect mb-4" @click="deleteCommunity">삭제</button>
            <!-- <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button> -->
            <button type="button" class="btn btn-primary" @click="putCommunity">저장</button>
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
        // console.log(res)
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
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
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