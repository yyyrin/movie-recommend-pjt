<template>
  <div>
    <router-link :to="{ name: 'movie_detail', params: { id: movie.id } }">
      <!-- card -->
    </router-link>
  </div>
</template>


<script>

export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
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