<template>
  <div class="app-layout">
    <SideBar />
    <router-view />
  </div>
</template>

<script setup lang="ts">
import SideBar from './components/SideBar.vue'
</script>

<style scoped>
.app-layout {
  display: flex;
  width: min(1280px, 100vw);
  height: min(800px, 100vh);
  background: #ffffff;
  border-radius: 16px;
  overflow: hidden;
}
</style>
