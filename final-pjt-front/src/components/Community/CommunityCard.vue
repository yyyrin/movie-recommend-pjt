<template>
  <div>
    <router-link :to="{ name: 'community_article', params: { name: community.name } } ">
      <div>
        {{ community.name }}
      </div>
    </router-link>
    <!-- <p>{{ community.name }}</p>
    <p>{{ community.thumbnail }}</p> -->
  </div>
</template>

<script>
export default {
  name: 'CommunityCard',
  props: {
    community: Object
  },

}
</script>

<style>

</style>