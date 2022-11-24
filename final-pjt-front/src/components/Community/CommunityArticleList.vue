<template>
  <div id="community-article-list">
    <v-simple-table dark>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left" style="font-size:20px;">
              작성자
            </th>
            <th class="text-center" style="font-size:20px;">
              제목
            </th>
            <th class="text-center" style="font-size:20px;">
              삭제
            </th>
          </tr>
        </thead>
        <tbody>
          <CommunityArticleItem
            v-for="article in articles"
            :key="article.id"
            :article="article"
            :community_id="community.id"
            :community_user_id="community.user.pk"
          />
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
import CommunityArticleItem from '@/components/Community/CommunityArticleItem'

export default {
  name: 'CommunityArticleList',
  components: {
    CommunityArticleItem,
  },
  props: {
    community: Object,
  },
  computed: {
    articles() {
      // return this.$store.state.articles.article_set
      return this.$store.state.articles.article_set.filter((article) => {
        return article.community.id === this.community?.id
      })
    }
  },
}
</script>

<style>
#community-article-list {
  width: 1080px;
}
</style>