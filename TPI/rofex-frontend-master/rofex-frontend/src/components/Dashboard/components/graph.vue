<template>
  <section class="charts">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-12">
          <div class="tableWr">            
            <div class="formWra">
                <h1 class="text-center titletrade">
              <strong> Sus Trades</strong>
              <hr class="linea" />
              </h1>
              <div class="graficoa" >
                <div class="row mt-5" v-if="arrPositive.length > 0">
                  <div class="col">
                    <h2 class="text-center ti" >Historial de mis Trades</h2>
                    <line-chart
                      :chartData="arrPositive"
                      :options="chartOptions"
                      :chartColors="positiveChartColors"
                      label="Precio"
                    />
                  </div>
                </div>
              </div>
              <br><br>
              <div>
              <div class="grafico" >
                <div class="col-md-6 graficoa" v-if="tradeDONov20.length > 0">
                  <div class="col">
                    <h2 class="text-center ti" >DONov20</h2>
                    <line-chart
                      :chartData="tradeDONov20"
                      :options="chartOptions"
                      :chartColors="positiveChartColors"
                      label="Precio"
                    />
                  </div>
                </div>
              </div>
              <div class="grafico" >
                <div class="col-md-6 graficoa" v-if="tradeDODic20.length > 0">
                  <div class="col">
                    <h2 class="text-center ti" >DODic20</h2>
                    <line-chart
                      :chartData="tradeDODic20"
                      :options="chartOptions"
                      :chartColors="positiveChartColors"
                      label="Precio"
                    />
                  </div>
                </div>
              </div>
              <br>
              <pre>

              </pre>
              </div>
              <div class="grafico" >
                <div class="col-md-6 graficoa" v-if="tradeDOEne21.length > 0">
                  <div class="col">
                    <h2 class="text-center ti" >DOEne21</h2>
                    <line-chart
                      :chartData="tradeDOEne21"
                      :options="chartOptions"
                      :chartColors="positiveChartColors"
                      label="Precio"
                    />
                  </div>
                </div>
              </div>
              <div class="grafico" >
                <div class="col-md-6 graficoa" v-if="tradeDOFeb21.length > 0">
                  <div class="col">
                    <h2 class="text-center ti" >DOFeb21</h2>
                    <line-chart
                      :chartData="tradeDOFeb21"
                      :options="chartOptions"
                      :chartColors="positiveChartColors"
                      label="Precio"
                    />
                  </div>
                </div>
              </div>
            </div>
        </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import LineChart from "./Vuechart";

//import moment from "moment";
export default {
  components: {
    LineChart
  },
  data() {
    return {
      tradeDONov20:[],
      tradeDODic20:[],
      arrPositive: [],
      tradeDOFeb21:[],
      tradeDOEne21:[],
      positiveChartColors: {
        borderColor: "#077187",
        pointBorderColor: "#0E1428",
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        gridLines:true,animation: false
        ,scales: {
                    xAxes: [{
                            type: "time",
                            time: {
                                unit: 'month'
                            },
                        }],
                    yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                }
      }
    };
  },
  async mounted() {
    const  data  = this.getTrades();    
    data.forEach(d => {
      const date = d.datetime;
      const {
        price,
      } = d;
      this.arrPositive.push({ date, total: price });
    
    })
    const  histo  =this.getTradesHistoryDONov20(/*d.symbol,d.datetime*/);
    histo.forEach(de => {
      const date = de.datetime;
      const {
        price,
      } = de;
      this.tradeDONov20.push({ date, total: price });    
    })
     const  histodi  =this.getTradesHistoryDODic20(/*d.symbol,d.datetime*/);
    histodi.forEach(de => {
      const date = de.datetime;
      const {
        price,
      } = de;
      this.tradeDODic20.push({ date, total: price });    
    })
     const  histoe  =this.getTradesHistoryDOEne21(/*d.symbol,d.datetime*/);
    histoe.forEach(de => {
      const date = de.datetime;
      const {
        price,
      } = de;
      this.tradeDOEne21.push({ date, total: price });    
    })
     const  histof  =this.getTradesHistoryDOFeb21(/*d.symbol,d.datetime*/);
    histof.forEach(de => {
      const date = de.datetime;
      const {
        price,
      } = de;
      this.tradeDOFeb21.push({ date, total: price });    
    })
  },
  methods: {
    getTrades: function() {
      return this.$store.getters.getTrades;
    },
    getTradesHistoryDONov20() {
      return this.$store.getters.getTradesHistoryDONov20;
    },
    getTradesHistoryDODic20() {
      return this.$store.getters.getTradesHistoryDODic20;
    },
    getTradesHistoryDOEne21() {
      return this.$store.getters.getTradesHistoryDOEne21;
    },
    getTradesHistoryDOFeb21() {
      return this.$store.getters.getTradesHistoryDOFeb21;
    },
    }
};
</script>

<style scoped>
pre{
  background-color: transparent;
  border-color: transparent;
}
.charts {
  height: auto;  
  min-height:895px
}
.ti,.ola{
  color: black;
}
.graficoa{
  background-color: rgba(255, 255, 255, 0.747);
}
table{
   position:relative;
   margin:auto;
   width:100%;
   /*left:-15%*/;
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
</style>