<script setup>
import { RouterView } from 'vue-router';
import Navbar from "@/components/Navbar.vue";
</script>

<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-app-bar-title class="title-wrapper">
        <v-btn to="/" class="title-btn" text>Meu Desafio - TECSCI</v-btn>
      </v-app-bar-title>
      <v-spacer></v-spacer>
      <nav>
        <v-btn to="/" text aria-label="Ir para a página inicial">Inicio</v-btn>
        <v-btn to="/api" text aria-label="Ir para a página da API">API</v-btn>
        <v-btn to="/about" text aria-label="Ir para a página Sobre">Sobre</v-btn>
      </nav>
      <v-btn icon @click="toggleTheme" :aria-label="isDarkTheme ? 'Ativar modo claro' : 'Ativar modo escuro'">
        <v-icon>{{ isDarkTheme ? 'mdi-weather-sunny' : 'mdi-weather-night' }}</v-icon>
      </v-btn>
    </v-app-bar>



    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>

<style scoped>
header {
  line-height: 1.5;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
