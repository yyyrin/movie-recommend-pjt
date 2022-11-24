<template>
  <div>
    <router-link :to="{ name: 'movie_detail', params: { id: review?.movie.id } }">
      <div class="col">
        <div style="color:black;" class="card embed-responsive embed-responsive-5by3">
          <img :src=review?.movie.poster_path alt="">
          <p>영화명: {{ review?.movie.title }}</p>
          <p>리뷰 내용: {{ review?.content }}</p>
          <p>좋아요 수: {{ review?.like_user.length }}</p>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'ReviewItem',
  props: {
    review: Object,
  },
}
</script>

<style>

</style>