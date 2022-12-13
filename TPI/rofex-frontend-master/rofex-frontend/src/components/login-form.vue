<template>
  <div class="loginwrapper">
    <form v-on:submit.prevent="login" class="formwrapper">
      <h1 class="text-center">Iniciar Sesion</h1>
      <div class="userinputwrapper">
        <label for="username">
          <v-text-field
            label="Email"
            :type="'email'"
            name="username"
            v-on:click="clearError"
            v-model="username"
            value=""
            required
          />
        </label>
      </div>
      <div>
        <label for="password">
          <!--
           -->
          <v-text-field
            type="password"
            label="Contraseña"
            name="password"
            required
            v-on:click="clearError"
            id="password"
            v-model="password"
            value=""
          />
        </label>
      </div>
      <div><button type="submit" class="myButton">Ingresar</button></div>
      <br />
      <div v-if="errorMessage" class="errormessage">
        <div>
          <br />
          {{ errorMessage }}
        </div>
      </div>
      <div class="signup">
        <hr />
        <br />
        <span>
          No tienes una cuenta?<router-link to="/registration">
            Registrarte</router-link
          ></span
        >
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",

  data() {
    return {
      username: "",
      password: "",
      errorMessage: "",
      users: [],
    };
  },

  computed: {},
  methods: {
    clearError() {
      this.errorMessage = "";
    },
    login() {
      this.$store
        .dispatch("returnToken", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          this.$router.push({ name: "Menu" });
          return response;
        })
        .catch((error) => {
          this.errorMessage = "Datos Incorrentos";
          return error;
        });
    },
  },
};
</script>

<style>
.signup {
  position: relative;
  top: 2rem;
}
.loginwrapper {
  text-align: center;
  display: flex;
  justify-content: center;
  margin: 8%;
}
.formwrapper {
  border-top: 2px solid #0275d8;
  box-shadow: rgba(0, 0, 0, 0.47) 0px 5px 14px;
  padding: 4rem 1rem;
  width: 450px;

  border-radius: 5px;
}
.myButton {
  cursor: pointer;
  box-shadow: 0px 1px 0px 0px #97c4fe;
  background: linear-gradient(to bottom, #3d94f6 5%, #1e62d0 100%);
  background-color: #3d94f6;
  border-radius: 5px;
  border: 1px solid #337fed;
  display: inline-block;
  cursor: pointer;
  color: #ffffff;
  font-family: Arial;
  font-size: 15px;
  font-weight: bold;
  padding: 6px 24px;
  text-decoration: none;
  text-shadow: 0px 1px 0px #1570cd;
  width: 99%;
  height: 40px;
  position: relative;
  top: 1rem;
}
.myButton:hover {
  background: linear-gradient(to bottom, #1e62d0 100%, #3d94f6 100%);
  background-color: #1e62d0;
}
.errormessage {
  color: red;
}
@media (max-width: 1005px) {
  .namesfield {
    width: 80%;
  }
}
.userinputwrapper {
  padding-top: 1rem;
}
</style>
