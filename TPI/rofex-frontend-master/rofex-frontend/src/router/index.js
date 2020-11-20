import Vue from "vue";
import VueRouter from "vue-router";

import Dashboard from "../views/dashboard.vue";
import LogOut from "../components/Logout.vue";
import menu from "../views/menu.vue";
import Login from "../views/login.vue";
import Registration from "../views/registration.vue";

import Trades from "../components/trades.vue";
import Table from "../components/table-chart.vue";
import Graphs from "../components/graphs.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/trades",
    name: "trades",
    component: Trades,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/logout",
    name: "logout",
    component: LogOut,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/",
    name: "Login",
    component: Login,
    meta: {
      requiresAuth: false,
    },
  },
  {
    path: "/registration",
    name: "Registration",
    component: Registration,
    meta: {
      requiresAuth: false,
    },
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/menu",
    name: "Menu",
    component: menu,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/table",
    name: "Table",
    component: Table,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/graphs",
    name: "Graphs",
    component: Graphs,
    meta: {
      requiresAuth: true,
    },
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
