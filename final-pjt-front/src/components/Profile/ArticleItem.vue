<template>
  <div class="d-flex justify-content-center my-5">
    <router-link :to="{ name: 'community_article_detail', params: { community_id: article.community.id, article_id: article.id } }">
      <div class="card2 p-4" style="width: 80; background-color: #FF6800; border-radius: 25px;" >
        <!-- <img src="`${article?.imagepath}`" class="card-img-top" alt="..."> -->
        <div class="card-body2">
          <div class="card-text2">
            <p>커뮤니티명: {{ article?.community.name }}</p>
            <p>title:{{ article?.title }}</p>
            <p>좋아요수: {{article?.like_users.length}}</p>
          </div>
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