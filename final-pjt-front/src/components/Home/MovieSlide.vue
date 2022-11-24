<template>
  <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img class="slide-img card-img-top" src="@/assets/wolf.jpg" contain>
      </div>
      <div class="carousel-item">
        <img class="slide-img card-img-top" src="@/assets/abouttime.jpg" contain>
      </div>
      <div class="carousel-item">
        <img class="slide-img card-img-top" src="https://www.10wallpaper.com/wallpaper/medium/1603/Me_before_you_2016-Movie_High_Quality_Wallpaper_medium.jpg" contain>
      </div>
      <div class="carousel-item">
        <img class="slide-img card-img-top" src="https://mblogthumb-phinf.pstatic.net/MjAyMTAyMDJfMjkw/MDAxNjEyMjUxMzk0OTA0.Q6qjz9YG_0KFsQQDF_imqE9HqtsBNQnnWnLj8-8yZOAg.q7MZJWcoHzCmmHfXYl5sgg6zoilYPR66t5bjLeFYo-Eg.JPEG.minarigirl/%EC%86%8C%EC%9A%B85.jpg?type=w800" contain>
      </div>
      <!-- <div class="carousel-item" v-for="(poster, index) in posters" :key="index">
        <img :src="poster.src" contain height="380px">
      </div> -->
      <!-- <MovieSlideItem v-for="movie in movies.slice(0, 10)" :key="movie.id" :movie="movie"/> -->
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script>
// import _ from 'lodash'

export default {
  name: 'MovieSlide',
  // computed: {
  //   movies() {
  //     // return this.$store.state.movies
  //     return _.orderBy(this.$store.state.movies, 'vote_average', 'desc')
  //   }
  // },
  // data() {
  //   return {
  //     posters: {},
  //   }
  // },
  // created() {
  //   this.getPosters()
  // },
  // methods: {
  //   getPosters () {
  //     this.movies = _.orderBy(this.$store.state.movies, 'vote_average', 'desc')
  //     // console.log(this.movies)
  //     for (var step = 0; step < 10; step++) {
  //       var poster_path = this.movies[step].poster_path
  //       // console.log(poster_path)
  //       this.posters[step] = { src : `https://image.tmdb.org/t/p/w500/${poster_path}` } 
  //     }
  //   }
  // }  
} 
</script>

<style>
#carouselExampleControls {
  padding-top: 90px;
}
.slide-img {
  text-align:center;
  object-fit: cover;
  height: 700px;
  width: 1500px;
}

</style>
