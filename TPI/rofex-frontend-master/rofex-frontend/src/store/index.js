import Vue from "vue";
import Vuex from "vuex";
import Api from "@/services/api";
import axios from "axios";

Vue.use(Vuex);

function authHeaders(token) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}
export const store = new Vuex.Store({
  state: {
    token: localStorage.getItem("access_token") || null,
    currentUser: null,
    trades: null,
    tradesHistoryDONov20: null,
    tradesHistoryDODic20: null,
    tradesHistoryDOEne21: null,
    tradesHistoryDOFeb21: null,
    user:null
  },
  getters: {
    isLoggedIn(state) {
      return state.token !== null;
    },
    getUser(state) {
      return state.user;
    },
    getTrades(state) {
      return state.trades;
    },
    getTradesHistoryDONov20(state) {
      return state.tradesHistoryDONov20.trades;
    },
    getTradesHistoryDODic20(state) {
      return state.tradesHistoryDODic20.trades;
    },
    getTradesHistoryDOEne21(state) {
      return state.tradesHistoryDOEne21.trades;
    },
    getTradesHistoryDOFeb21(state) {
      return state.tradesHistoryDOFeb21.trades;
    },
  },
  mutations: {
    SET_CURRENT_USER(state, user) {
      state.currentUser = user;
    },
    LOGOUT_USER(state) {
      state.currentUser = {};
      state.trades = null;
      
      state.tradesHistoryDONov20= null;
      state.tradesHistoryDODic20= null;
      state.tradesHistoryDOEne21= null;
      state.tradesHistoryDOFeb21= null;
    },
    RETURN_TOKEN(state, token) {
      state.token = token;
    },
    DESTROY_TOKEN(state) {
      state.token = null;
    },
    SET_TRADES(state, trades) {
      state.trades = trades;
    },
    SET_TRADESHisDONov20(state, trades) {
      state.tradesHistoryDONov20 = trades;
    },
    SET_TRADESHisDODic20(state, trades) {
      state.tradesHistoryDODic20 = trades;
    },
    SET_TRADESHisDOEne21(state, trades) {
      state.tradesHistoryDOEne21 = trades;
    },
    SET_TRADESHisDOFeb21(state, trades) {
      state.tradesHistoryDOFeb21 = trades;
    },
    DELETE_TRADE(state) {
      state.trade = null;
    },
  },
  actions: {
    async gettradehistoryDONov20( { state, commit }) {
      try {
        axios.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${state.token}`;
        axios.defaults.headers.post["Content-Type"] = "application/json";
        const data = await Api().post(          `/trade_history/?trade_symbol=DONov20&trade_date=2020-05-01`      );
        if (data !== null) {
          commit( 'SET_TRADESHisDONov20', data.data);
        }
        return data;      
        
      } catch (error) {
        return {
          error: "Error al traer trades",
        };
      }
    },
    async gettradehistoryDODic20( { state, commit }) {
      try {
        axios.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${state.token}`;
        axios.defaults.headers.post["Content-Type"] = "application/json";
        const data = await Api().post(          `/trade_history/?trade_symbol=DODic20&trade_date=2020-05-01`      );
        if (data !== null) {
          commit( 'SET_TRADESHisDODic20', data.data);
        }
        return data;      
        
      } catch (error) {
        return {
          error: "Error al traer trades",
        };
      }
    },
    async gettradehistoryDOEne21( { state, commit }) {
      try {
        axios.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${state.token}`;
        axios.defaults.headers.post["Content-Type"] = "application/json";
        const data = await Api().post(          `/trade_history/?trade_symbol=DOEne21&trade_date=2020-05-01`      );
        if (data !== null) {
          commit( 'SET_TRADESHisDOEne21', data.data);
        }
        return data;      
        
      } catch (error) {
        return {
          error: "Error al traer trades",
        };
      }
    },
    async gettradehistoryDOFeb21( { state, commit }) {
      try {
        axios.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${state.token}`;
        axios.defaults.headers.post["Content-Type"] = "application/json";
        const data = await Api().post(          `/trade_history/?trade_symbol=DOFeb21&trade_date=2020-05-01`      );
        if (data !== null) {
          commit( 'SET_TRADESHisDOFeb21', data.data);
        }
        return data;      
        
      } catch (error) {
        return {
          error: "Error al traer trades",
        };
      }
    },
    LOGOUT_USER(context) {
      //Limpia array de datos del user
      context.commit("LOGOUT_USER");
    },
    async getTrades({ state, commit }) {
      if (state.currentUser !== null) {
        await this.getMe;
      }
      try {
        const limit = 100;
        axios.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${state.token}`;
        axios.defaults.headers.post["Content-Type"] = "application/json";
        const data = await Api().post(
          `/trades/?user_id=${state.currentUser.id}&limit=${limit}`
        );
        if (data !== null) {
          commit("SET_TRADES", data.data);
        }
        return data;
      } catch (error) {
        return {
          error: "Error al buscar el usuario",
        };
      }
    },

    //GET USER ONCE LOGGED IN
    async getMe({ commit, state }) {
      if (state.currentUser !== null) {
        return state.currentUser;
      }
      try {
        if (!state.token) {
          return {
            user: null,
            error: null,
          };
        }
        const { data } = await Api().get("/users/me", authHeaders(state.token));
        console.log(data);
        const user = data;
        if (user.id) {
          commit("SET_CURRENT_USER", user);
        } else {
          if (state.token) {
            commit("LOGOUT_USER");
          }
        }
        return data;
      } catch (error) {
        commit("LOGOUT_USER");
        return {
          error: "Error al buscar el usuario",
        };
      }
    },
    //REGISTER NEW USER
    register(context, data) {
      return new Promise((resolve, reject) => {
        let user_data = {
          email: data.email,
          name: data.name,
          lastname: data.lastname,
          hashed_password: data.password,
        };
        Api()
          .post("/users/", user_data)
          .then((response) => {
            resolve(response);
          })
          .catch((error) => {
            console.log(error.response);
            reject(error);
          });
      });
    },
    //TOKENS
    destroyToken(context) {
      if (context.getters.isLoggedIn) {
        localStorage.removeItem("access_token");
        context.commit("DESTROY_TOKEN");
      }
    },
    //LOGIN AND RETURN TOKEN
    returnToken(context, credentials) {
      return new Promise((resolve, reject) => {
        let fd = new FormData();
        fd.append("username", credentials.username);
        fd.append("password", credentials.password);
        Api()
          .post("/token", fd)
          .then((response) => {
            const token = response.data.access_token;
            console.log(response);

            localStorage.setItem("access_token", token);
            context.commit("RETURN_TOKEN", token);
            resolve(response);
          })
          .catch((error) => {
            console.log(error.response);
            reject(error);
          });
      });
    },
    //logoutUser({ commit }) {
    //commmit("LOGOUT_USER");
    //},
    //loginUser({ commit }, user) {
    //commit("SET_CURRENT_USER", user);
    //},
    createTrades(context, data) {
      return new Promise((resolve, reject) => {
        Api()
          .post(
            "/create-trade/",
            {
              symbol: data.symbol,
              size: parseFloat(data.size),
              price: parseFloat(data.price),
              datetime: data.datetime,
              iduser: this.state.currentUser.id,
            },
            authHeaders(this.state.token)
          )
          .then((response) => {
            console.log(response);
            resolve(response);
          })
          .catch((error) => {
            console.log(error.response);
            reject(error);
          });
      });
    },
    deleteTrade(context,id) {
      return new Promise((resolve, reject) => {
        axios.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${this.state.token}`;
        axios.defaults.headers.post["Content-Type"] = "application/json";
        Api()
          .post(
            `/delete-trade/?trade_id=${id}`
          )
          .then((response) => {
            console.log(response);
            resolve(response);
          })
          .catch((error) => {
            console.log(error.response);
            reject(error);
          });
      });
    },
  },
  modules: {},
});
