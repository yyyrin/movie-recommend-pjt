<template>
  <div class="movie-card" >
      <div class="col">
        <div class="card h-100">
          <img :src="movieURL" class="card-img-top" alt="movie poster" @click="choosed()">
          <!-- 마우스 오버시 title 보이게 할 계획
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
          </div> -->
        </div>
      </div>

  </div>
</template>


<script>

export default {
  name: 'CheckMovieCard',
  props: {
    movie: Object,
  },
  computed: {
    movieURL() {
      const posterPath = this.movie.poster_path
      return `https://image.tmdb.org/t/p/w500/${posterPath}`
    }
  },
  methods: {
    choosed() {
        this.$emit('choosed', this.movie)
    }
  }
}
</script>

<style>
/* .card-text {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
} */
#main-poster-img {
  height: 380px;
  /* width: 20rem; */
  object-fit: cover;
}
.movie-card {
  min-width: 200px;
  border-style: none;
  border: 0px;
}
</style>