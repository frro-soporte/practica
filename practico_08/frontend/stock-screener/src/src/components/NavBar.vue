<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">Stock Screener</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" v-model="code" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" @click="changeSymbol()">Search</b-button>
          </b-nav-form>       
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data(){
    return{
      code:""
    }
  },
  methods:{
    changeSymbol(){
      this.$store.dispatch("setCode",{code: this.code})
    }
  }
};
</script>

<style>
</style>