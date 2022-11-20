<template>
  <div>
    <div class="input-group input-group-lg">
    <input type="text" class="form-control" placeholder="댓글을 입력해주세요." aria-label="create comment" aria-describedby="button-addon2" v-model="content">
    <button class="btn btn-outline-secondary" type="button" id="button-addon2" @click="createComment">등록</button>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateCommunityArticleComment',
  data() {
    return {
      content: null,
    }
  },
  props: {
    community_id: Number,
    article_id: Number,
  },
  methods: {
    createComment() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/community/${this.$route.params.community_id}/article/${this.$route.params.article_id}/comments/`,
        data: {
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // console.log(content)
        this.$router.go(this.$router.currentRoute)
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