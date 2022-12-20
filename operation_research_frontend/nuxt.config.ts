import { defineNuxtConfig } from 'nuxt'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  modules: ['@unocss/nuxt'],


  unocss: {
    // presets
    uno: true, // enabled `@unocss/preset-uno`
    icons: true, // enabled `@unocss/preset-icons`
    attributify: true, // enabled `@unocss/preset-attributify`,

    // core options
    shortcuts: [],
    rules: [],
    theme: {
      colors: {
        dark: '#060E28',
      },
    },
  },
  css: ['~/assets/css/main.css', 'primevue/resources/themes/saga-blue/theme.css', 'primevue/resources/primevue.css', 'primeicons/primeicons.css'],
  build: {
    transpile: ['primevue'],
  },
})
