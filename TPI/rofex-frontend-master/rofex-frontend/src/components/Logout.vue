<template>
<div></div>
</template>

<script>
export default {
  created() {
    this.$store.dispatch('LOGOUT_USER')
    this.$store.dispatch('destroyToken')
      .then((response) => {
        this.$router.push({ name: "Login" });
        return response;
      });
  }
}
</script>

