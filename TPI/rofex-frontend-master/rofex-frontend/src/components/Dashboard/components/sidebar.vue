<template>
  <aside class="side-nav" id="show-side-navigation1">
    <i
      class="fa fa-bars close-aside hidden-sm hidden-md hidden-lg"
      data-close="show-side-navigation1"
    ></i
    ><br />
    <div class="heading">
      <img
        src="https://www.flaticon.com/svg/static/icons/svg/149/149071.svg"
        alt=""
      />
      <div class="infoHome">
        <p v-if="isLoggedIn">
          {{ currentUser.lastname + ", " + currentUser.name }} <br />
          <br />
          Bienvenido
        </p>
      </div>
    </div>
    <!--<div class="search">
      <input type="text" placeholder="Buscar" /><i class="fa fa-search"></i>
    </div>-->
    <ul class="categories">
      <li>
        <v-icon class="pt-5 mt-5 icon">mdi-chart-tree</v-icon>
        <router-link to="/table">Tabla de trades</router-link>
      </li>
      <li>
        <v-icon class="pt-5 mt-5 icon">mdi-finance</v-icon>
        <router-link to="/graphs">Grafica sus trades</router-link>
      </li>
      <li>
        <v-icon class="pt-5 mt-5 icon">mdi-plus</v-icon>
        <router-link to="/trades">Agregar un trade</router-link>
      </li>
      <li v-if="isLoggedIn">
        <i class="fa fa-sign-out" style="color:white"></i
        ><router-link :to="{ name: 'logout' }">Cerrar Sesión</router-link>
      </li>
    </ul>
    <!-- <div v-for="trade in trades" :key="trade.id" color="white">
      {{ trade.id }}
    </div> -->
  </aside>
</template>

<script>
import Vue from "vue";
import { mapState, mapGetters } from "vuex";
export default Vue.extend({
  name: "Sidebar",

  props: {},
  computed: {
    ...mapState(["currentUser"], ["trades"]),
    ...mapGetters(["isLoggedIn"]),
  },

  mounted() {
    this.$store.dispatch("getMe").then(() => {
      this.$store.dispatch("getTrades");
    });
  },
  methods: {},
});
</script>

<style>
.icon {
  color: #aaa !important;
}
</style>
