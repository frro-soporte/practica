import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    symbol: {
      code: "AAPL",
      range: "1mo"
    }, 
  loading: false,
  info : '',
  history: '',
  spypattern: ''

  },
  actions: {
    setCode({ commit }, { code }) {
      commit("setCode", code);
    },
    setRange({ commit }, { range }) {
      commit("setRange", range);
    },
    getInfo({ commit }, {  }) {
      const infoResponse =  await this.$api
      .getStockInfo("AAPL")
      .then((response) => {
        return response.data
      })
      .catch((error) => {
        this.loading = false;

        // eslint-disable-next-line no-console
        console.log(error);
      });
      commit("getInfo", infoResponse);
    },
    getHistory({ commit }, {  }) {
      commit("getHistory", history);
    },
    getSpypattern({ commit }, {  }) {
      commit("getSpypattern", spypattern);
    }
    
  },
  mutations: {
    setCode: (state, code) => {
      state.symbol.code = code;
    },
    setRange: (state, range) => {
      state.symbol.range = range;
    },
    getInfo: (state, info) => {
      state.info = info;
    },
    getHistory: (state, history) => {
      state.history = history;
    },
    getSpypattern: () => {
      state.symbol.range = range;
    }
    
  },
  getters: {
    code: state => state.symbol.code,
    range: state => state.symbol.range,
    info: state=> state.info
  }
});

export default store;
