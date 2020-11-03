<template>
<b-container fluid v-if="loading">
<b-row>
  <b-col>
   <h3> Symbol Info</h3>
   <b-spinner variant="success" type="grow" label="Spinning">Loading</b-spinner>
  </b-col>
</b-row>
</b-container>
  <b-container fluid v-else>
    <b-row>
      <b-col xs="12" sm="12" lg="12" xl="12">
        <h3 class="card-text" v-b-toggle.collapse-1-inner size="sm">
          {{ symbol.longName }}
        </h3>
        <b-collapse id="collapse-1-inner" class="mt-2">
          <b-card>{{ symbol.longBusinessSummary }}</b-card>
        </b-collapse>
      </b-col>
    </b-row>
    <b-row>
      <b-col class="text-right p-4" xs="12" sm="12" lg="12" xl="12">
        <b-container>
          <b-row>
            <b-col class="text-left p-0" xs="6" sm="6" lg="6" xl="6">
              Previous close
              <br />Open price <br />Bid <br />Ask <br />Day's Range
              <br />Market capital <br />Fifty Day's range <br />Volume
              <br />Avg. Volumne <br />Beta <br />Forward EPS <br />Forward PE
              <br />
            </b-col>
            <b-col class="text-left p-0" xs="6" sm="6" lg="6" xl="6">
              <strong>
                {{ symbol.previousClose }}
                <br />
              </strong>
              <strong>
                {{ symbol.open }}
                <br />
              </strong>
              <strong>
                {{ symbol.bidSize }} {{ symbol.bid }}
                <br />
              </strong>
              <strong>
                {{ symbol.askSize }} {{ symbol.ask }}
                <br />
              </strong>
              <strong>
                {{ symbol.dayHigh - symbol.dayLow }}
                <br />
              </strong>
              <strong>{{ symbol.marketCap }}</strong>
              <br />
              <strong>{{
                symbol.fiftyTwoWeekHigh - symbol.fiftyTwoWeekLow
              }}</strong>
              <br />
              <strong>{{ symbol.volume }}</strong>
              <br />
              <strong>{{ symbol.averageVolume }}</strong>
              <br />
              <strong>{{ symbol.beta }}</strong>
              <br />
              <strong>{{ symbol.forwardEps }}</strong>
              <br />
              <strong>{{ symbol.forwardPE }}</strong>
              <br />
            </b-col>
          </b-row>
        </b-container>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "Info",
  props: ["data"],
  data() {
    return {};
  },
  computed: {
    symbol: function() {
      return this.info
      ? this.info
      : ""
    },
    info: function(){  
      return this.$store.getters([''])
    }
    
  },
  async mounted() {
    this.$store.dispatch('getInfo')
  },
};
</script>

<style>
</style>
