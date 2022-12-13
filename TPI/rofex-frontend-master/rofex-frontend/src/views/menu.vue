<template class="container">
  <div>
    <v-row>
      <v-col align="center" justify="center" class="menu-row">
        <h1 id="menu">Menu</h1>
      </v-col>
    </v-row>
    <v-row cols="3">
      <v-col
        v-for="(i, index) in items"
        :key="index"
        xl="4"
        lg="4"
        md="3"
        sm="12"
        xs="12"
        align="center"
        class="py-5"
      >
        <v-row>
          <v-col>
            <h3 class="py-5 my-5 color">{{ i.text }}</h3>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card
              class="d-flex align-stretch mb-6"
              color="grey lighten-2"
              flat
              tile
            >
              <router-link :to="i.path">
                <v-icon class="pt-5 mt-5 icon ">
                  {{ i.icon }}
                </v-icon>
              </router-link>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <div>
      <v-card
        class="d-flex align-stretch mb-6"
        color="grey lighten-2"
        flat
        height="640"
        tile
      >
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "menu",
  beforeCreate() {
    //check if the user is loggedIn
    if (!this.$store.getters.isLoggedIn) {
      this.$router.push({ name: "Login" });
    }
  },
  mounted() {
    this.$store.dispatch("getMe").then(() => {
      this.$store.dispatch("getTrades");      
      this.$store.dispatch('gettradehistoryDONov20' );
      this.$store.dispatch('gettradehistoryDODic20');      
      this.$store.dispatch('gettradehistoryDOEne21' );
      this.$store.dispatch('gettradehistoryDOFeb21');
    });
    
  },

  components: {},
  
  data: () => ({
    items: [
      {
        icon: "mdi-chart-tree",
        text: "Tabla de trades",
        path: "table",
      },
      {
        icon: "mdi-finance",
        text: "Grafica de cada trade",
        path: "graphs",
      },
      {
        icon: "mdi-plus",
        text: "Agregar un trade",
        path: "trades",
      },
    ],
  }),
};
</script>
<style scoped>
*,
body {
  background-color: #2a2b3d !important;
}
.menu-row {
  margin: 20px;
}
#menu {
  font-size: 2.5rem;
  color: white;
}
.color {
  color: white;
}
.icon {
  display: inline-block;
  font-size: 120px;
  color: white;
  border-radius: 50%;
}
</style>
