<script setup>

import { ref, computed } from 'vue'
import Sidebar from 'primevue/sidebar';
import CustomSidebar from '../components/Sidebar.vue';
import Navbar from '../components/Navbar.vue';

const visibleLeft = ref(false);
const link = computed(() => {
  return 'decoration-none block w-full text-white px-6 py-4 rounded-md text-sm font-medium'
})

const linkActive = computed(() => {
  return 'bg-white text-black'
})
</script>


<template>
  <div class="flex items-start h-100vh">
    <div class="flex items-start h-full">
      <div class="flex flex-col items-center justify-start bg-dark h-100%">
        <div class="p-sidebar-header p-[1rem] flex-col">
          <img src="~/assets/images/almau_short_logo.png" alt="logo" class="w-20 p-b-5" />
          <Button class="bg-[#060E28] b-[#060E28]" icon="pi pi-bars" @click="visibleLeft = true" />
        </div>
        <div class="p-sidebar-content p-[1rem] ">
          <NuxtLink :active-class="linkActive" :class="link" to="/"><i class="pi pi-home"></i></NuxtLink>
          <NuxtLink :active-class="linkActive" :class="link" to="/queue/single_channel"><i class="pi pi-arrow-up"></i>
          </NuxtLink>
          <NuxtLink :active-class="linkActive" :class="link" to="/queue/multi_channel"><i class="pi pi-arrows-alt"></i>
          </NuxtLink>
        </div>
      </div>
      <Sidebar :modal="false" v-model:visible="visibleLeft" class="p-sidebar-sm bg-[#060E28] ">
        <CustomSidebar />
      </Sidebar>
    </div>

    <div class="w-100vw">
      <Navbar />

      <main class="p-4">
        <slot />
      </main>
    </div>

  </div>
</template>

<style>
/* sidebar__названиеблока */
.sidebar {

  background-color: #060E28;

}
</style>


