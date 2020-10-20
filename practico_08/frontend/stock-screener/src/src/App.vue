<template>
  <div id="app">
    <NavBar />
    <b-container fluid v-if="loading">
      <b-row>
        <b-col>
          <b-spinner variant="success" type="grow" label="Spinning">Loading</b-spinner>
        </b-col>
      </b-row>
    </b-container>
    <b-container fluid v-else>
      <b-row>
        <b-col class="text-left p-0" xs="12" sm="12" lg="4" xl="4">
          <Info />
          <SpyPattern />
        </b-col>
        <b-col class="text-left p-0" xs="12" sm="12" lg="8" xl="8">
          <SymbolView></SymbolView>
        </b-col>
      </b-row>
      <b-row class="align-content-center">
        <b-col class="p-0" xs="12" sm="12" lg="12" xl="12">
          <SymbolHistory />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import SymbolView from "@/components/SymbolView.vue";
import SymbolHistory from "@/components/SymbolHistory.vue";
import SpyPattern from "@/components/SpyPattern.vue";
import Info from "@/components/Info.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "App",
  components: {
    SymbolView,
    SpyPattern,
    SymbolHistory,
    NavBar,
    Info,
  },


};
</script>

<style>
</style>
