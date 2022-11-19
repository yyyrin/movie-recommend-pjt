<template>
  <div>
    <p>{{ community.name }}</p>
    <p>{{ community.thumbnail }}</p>
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