<template>
  <div id="login">

    <div class="container1">
      <div class="card1">
        <div class="card_title1">
          <h1>Log In</h1>
        </div>
        <div class="form1">
        <form class="form-signin1" @submit.prevent="LogIn">
          <input type="text" class="form-control1" id="username" v-model="username" name="username" placeholder="Username" required="" autofocus="" />
          <input type="password" class="form-control1" id="password" v-model="password" name="password" placeholder="Password" required=""/>      
          <button class="btn btn-lg btn-warning btn-block" type="submit" style="background-color:#FF6800;">Login</button>   
        </form>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    LogIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
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

.container1 {
  height: 100vh;
  width: 100%;
  align-items: center;
  display: flex;
  justify-content: center;
  background-image: radial-gradient(
    circle farthest-corner at 10% 20%,
    #f27312eb 0%,
    rgb(167, 138, 107) 90%
  );
}

.card1 {
  border-radius: 10px;
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.3);
  width: 400px;
  height: 400px;
  background-color: #ffffff;
  padding: 10px 30px;
}

.card_title1 {
  text-align: center;
  padding: 10px;
}

.card_title1 h1 {
  font-size: 26px;
  font-weight: bold;
}

.form1 input {
  margin: 10px 0;
  width: 100%;
  background-color: #e2e2e2;
  border: none;
  outline: none;
  padding: 12px 20px;
  border-radius: 4px;
}

.form1 button {
  background-color: #4796ff;
  color: #ffffff;
  font-size: 16px;
  outline: none;
  border-radius: 5px;
  border: none;
  padding: 8px 15px;
  width: 100%;
}

.card_terms1 {
  display: flex;
  align-items: center;
  padding: 10px;
}

.card_terms1 input[type="checkbox"] {
  background-color: #e2e2e2;
}

.card_terms1 span {
  margin: 5px;
  font-size: 13px;
}

.card1 a {
  color: #4796ff;
  text-decoration: none;
}
</style>