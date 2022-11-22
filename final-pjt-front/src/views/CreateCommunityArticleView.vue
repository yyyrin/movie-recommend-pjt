<template>
  <div>
    <nav-bar></nav-bar>
    <h1>CreateCommunityArticleView</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <label for="imagepath">이미지 : </label>
      <textarea id="imagepath" cols="30" rows="10" v-model="imagepath"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateCommunityArticleView',
  components: {
    NavBar,
  },
  props: {
    community_id: Number,
  },
  data() {
    return {
      title: null,
      content: null,
      imagepath: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const imagepath = this.imagepath

      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      const badwords = this.$store.state.bad
      let flag = 1 
      badwords.forEach(word=>{
        if (title.indexOf(`${word}`) > -1 || content.indexOf(`${word}`)){
          alert('바르고 고운말!')
          flag = 0
          return
        }
      })
      if (flag === 1){
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/community/${this.$route.params.community_id}/article/`,
          data: {
            title: title,
            content: content,
            imagepath: imagepath,
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then(() => {
            // console.log(res)
            this.$router.push({ name: 'community_article' })
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

</style>