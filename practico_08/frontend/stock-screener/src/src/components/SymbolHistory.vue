<template>
  <b-container fluid v-if="data">
    <b-row>
      <b-card>
        <b-table small :items="historicData" fixed sticky-header></b-table>
      </b-card>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "SymbolHistory",
  props: ["data"],
  data() {
    return {};
  },
  methods: {
    JSONHistoryToArray(json) {
      let jsonArray = [];
      for (let k of Object.keys(json)) {
        json[k].Date = k;
        jsonArray.push(json[k]);
      }
      return jsonArray;
    },
  },
  computed: {
    historicData: function () {
      return this.data ? this.JSONHistoryToArray(this.data) : null;
    },
  },
};
</script>

<style>
</style>
