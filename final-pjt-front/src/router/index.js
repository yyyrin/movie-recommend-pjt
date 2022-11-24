import Vue from 'vue'
import VueRouter from 'vue-router'

import LogInView from '@/views/LogInView'
import SignUpView from '@/views/SignUpView'
import HomeView from '@/views/HomeView'
import MovieDetailView from '@/views/MovieDetailView'
import GenreView from '@/views/GenreView'
import CommunityView from '@/views/CommunityView'
import CommunityArticleView from '@/views/CommunityArticleView'
import CreateCommunityArticleView from '@/views/CreateCommunityArticleView'
import CommunityArticleDetail from '@/views/CommunityArticleDetail'
import SearchView from '@/views/SearchView'
import ProfileView from '@/views/ProfileView'
// import MyArticleList from '@/components/Profile/MyArticleList'
// import YourProfileView from '@/views/YourProfileView'

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

  // 홈
  {
    path: '/home',
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
    path: '/community/:community_id',
    name: 'community_article',
    component: CommunityArticleView,
  },
  {
    path: '/community/:community_id/article/create',
    name: 'create_community_article',
    component: CreateCommunityArticleView,
  },
  {
    path: '/community/:community_id/article/:article_id',
    name: 'community_article_detail',
    component: CommunityArticleDetail,
  },

  // 검색
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },

  // 프로필
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  // 타인 프로필
  // {
  //   path: '/profile',
  //   name: 'profile',
  //   component: YourProfileView
  // },
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
