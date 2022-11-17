<template>
  <div>
    <nav class="navbar navbar-expand-lg" style="background-color: #000000;">
  <div class="container-fluid">
    <!-- <router-link class="nav-link" :to={ name: 'home' }></router-link> -->
    <a class="navbar-brand" href="#">
      <img src="@/assets/LOGO.png" alt="logo" height="35">
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto justify-content-start">
        <!-- 장르 -->
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'genre' }">장르</router-link>
        </li>
        <!-- 커뮤니티 -->
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'community' }">커뮤니티</router-link>
        </li>
      </ul>

      <!-- 여기부터 수정수정!!!
      <ul class="nav-nav me-auto justify-content-end"> -->
        <!-- 검색 버튼 -->
        <!-- <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'search' }">
            <img src="@/assets/search_button.png" alt="search_button" height="30">
          </router-link>
        </li> -->

        <!-- 프로필 dropdown -->
        <!-- <li class="nav-item dropdown">     
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <img src="@/assets/basic_profile.png" alt="basic_profile" height="30">
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">MY</a></li>
            <li><a class="dropdown-item" href="#">로그아웃</a></li>
          </ul>
        </li>
        
      </ul> -->
      


    </div>
  </div>
</nav>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
}
</script>

<style>

</style>