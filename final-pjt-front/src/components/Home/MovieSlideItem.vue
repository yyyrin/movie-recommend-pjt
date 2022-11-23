<template>
  <div>
    <div>하이</div>
    <!-- <router-link :to="{ name: 'movie_detail', params: { id: movie.id } }">
      <p><img :src="movieURL" alt="movie_poster"></p>
    </router-link> -->
  </div>
</template>

<script>

export default {
  name: 'MovieSlideItem',
  // props: {
  //   movie: Object,
  // },
  // computed: {
  //   movieURL() {
  //     const posterPath = this.movie?.poster_path
  //     // null값 check
  //     if (!posterPath && typeof posterPath === 'object') {
  //       return '@/assets/basic_profile.png'
  //     } else {
  //       return `https://image.tmdb.org/t/p/w500/${posterPath}`  // 여기서 get 오류가 나는데..?
  //     }
  //   }
  // }
}
</script>

<style>

</style>