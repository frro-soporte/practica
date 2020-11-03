<template>
  <div id="app">
    <NavBar />
    <b-container fluid v-if="loading">
      <b-row>
        <b-col>
          <b-spinner variant="success" type="grow" label="Spinning">Loading</b-spinner>
        </b-col>
      </b-row>
    </b-container>
    <b-container fluid v-else>
      <b-row>
        <b-col class="text-left p-0" xs="12" sm="12" lg="4" xl="4">
          <Info />
          <SpyPattern />
        </b-col>
      </b-row>
      <b-row align-v="center" align-h="center" class="mt-5">
        <b-col sm="12" md="6">
          <b-form-input
            :disabled="loading"
            class="symbol-input"
            v-model="symbol"
            :placeholder="
              loading ? 'Cargando...' : 'Ingrese el codigo de accion, Ej.: AAPL'
            "
          ></b-form-input>
        </b-col>
        <b-button :disabled="loading" @click="doSearch()">
          <strong v-if="!loading">Buscar</strong>
          <div v-else class="px-3">
            <b-spinner variant="primary" small label="Spinning"></b-spinner>
          </div>
        </b-button>
      </b-row>
      <b-row align-h="center" align-v="center" class="mt-5">
        <b-col cols="12">
          <b-tabs content-class="mt-3 " align="center" pills>
            <b-tab title="General" active>
              <b-row>
                <b-col cols="4"
                  ><b-card class="card-container" title="Informacion">
                    <b-card v-if="loading || dataIsEmpty">
                      <b-skeleton width="85%"></b-skeleton>
                      <b-skeleton width="55%"></b-skeleton>
                      <b-skeleton width="70%"></b-skeleton>
                      <b-skeleton width="85%"></b-skeleton>
                      <b-skeleton width="55%"></b-skeleton>
                      <b-skeleton width="70%"></b-skeleton>
                      <b-skeleton width="85%"></b-skeleton>
                      <b-skeleton width="55%"></b-skeleton>
                      <b-skeleton width="70%"></b-skeleton>
                      <b-skeleton width="85%"></b-skeleton>
                      <b-skeleton width="55%"></b-skeleton>
                    </b-card>
                    <div v-else>
                      <Info :data="data.info" />
                      <SpyPattern :data="data.SpyPattern" />
                    </div> </b-card
                ></b-col>
                <b-col cols="8"
                  ><b-card class="card-container" title="historico">
                    <b-card v-if="loading || dataIsEmpty">
                      <b-skeleton width="85%"></b-skeleton>
                      <b-skeleton width="55%"></b-skeleton>
                      <b-skeleton width="70%"></b-skeleton>
                      <b-skeleton width="85%"></b-skeleton>
                      <b-skeleton width="55%"></b-skeleton>
                      <b-skeleton width="70%"></b-skeleton>
                      <b-skeleton width="85%"></b-skeleton>
                      <b-skeleton width="55%"></b-skeleton>
                      <b-skeleton width="70%"></b-skeleton>
                      <b-skeleton width="85%"></b-skeleton>
                      <b-skeleton width="55%"></b-skeleton>
                    </b-card>
                    <SymbolHistory v-else :data="data.history" /></b-card
                ></b-col>
              </b-row>
            </b-tab>
            <b-tab title="Graficos" :disabled="dataIsEmpty || loading">
              <SymbolView :symbol="this.graphicSymbol"></SymbolView>
            </b-tab>
          </b-tabs>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {
    SymbolView: () => import("@/components/SymbolView.vue"),
    SpyPattern: () => import("@/components/SpyPattern.vue"),
    SymbolHistory: () => import("@/components/SymbolHistory.vue"),
    Info: () => import("@/components/Info.vue"),
  },
  data() {
    return {
      loading: false,
      symbol: "",
      graphicSymbol: "",
      data: {
        history: "",
        info: "",
        SpyPattern: "",
      },
    };
  },
  computed: {
    dataIsEmpty: function () {
      return !this.data.history || !this.data.info || !this.data.SpyPattern;
    },
  },
  methods: {
    async doSearch() {
      this.loading = true;
      this.graphicSymbol = this.symbol;
      try {
        const history = await this.$api.getStockHistory(
          this.symbol || "AAPL",
          "1mo"
        );
        const info = await this.$api.getStockInfo(this.symbol || "AAPL");
        const SpyPattern = await this.$api.getSpy_pattern(
          this.symbol || "AAPL",
          "1mo"
        );
        this.data.history = history.data;
        this.data.info = info.data;
        this.data.SpyPattern = SpyPattern.data;
      } catch (error) {
        throw new Error(error);
      } finally {
        this.loading = false;
      }
    },
  },
  async mounted() {
    this.doSearch();
  },


};
</script>

<style>
.symbol-input {
  left: 3px !important;
  top: 3px !important;
  background-color: rgb(245, 245, 245);
  font-weight: 500;
  border: 1px solid rgba(0, 0, 0, 0.2);
  box-shadow: 1px 1px 1px 1px rgb(155, 155, 155);
}
.symbol-input:focus {
  top: 2px !important;
  left: 2px !important;
  border: 2px solid rgb(10, 154, 238);
  box-shadow: 2px 2px 0px 0px rgb(10, 154, 238) !important;
}
body {
  background-color: rgb(23, 21, 36) !important;
}
.title {
  color: darkcyan;
}
.card-container {
  border: 2px solid rgb(10, 154, 238);
  box-shadow: 4px 4px 3px 3px rgb(15, 71, 104) !important;
  background-color: rgb(235, 235, 235) !important;
}
</style>
