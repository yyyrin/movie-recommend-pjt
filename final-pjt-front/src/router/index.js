import Vue from 'vue'
import VueRouter from 'vue-router'

import LogInView from '@/views/LogInView'
import SignUpView from '@/views/SignUpView'
import HomeView from '@/views/HomeView'
import MovieDetailView from '@/views/MovieDetailView'
import GenreView from '@/views/GenreView'
import CommunityView from '@/views/CommunityView'
import CommunityArticleView from '@/views/CommunityArticleView'
import SearchView from '@/views/SearchView'
import ProfileView from '@/views/ProfileView'

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

  // 영화 detail
  {
    path: '/detail/:id',
    name: 'movie_detail',
    component: MovieDetailView,
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
  {
    path: '/community/:name',
    name: 'community_article',
    component: CommunityArticleView,
  },

  // 검색
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },

  // 프로필
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// const originalPush = VueRouter.prototype.push;
// VueRouter.prototype.push = function push(location) {
// 	return originalPush.call(this, location).catch(err => {
// 		if (err.name !== 'NavigationDuplicated') throw err;
// 	});
// };

export default router
