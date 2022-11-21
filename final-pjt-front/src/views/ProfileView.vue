<template>
  <div id="ProfileView">
    <nav-bar></nav-bar>
    <h1>MY PROFILE</h1>
    <ProfileInto/>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar'
import ProfileInto from '@/components/Profile/ProfileInto'

export default {
  name: 'ProfileView',
  components: {
    NavBar,
    ProfileInto,
  },
  computed: {
    isLogIn() {
      return this.$store.getters.isLogIn
    }
  },
  created() {
    this.getAccounts()
  },
  methods: {
    getAccounts() {
      if (this.isLogIn === true) {
        this.$store.dispatch('getAccounts')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'signup' })
      }
    }
  }
}
</script>

<style>
#ProfileView {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #FF6800;
}
</style>