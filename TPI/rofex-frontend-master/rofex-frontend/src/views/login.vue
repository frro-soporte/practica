<template>
  <login />
</template>

<script>
import login from "../components/login-form";

export default {
  name: "Login",
  components: {
    login,
  },
  beforeCreate() {
    //check if the user is loggedIn
    if (this.$store.getters.isLoggedIn) {
      this.$router.push({ name: "Menu" });
    }
  },
};
</script>
