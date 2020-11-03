<template>
  <b-container v-if="data">
    <b-row>
      <b-col>
        <span>{{ pattern }}</span>
      </b-col>
    </b-row>
  </b-container>
</template>


<script>
export default {
  name: "SpyPattern",
  props: ["data"],
  data() {
    return {};
  },
  computed: {
    pattern: function () {
      return this.data ? this.data : "No se encontro ningun patron";
    },
  },
};
</script>

<style></style>;
