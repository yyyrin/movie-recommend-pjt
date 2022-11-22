<template>
  <div>
    <li class="list-group-item">
      <!-- <p>{{ review }}</p> -->
      <p>영화명: {{ review?.movie.title }}</p>
      <p>리뷰 내용: 
        <router-link :to="{ name: 'movie_detail', params: { id: review?.movie.id } }">
          {{ review?.content }}
        </router-link>
      </p>
      <p>좋아요 수: {{ review?.like_user.length }}</p>
    </li>
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