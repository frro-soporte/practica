<template>
<b-container fluid v-if="loading">
<b-row>
  <b-col>
   <h3> Symbol History</h3>
   <b-spinner variant="success" type="grow" label="Spinning">Loading</b-spinner> 
  </b-col>
</b-row>
</b-container>
  <b-container fluid v-else>
    <b-row>
      <b-card>
        <b-table :items="historicData" fixed sticky-header></b-table>
      </b-card>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "SymbolHistory",
  data() {
    return {
      historyResponse: "",
      loading: false,
    };
  },
  methods: {
    JSONHistoryToArray(json) {
      let jsonArray = [];
      // TODO: maybe i can implemented this process with recursivity to improve it
      for (let k of Object.keys(json)) {
        json[k].Date = k;
        jsonArray.push(json[k]);
      }
      return jsonArray;
    },
  },
  computed: {
    historicData: function () {
      return this.historyResponse
        ? this.JSONHistoryToArray(this.historyResponse)
        : [];
    },
  },
  async mounted() {
    this.loading = true;
    await this.$api
      .getStockHistory("AAPL", "1mo")
      .then((response) => {
    this.loading = false;

        this.JSONHistoryToArray(response.data);
        this.historyResponse = response.data;
      })
      .catch((error) => {
    this.loading = false;

        // eslint-disable-next-line no-console
        console.log(error);
      });
  },
};
</script>

<style>
</style>
