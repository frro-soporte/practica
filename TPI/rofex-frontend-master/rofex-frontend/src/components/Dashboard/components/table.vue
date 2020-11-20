<template>
  <section class="charts">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-12">
          <div class="tableWr">
            <div class="formWra ">
              <h1 class="text-center titletrade">
                <strong> Sus Trades</strong>
                <hr class="linea" />
              </h1>
              <div id="app" class="container" v-if="trades.length == 0">
                <h2>No hay Trades Cargados</h2>
              </div>
              
              <div
                id="app"
                class="container col-md-12"
                v-if="trades.length !== 0"
              >
                <table border="1" >
                  <thead>
                    <th>Dolar Futuro</th>
                    <th>Cantidad Comprada</th>
                    <th>Precio ($)</th>
                    <th>Fecha</th>
                    <th></th>
                  </thead>
                  <tr v-for="trade in trades" v-bind:key="trade.idtrade">
                    <td>{{ trade.symbol }}</td>
                    <td>{{ trade.size }}</td>
                    <td>{{ trade.price }}</td>
                    <td>{{ trade.datetime }}</td>
                    <td>
                      <button class="red" @click="deleteT(trade.idtrade)">
                        <v-icon id="iconDelete">mdi-delete</v-icon>
                      </button>
                    </td>
                  </tr>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import Vue from "vue";
import moment from "moment";
//import { mapActions } from "vuex";

export default Vue.extend({
  name: "Tables",
  data() {
    return {
      trades: [],
      componentKey:0,
    };
  },
  mounted() {
    this.getTrades();
    this.trades.forEach((trade) => {
      trade.datetime = moment(trade.datetime).format("DD/MMM/YYYY");
    });
  },
  methods: {
    getTrades: function() {
      this.trades = this.$store.getters.getTrades;
    },
    deleteT(idtrade) {
        this.$store.dispatch('deleteTrade', idtrade)
        .then(this.$router.push({ name: "Dashboard" }))
           
    }
  },
    //...mapActions(["deleteTrade"]),
  
});
</script>
<style scoped>
.red {
  background-color: #f44336;
  border-radius: 10px;
}
td + td,
th + th {
  border-left: 2px solid black;
}
tr + tr {
  border-top: 2px solid black;
}

td,
th {
  padding: 3px;
}

.charts {
  height: auto;
  min-height: 895px;
}
table {
  position: relative;
  margin: auto;
  width: 100%;
  left: auto;
  background-color: #c7ace6;
  border: black;
  color: black;
  border-radius: 1px;
}
th {
  text-align: center;
  color: black;
  background-color: #7b5e9b;
  border-radius: 1px;

  font-size: 30px;
}

.titletrade {
  position: relative;
  text-align: center;
  border: 10px;
}
.tableWr {
  text-align: center;
  display: flex;
  justify-content: center;
  margin: 10%;
}
.formWra {
  margin-top: -130px;
  background: #313348;
  box-shadow: rgba(0, 0, 0, 0.47) 0px 5px 14px;
  padding: 6rem 1rem;
  width: 100%;
  color: #bbb;
  font-size: 23px;
  display: block;
}
#iconDelete {
  margin: 5px;
  font-size: 30px;
  color: #ffffff;
}
</style>
