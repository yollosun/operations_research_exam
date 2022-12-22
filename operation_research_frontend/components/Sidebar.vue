<script lang="ts" setup>
import { computed } from 'vue'

const link = computed(() => {
  return 'decoration-none block w-full text-white px-6 py-4 rounded-md text-sm font-medium'
})

const linkActive = computed(() => {
  return 'bg-white text-black'
})
</script>

<template>
  <div class="flex flex-col items-center justify-start w-full ">
    <img src="~/assets/images/almau_full_logo.png" alt="logo" class="w-40 p-b-5" />
    <NuxtLink :active-class="linkActive" :class="link" to="/"><i class="pi pi-home p-r-5"></i> Главная</NuxtLink>
    <NuxtLink :active-class="linkActive" :class="link" to="/queue/single_channel"><i class="pi pi-arrow-up p-r-5"></i>
      Одноканальная СМО
    </NuxtLink>
    <NuxtLink :active-class="linkActive" :class="link" to="/queue/multi_channel_expectation"> <i
        class="pi pi-arrows-alt p-r-5"></i>
      Многоканальная СМО c ожиданием
    </NuxtLink>
    <NuxtLink :active-class="linkActive" :class="link" to="/queue/multi_channel_rejection"> <i
        class="pi pi-arrows-h p-r-5"></i>
      Многоканальная СМО с отказами
    </NuxtLink>
    <NuxtLink :active-class="linkActive" :class="link" to="/nlp/pegasus"> <i class="pi pi-star-fill p-r-5"></i>
      Парафрайзер
    </NuxtLink>
  </div>

</template>
