/* eslint-disable */

import axios from "axios";

let BASE_API = process.env.VUE_APP_BASE_API;

const http = axios.create({
  baseURL: BASE_API,
});

const api = {
  getSpy_pattern(stock,range) {
    return http.get("/spy_pattern", {
        stock: stock,
        range: range,

    });
  },
  getStockHistory(stock,range) {
    return http.get("historic", {
      stock: stock,
      range: range
    });
  },
  getStockInfo(stock) {
    return http.get("/info", {
      stock:stock
    });
  },

};

export { api, http };
