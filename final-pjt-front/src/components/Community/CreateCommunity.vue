<template>
  <div>
    <!-- Button trigger modal -->
    <button type="button" class="create-community-btn btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      새로 만들기
    </button>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="mb-3">
              <label for="name" class="col-form-label">커뮤니티명:</label>
              <input type="text" class="form-control" id="name" v-model.trim="name">
            </div>
            <div class="mb-3">
              <label for="community-thumbnail" class="col-form-label">썸네일:</label>
              <input type="text" class="form-control" id="community-thumbnail" v-model.trim="thumbnail">
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="createCommunity">생성</button>
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