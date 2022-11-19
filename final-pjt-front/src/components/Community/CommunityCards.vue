<template>
  <div class="grid">
    <CommunityCard
      class="block"
      v-for="community in communities"
      :key="community.id"
      :community="community"
    />
  </div>
</template>

<script>
import CommunityCard from '@/components/Community/CommunityCard'

export default {
  name: 'CommunityCards',
  components: {
    CommunityCard
  },
  computed: {
    communities() {
      return this.$store.state.communities
    }
  }
}
</script>

<style>

</style>