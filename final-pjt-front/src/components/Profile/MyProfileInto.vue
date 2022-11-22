<template>
  <div>
    <!-- <h1>MyProfileInto</h1> -->
    <img src="@/assets/basic_profile.png" alt="my-profile" height="100">
    <!-- <p>유저 이미지 변경 나중에 : {{ userInfo?.user.img_path }}</p> -->
    <p>사용자: {{ myInfo?.user.username }}</p>
    <button>회원정보 수정</button>
  </div>
</template>

<script>
export default {
  name: 'MyProfileInto',
  props: {
    myInfo: Object,
  },
}
</script>

<style>

</style>