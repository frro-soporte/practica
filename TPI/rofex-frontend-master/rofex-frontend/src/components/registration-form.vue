<template>
  <div class="loginwrapper">
    <form
      v-on:submit.prevent ="errorMessage.length==0? validateForm():''"
      class="formwrapper"
    >
      <h1 class="text-center titlesignup">Crear Cuenta</h1>
      <div class="userinputwrapper">
        <label for="surname">
          <v-text-field label="Apellido" name="surname"   v-model="surname" required />
        </label>
      </div>
      <div class="userinputwrapper">
        <label for="name">
          <v-text-field label="Nombre" name="name" v-on:click="clearError" v-model="name" required  />
        </label>
      </div>
      <div class="userinputwrapper">
        <label for="email">
          <v-text-field :type="'email'" label="Correo Electronico" name="email" v-on:click="clearError" v-model="email" required  />
        </label>        
      </div>
      <div>
        <label for="password">
          <v-text-field label="Contraseña" name="password"  :type="'password'" v-on:click="clearError" v-model="password" required/>
        </label>
      </div>
      <div>
        <label for="repitePass">
          <v-text-field label="Repita la Contraseña" name="repitePass"  :type="'password'" v-on:click="clearError" v-model="repitePass"  required/>
        </label>
      </div>
      <div><button type="submit" class="myButton" >Aceptar</button></div><br>
       <div v-if="errorMessage" class="errormessage">
                   <div v-for="error in errorMessage" v-bind:key="error.index"><br>
                    {{error}}
                   </div>
                </div>
      <div class="signup">
        <hr />
        <br />
        <span>
          Ya tienes cuenta? <router-link to="/">Iniciar Sesión</router-link></span>         
      </div>
    </form>
  </div>
</template>
<script>
import Vue from "vue";
export default Vue.extend({
  name: "SignUp",
  data() {
    return {
      name: "",
      surname: "",
      email: "",
      password: "",
      repitePass:"",
      errorMessage:[],
    };
  },
  methods: {
     validateForm(){
            console.log(history)
            if(this.repitePass == this.password ){    
                if(this.password.length<21 && this.password.length>7){                      
                this.submitForm()
            }else{this.errorMessage.push('La Contraseña debe tener entre 8 y 20 caracteres')             
              return
            }}else{
             this.errorMessage.push('Las Contraseñas no Coinciden')}
            console.log(this.errorMessage)
        },
    clearError() {
      console.log("form fields cleared");
      this.errorMessage = [];
    },
    submitForm() {
        this.$store.dispatch('register', {
          email: this.email,
          name: this.name,
          lastname: this.surname,
          password: this.password
          })
          .then(response=>{
            this.$router.push({ name: 'Login' });        
            return response
            })
          .catch((error)=>{
          this.errorMessage.push('El email ya se encuentra registrado');
          return error;
            });      
    }
  }
});
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
.myButton {
  cursor: pointer;
	box-shadow: 0px 1px 0px 0px #97c4fe;
	background:linear-gradient(to bottom, #3d94f6 5%, #1e62d0 100%);
	background-color:#3d94f6;
	border-radius:5px;
	border:1px solid #337fed;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:15px;
	font-weight:bold;
	padding:6px 24px;
	text-decoration:none;
	text-shadow:0px 1px 0px #1570cd;
  width: 99%;
  height: 40px;
  position: relative;
  top: 1rem;
}
.myButton:hover {
	background:linear-gradient(to bottom, #1e62d0 100%, #3d94f6 100%);
	background-color:#1e62d0;
}
</style>
