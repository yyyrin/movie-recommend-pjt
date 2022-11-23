<template id="movie-slide">
  <!-- <swiper class="swiper" ref="mySwiper2"
    :options="swiperOptions"
    @slideChange="slideChangeTransitionStart"
  >
    <MovieSlideItem v-for="movie in movies" :key="movie.id" :movie="movie" 
      :image-source="movie.poster_path"
      background-size="100% 100%"
    />
  </swiper> -->
  <!-- <div>
    <carousel-3d  :controls-visible="true" :controls-prev-html="'&#10092; '" :controls-next-html="'&#10093;'" :controls-width="30" :controls-height="60" :clickable="true">
      <slide></slide>
      <MovieSlideItem v-for="movie in movies" :key="movie.id" :movie="movie"/>
    </carousel-3d>
  </div> -->
  <div></div>
</template>

<script>
//import {Swiper, } from 'vue-awesome-swiper'
//import 'swiper/dist/css/swiper.css'
//import MovieSlideItem from '@/components/Home/MovieSlideItem'

export default {
  name: 'MovieSlide',
/*   components: {
    // Carousel3d,
    Swiper,
    MovieSlideItem
  },
  data() {
    return {
      swiperOptions: {
        slidesPerView: 3,
        spaceBetween: 10,
        freeMode: true,
        mousewheel : true,
      },
    }
  },
  computed: {
    swiper : function() {
				return this.$refs.mySwiper2.$swiper
    },
    movies() {
      return this.$store.state.movies
    }
  },
  methods : {
    slideChangeTransitionStart : function() {
      //console.log(this.swiper.activeIndex); //현재 index값 얻기
    }
  },
  filters : {
    styleSwiper : function(movie){
      return "background:url("+"https://image.tmdb.org/t/p/w500"+movie.poster_path+") no-repeat; background-position: center center;"
    },
  },
  mounted() {
			//console.log('Current Swiper instance object', this.swiper)
		this.swiper.slideTo(1, 1000, false)
  } */
}
</script>

<style>
</style>
