<template>
  <b-container>
    <b-row>
      <b-col>
        <b-card>
          <VueTradingView :options="screenerOption" />
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import VueTradingView from "vue-trading-view";

export default {
  name: "SymbolView",
  props: {
    symbol: String,
  },
  components: {
    VueTradingView,
  },
  computed: {
    screenerOption: function () {
      return {
        symbol: this.symbol,
        theme: "dark",
      };
    },
  },
};
</script>

<style scoped>
#vue-trading-view>>>div {
  width: 100px;
}

</style>
