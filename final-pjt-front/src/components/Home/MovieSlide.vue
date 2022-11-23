<template>
  <div>
    <Flicking :options="{ renderOnlyVisible: true }">
        <div v-for="idx in list" class="flicking-panel" :key="idx">{{ idx }}</div>
      </Flicking>
      <!-- <MovieSlideItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      /> -->
      <!-- <div class="card-panel">1</div>
      <div class="card-panel">2</div>
      <div class="card-panel">3</div>
      <div class="card-panel">4</div>
      <div class="card-panel">5</div>
      <div class="card-panel">6</div>
    </Flicking> -->
    <!-- <carousel-3d> -->
      <!-- <slide> -->
      <!-- <slide v-for="movie in movies" :key="movie.id"> -->
      <!-- <slide v-for="movie in movies" :key="movie.id">
        <span class="title">You know</span> -->
        <!-- <MovieSlideItem v-for="movie in movies" :key="movie.id" :movie="movie"/> -->
        <!-- <template slot-scope="{ index, isCurrent, leftIndex, rightIndex }">
            <img :data-index="index" :class="{ current: isCurrent, onLeft: (leftIndex >= 0), onRight: (rightIndex >= 0) }" :src="movieURL">
        </template> -->
      <!-- </slide> -->
    <!-- </carousel-3d> -->
  </div>
</template>

<script>
import { Flicking } from "@egjs/vue-flicking";
import "@egjs/flicking-plugins/dist/flicking-plugins.css";
// import { Perspective } from "@egjs/flicking-plugins";
// import MovieSlideItem from '@/components/Home/MovieSlideItem'

export default {
  name: 'MovieSlide',
  components: {
    Flicking,
    // MovieSlideItem,
  },
  data() {
    return {
      list: [0, 1, 2, 3, 4]
    }
  }
  // computed: {
  //   movies() {
  //     return this.$store.state.movies
  //   }
  // },
}
</script>

<style>
/* @import url("node_modules/@egjs/vue-flicking/dist/flicking.css"); */

</style>
