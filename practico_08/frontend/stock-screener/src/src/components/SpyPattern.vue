<template>
  <b-container fluid v-if="loading">
    <b-row>
      <b-col>
        <h3>Symbol History</h3>
        <b-spinner variant="success" type="grow" label="Spinning">Loading</b-spinner>
      </b-col>
    </b-row>
  </b-container>
  <b-container v-else>
    <b-row>
      <b-col>
        <h3>Spy Pattern</h3>
        <span>{{pattern}}</span>
      </b-col>
    </b-row>
  </b-container>
</template>


<script>
export default {
  name: "SpyPattern",
  data() {
    return {
      loading: false,
      info: "",
    };
  },
  computed: {
    pattern: function () {
      return this.info ? this.info : "No se encontro ningun patron";
    },
  },
  async mounted() {
    this.loading = true;
    await this.$api
      .getSpy_pattern("AAPL", "1mo")
      .then((response) => {
        this.loading = false;

        this.info = response.data;
      })
      .catch((error) => {
        this.loading = false;

        // eslint-disable-next-line no-console
        console.log(error);
      });
  },
};
</script>

<style></style>;
