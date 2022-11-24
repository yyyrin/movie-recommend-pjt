<template>
  <div id="create-community-article-view">
    <nav-bar></nav-bar>

    <div id="create-community-article-body" class="my-3">
      <form @submit.prevent="createArticle">
        <!-- title -->
        <div class="row mt-2" style="display:block;">
          <div class="FlexableTextArea" style="font-size-adjust:none; font-weight:400;">
            <textarea placeholder="제목을 입력해 주세요." style="height:40px;"></textarea>
          </div>
        </div>
        <!-- img -->
        <div class="row mt-2" style="display:block;">
          <div class="FlexableTextArea" style="font-size-adjust:none; font-weight:400;">
            <textarea placeholder="제목을 입력해 주세요." style="height:40px;"></textarea>
          </div>
        </div>
        <!-- content -->
        
        <label for="title">제목 : </label>
        <input type="text" id="title" v-model.trim="title"><br>
        <label for="content">내용 : </label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
        <label for="imagepath">이미지 : </label>
        <textarea id="imagepath" cols="30" rows="10" v-model="imagepath"></textarea><br>
        <input type="submit" id="submit">
      </form>
    </div>
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
        if (title.indexOf(`${word}`) > -1 || content.indexOf(`${word}`)>-1){
          alert('바르고 고운말!')
          flag = 0
          console.log(flag)
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
#create-community-article-view {
  padding-top: 90px;
  color: white;
}
#create-community-article-body {
  width: 900px;
  margin: 0 auto;
  display: block;
  background-color: rgb(27, 27, 27);
  /* border: white; */
  border-radius: 2%;
}

</style>