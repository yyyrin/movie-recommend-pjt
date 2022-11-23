<template>
  <div>
    <h2>좋아하는 장르를 더 많이 선택하세요.</h2>
    <CheckMovieCards/>
  </div>
</template>

<script>
import CheckMovieCards from '@/components/Home/CheckMovieCards'

export default {
  name: 'CheckPreferenceView',
  components: {
    CheckMovieCards,
  },
  created() {
    this.getCheckMovies()
  },
  methods: {
    
  }
}
</script>

<style>

</style>