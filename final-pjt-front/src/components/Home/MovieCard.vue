<template>
  <div>
    <router-link :to="{ name: 'movie_detail', params: { id: movie.id } }">
      <div class="col">
        <div class="card h-100">
          <img :src="movieURL" class="card-img-top" alt="...">
          <!-- 마우스 오버시 title 보이게 할 계획
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
          </div> -->
        </div>
      </div>
    </router-link>
  </div>
</template>


<script>

export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  computed: {
    movieURL() {
      const posterPath = this.movie.poster_path
      return `https://image.tmdb.org/t/p/w500/${posterPath}`
    }
  }
}
</script>

<style>
.card-text {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}
</style>