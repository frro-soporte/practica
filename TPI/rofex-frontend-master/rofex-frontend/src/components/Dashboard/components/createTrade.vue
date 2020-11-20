<template>
  <section class="charts">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-12">
          <div class="loginWr">
            <form v-on:submit.prevent="createTrad" class="formWra">
              <h1 class="text-center titletrade">
                <strong> Ingrese su Trade</strong>
                <hr class="linea" />
              </h1>
              <div class="UIWr">
                <label for="firstname">
                  <p>Dolar Futuro</p>
                  <select
                    name="Symbol"
                    id="Symbol"
                    class="inputData"
                    v-model="Symbol"
                    required
                  >
                    <option value="DONov20">DONov20</option>
                    <option value="DODic20">DODic20</option>
                    <option value="DOEne21">DOEne21</option>
                    <option value="DOFeb21">DOFeb21</option>
                    <option value="DOMar21">DOMar21</option>
                    <option value="DOAbr21">DOAbr21</option>
                  </select>
                </label>
              </div>
              <div class="UIWr">
                <label for="Size">
                  <p>Cantidad Comprada</p>
                  <input
                    type="number"
                    min="0"
                    v-on:click="clearError"
                    v-model="Size"
                    id="Size"
                    class="inputData"
                    value=""
                    required
                  />
                </label>
              </div>
              <div class="UIWr">
                <label for="Price">
                  <p>Price</p>
                  <input
                    type="number"
                    
                    step="0.01"
                    min="0"
                    v-on:click="clearError"
                    v-model="Price"
                    id="Price"
                    class="inputData"
                    value=""
                    required
                  />
                </label>
              </div>
              <div class="UIWr">
                <label for="Datetime">
                  <p>Datetime</p>
                  <input
                    type="datetime-local"
                    max="2020-11-20T23:59"
                    v-on:click="clearError"
                    id="Datetime"
                    v-model="Datetime"
                    class="inputData"
                    value=""
                    required
                  />
                </label>
              </div>
              <div v-if="errorMessage" class="errormessage">
                  <div><br>
                    {{errorMessage}}
                  </div>
              </div>
              <div>
                <button type="submit" class="submitbtnTrade" >Crear</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import Vue from "vue";
export default Vue.extend({
  name: "CreateTrade", 
  
  data() {
    return {
      Symbol: "",
      Size: "",
      Price: "",
      Datetime: "",
      errorMessage: "",
    };
  },
  methods: {
    
  
    clearError() {
      this.errorMessage = "";
    },
    createTrad() {
      this.$store.dispatch("createTrades", {
        symbol: this.Symbol,
        size: this.Size,
        price: this.Price,
        datetime: this.Datetime,
      }).then(
        alert('Trade Registrado Correctamente!'),
      )
      .catch((error)=>{
        this.errorMessage='Error al Ingresar Trade. Intente mas tarde.';
        return error;
    });
    },
  },
});
</script>
<style>
.UIWr {
  margin-top: 20px;
}
.linea {
  background-color: black;
  color: rgb(59, 58, 58);
  height: 2px;
}
.loginWr {
  text-align: center;
  display: flex;
  justify-content: center;
  margin: 10%;
}
.titletrade {
  position: relative;
  text-align: center;
  border: 10px;
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
.submitbtnTrade {
  cursor: pointer;
  box-shadow: 0px 1px 0px 0px #4434d6;
  background-color: #5e51d3;
  border-radius: 5px;
  display: inline-block;
  cursor: pointer;
  font-size: 25px;
  font-weight: bold;
  padding: 6px 24px;
  text-decoration: none;
  text-shadow: 0px 1px 0px #1570cd;
  position: relative;
  top: 1rem;
  width: 500px;

  margin-top: 20px;
  margin-bottom: 20px;
}
.submitbtnTrade:hover {
  background-color: #5547d4;
}
.submitbtnTrade:focus {
  outline: none;
}
.errormessage {
  color: red;
}
.inputData {
  width: 500px;
  border: 0.5px solid rgb(0, 0, 0);
  border-radius: 5px;
  background-color: #44425c;
  box-shadow: rgba(0, 0, 0, 0.47) 3px 3px 3px;
}
</style>
