import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    symbol: {
      code: "AAPL",
      range: "1mo"
    }
  },
  actions: {
    setCode({ commit }, { code }) {
      commit("setCode", code);
    },
    setRange({ commit }, { range }) {
      commit("setRange", range);
    }
  },
  mutations: {
    setCode: (state, code) => {
      state.symbol.code = code;
    },
    setRange: (state, range) => {
      state.symbol.range = range;
    }
  },
  getters: {
    code: state => state.symbol.code,
    range: state => state.symbol.range
  }
});

export default store;
