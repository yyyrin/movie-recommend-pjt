<template>
  <div id="home">
    <nav-bar></nav-bar>
    <MovieSlide/>

    <!-- 1. 추천영화 -->
    <section>
      <div id="recommend-cards" style="background-color: rgb(27, 27, 27)">
        <div class="title d-flex justify-content-between mx-5">
          <h1 tabindex="0" class="title-area">
            <span class="label">추천 영화</span>
          </h1>
        </div>
        <MovieCards/>
      </div>
    </section>

    <!-- 2. 장르별 추천 영화 -->
    <section v-for="(genre, index) in genres" :key="index">
      <div id="recommend-cards" style="background-color: rgb(27, 27, 27)">
        <div class="title d-flex justify-content-between mx-5">
          <h1 tabindex="0" class="title-area">
            <span class="label">{{ genre }} 추천 영화</span>
          </h1>
          <router-link :to="{ name: 'search', params: {keyword: `${genre}`} }">더보기 ></router-link>
        </div>
        <MovieGenreCards
          :genre="genre"
        />
      </div>
    </section>

  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import MovieSlide from '@/components/Home/MovieSlide'
import MovieCards from '@/components/Home/MovieCards'
import MovieGenreCards from '@/components/Home/MovieGenreCards'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'HomeView',
  components: {
    NavBar,
    MovieSlide,
    MovieCards,
    MovieGenreCards,
  },
  computed: {
    isLogIn() {
      return this.$store.getters.isLogIn
    },
    genres() {
      return this.$store.state.genres
    },
  },
  created() {
    this.usercheck()
    this.check()
    this.getMovies()
  },
  methods: {
    usercheck() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${this.$store.state.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.$store.commit('GET_IMG_PATH', [res.data.user.img_path, res.data.user.id])
      })
      .catch((err) => {
        console.log(err)
      })
    },
    check() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/check/`,
        headers: {Authorization: `Token ${this.$store.state.token}`}
      })
        .then((res) => {
          if (res.data.result === 1) {
            this.$router.push('genre')
          }
        })
        .catch(()=> {})

    },
    getMovies() {
      if (this.isLogIn) {
        this.$store.dispatch('getMovies')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'login' })
      }
    }
  }
}
</script>

<style>
#home {
  background-image: url("../assets/lionking.png");
  /* background-color: black; */
  color: white;
}

#recommend-cards {
  margin: 30px 180px 30px 180px;
  padding: 20px;
}

.title {
  padding-left: 50;
  padding-right: 50;
}
.label {
  font-size: 23px;
}
</style>