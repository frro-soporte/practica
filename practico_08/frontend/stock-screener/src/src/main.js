import Vue from "vue";
import App from "./App.vue";
import "@babel/polyfill";
import "mutationobserver-shim";
import "./plugins/bootstrap-vue";
import BootstrapVue from "bootstrap-vue";
import IconsPlugin from "bootstrap-vue";
import { api, http } from "@/api/";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { store } from "@/store";


library.add(fas);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.config.productionTip = false;
Vue.prototype.$http = http;
Vue.prototype.$api = api;
Vue.prototype.$env = {
  IMAGE_FORMAT: "image/jpeg"
};

new Vue({
  store,
  render: h => h(App)
}).$mount("#app");
