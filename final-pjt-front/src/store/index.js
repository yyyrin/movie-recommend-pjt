import router from '@/router'
import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  // 토큰관리 -> Local에 저장 -> 나중에 변경하기
  plugins: [
    createPersistedState()
  ],
  state: {
    token: null,
    username: null,
    pk: null,
    imgpath: null,
    movies: [],
    // reviews: [],
    communities: [],
    articles: [],
    comments: [],
    bad: ['애플', 'apple', 'APPLE', '사과', '멍청이', '바보', '리중딱'],
    genres: ['애니메이션', '드라마', '스릴러', '모험', '판타지', '공포', '액션', '코미디', '역사', '서부', '범죄', '다큐멘터리', 'SF', '미스터리', '음악', '로맨스', '가족', '전쟁', 'TV 영화']
  },
  getters: {
    isLogIn(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    // 회원가입 && 로그인
    SAVE_TOKEN(state, data) {
      state.username = data.username
      state.token = data.token
      router.push({ name: 'home' })
    },
    GET_MOVIES(state, movies) {
      state.movies = movies
      // console.log(state.movies)
    },
    // GET_REVIEWS(state, reviews) {
    //   state.reviews = reviews
    // },
    GET_COMMUNITIES(state, communities) {
      state.communities = communities
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    GET_COMMENTS(state, comments) {
      state.comments = comments
    },
    GET_IMG_PATH(state, userdata) {
      console.log(userdata)
      state.imgpath = userdata[0]
      state.pk = userdata[1]
    }
  },
  actions: {
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
      .then((res) => {
        // console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(err => console.log(err))
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
      .then((res) => {
        const data = { token: res.data.key, username: payload.username }
        context.commit('SAVE_TOKEN', data)
      })
      .catch(() => {
        alert('일치하지 않는 회원 정보입니다.')
      })
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${payload.username}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((res) => {
        context.commit('GET_IMG_PATH', [res.data.user.img_path, res.data.user.id])
        // console.log(this.myInfo.reviews)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
        // console.log(context)
        context.commit('GET_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // getReviews(context) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/reviews/`,
    //     headers: {
    //       Authorization: `Token ${context.state.token}`
    //     }
    //   })
    //   .then((res) => {
    //     // console.log(res)
    //     // console.log(res.data)
    //     context.commit('GET_REVIEWS', res.data)
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // },
    // likeReview(context, payload) {
    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/api/v1/movies/${payload[0]}/reviews/${payload[1]}/like/`,
    //     headers: {
    //       Authorization: `Token ${context.state.token}`
    //     }
    //   })
    // },
    getCommunities(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((res) => {
        context.commit('GET_COMMUNITIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getArticles(context, community_id) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${community_id}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((res) => {
        // console.log(res.data.article_set)
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 여기 막힘!!! 
    getComments(context, payload) {
      // console.log(payload[0])
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${payload[0]}/article/${payload[1]}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((res) => {
        // console.log(res)
        context.commit('GET_COMMENTS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})