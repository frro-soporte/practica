<template>
  <b-container fluid>
    <VueTradingView
      :options="`{symbol:'NASDAQ:${this.symbol}',theme:'dark'}`"
    />
  </b-container>
</template>

<script>
import VueTradingView from "vue-trading-view";

export default {
  name: "SymbolView",
  props: {
    symbol: {
      type: String,
      default: "AAPL",
    },
  },
  components: {
    VueTradingView,
  },
  watch:{
    symbol(){
      this.$forceUpdate() 
    }
  }
};
</script>

<style scoped>
#vue-trading-view>>>div {
  width: 100px;
}

</style>
