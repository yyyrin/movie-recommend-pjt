<template>
  <nav class="navbar fixed-top navbar-dark navbar-expand-lg" style="background-color: #000000;">
    <div class="container-fluid">
      <!-- 로고 - 홈 연결 -->
      <router-link class="nav-link active" :to="{ name: 'home' }">
        <img src="@/assets/LOGO.png" alt="logo" height="50">
      </router-link>
      <!-- toggler -->
      <div class="navbar-dark bg-dark">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <!-- 장르 -->
          <!-- <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'genre' }">장르</router-link>
          </li> -->
          <!-- 영화 -->
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'home' }">영화</router-link>
          </li>
          <!-- 커뮤니티 -->
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'community' }">커뮤니티</router-link>
          </li>
          <!-- 검색 -->
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'search' }">검색</router-link>
          </li>
        </ul>

        <ul class="navbar-nav mb-2 mb-lg-0"> 
          <!-- 검색 버튼
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'search' }">
              <img src="@/assets/search_button.png" alt="search_button" height="30">
            </router-link>
          </li> -->

          <!-- 프로필 dropdown -->
          <li class="nav-item dropdown">     
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <img :src="imgpath" height="30">
            </a>
            <ul class="dropdown-menu dropdown-menu-dark dropdown-menu-lg-end">
              <!-- MY 프로필 이동 -->
              <li class="dropdown-item">
                <router-link class="nav-link" :to="{ name: 'profile', params: { username: $store.state.username } }">MY</router-link>
              </li>
              <!-- 로그아웃 -->
              <li class="dropdown-item">
                <router-link class="nav-link" :to="{ name: 'login' }">로그아웃</router-link>
              </li>
              <!-- 회원가입 -->
              <li class="dropdown-item">
                <router-link class="nav-link" :to="{ name: 'signup' }">회원가입</router-link>
              </li>
            </ul>
          </li>
        </ul>

      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  computed: {
    imgpath() {
      return this.$store.state.imgpath
    }
  },
}
</script>

<style>
/* .navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
} */
</style>