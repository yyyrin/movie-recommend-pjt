import Vue from 'vue'
import VueRouter from 'vue-router'

import LogInView from '@/views/LogInView'
import SignUpView from '@/views/SignUpView'
import HomeView from '@/views/HomeView'
import GenreView from '@/views/GenreView'
import CommunityView from '@/views/CommunityView'
import SearchView from '@/views/SearchView'

Vue.use(VueRouter)

const routes = [
  // Login
  {
    path: '/login',
    name: 'login',
    component: LogInView
  },

  // Signup
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },

  // 홈 및 기초화면
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  // 장르
  {
    path: '/genre',
    name: 'genre',
    component: GenreView
  },

  // Community
  {
    path: '/community',
    name: 'community',
    component: CommunityView,
  },

  // 검색
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
