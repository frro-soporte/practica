<template>
  <dashboard />
</template>

<script>
import dashboard from "../components/Dashboard/dashboard";

export default {
  name: "board",
  beforeCreate() {
    //check if the user is loggedIn
    if (!this.$store.getters.isLoggedIn) {
      this.$router.push({ name: "Login" });
    }
  },
  components: {
    dashboard,
  },
};
</script>
