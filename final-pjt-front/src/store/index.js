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
    movies: [],
  },
  getters: {
    isLogIn(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'home' })
    },
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
  },
  actions: {
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
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
        // console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(err => console.log(err))
    },
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((res) => {
        context.commit('GET_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})


// import Vue from 'vue'
// import Vuex from 'vuex'

// import accounts from '@/store/modules/accounts'

// Vue.use(Vuex)

// export default new Vuex.Store({
//   modules: {
//     accounts,
//   }
// })
