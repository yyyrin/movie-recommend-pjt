<template>
  <div id="signup">

    <div class="container">
      <div class="card">
        <div class="card_title">
          <h1>Sign Up</h1>
          <span>이미 계정이 있으신가요? <router-link :to="{ name: 'login' }">Login</router-link></span>
        </div>
        <div class="form">
        <form @submit.prevent="signUp">
          <input type="text" name="username" id="username" placeholder="UserName" v-model="username" required/>
          <input type="password" name="password1" placeholder="Password" id="password1" v-model="password1" required/>
          <input type="password" name="password2" placeholder="Password" id="password2" v-model="password2" required/>
          <button>Sign Up</button>
          </form>
        </div>
      </div>
    </div>
  </div>
  <!-- <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">

      <label for="username">username : </label>
      <input type="text" id="username" v-model="username" required><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1" required><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2" required><br>
      
      <input type="submit" value="SignUp">
    </form>
  </div> -->
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }
      const badwords = this.$store.state.bad
      let flag = 1 
      badwords.forEach(word=>{
        if (username.indexOf(`${word}`) > -1 ){
          alert('바르고 고운말!')
          flag = 0
          return
        }
      })
      if (flag === 1){
        this.$store.dispatch('signUp', payload)
      }
    },
  }
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

.container {
  height: 100vh;
  width: 100%;
  align-items: center;
  display: flex;
  justify-content: center;
  background-image: radial-gradient(
    circle farthest-corner at 10% 20%,
    rgba(252, 140, 55, 0.921) 0%,
    rgb(253, 232, 210) 90%
  );
}

.card {
  border-radius: 10px;
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.3);
  width: 400px;
  height: 400px;
  background-color: #ffffff;
  padding: 10px 30px;
}

.card_title {
  text-align: center;
  padding: 10px;
}

.card_title h1 {
  font-size: 26px;
  font-weight: bold;
}

.form input {
  margin: 10px 0;
  width: 100%;
  background-color: #e2e2e2;
  border: none;
  outline: none;
  padding: 12px 20px;
  border-radius: 4px;
}

.form button {
  background-color: #4796ff;
  color: #ffffff;
  font-size: 16px;
  outline: none;
  border-radius: 5px;
  border: none;
  padding: 8px 15px;
  width: 100%;
}

.card_terms {
  display: flex;
  align-items: center;
  padding: 10px;
}

.card_terms input[type="checkbox"] {
  background-color: #e2e2e2;
}

.card_terms span {
  margin: 5px;
  font-size: 13px;
}

.card a {
  color: #4796ff;
  text-decoration: none;
}

</style>