<template>
  <div>
    <router-link :to="{ name: 'community_article_detail', params: { community_id: article.community.id, article_id: article.id } }">
      <div class="col">
        <div class="card embed-responsive embed-responsive-5by3">
          <p>커뮤니티명: {{ article.community.name }}</p>
          <p>title:{{ article.title }}</p>
          <p>좋아요수: {{article.like_users.length}}</p>
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
  name: 'ArticleItem',
  props: {
    article: Object,
  },
}
</script>

<style>

</style>