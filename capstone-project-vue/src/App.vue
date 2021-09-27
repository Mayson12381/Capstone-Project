<template>
  <Navbar />
  <router-view />
</template>

<script lang="ts">
import Navbar from '@/components/Navbar'
import { defineComponent } from 'vue'

export default defineComponent({
  components: {
    Navbar,
  },
  setup() {
    return {}
  },
})
</script>

<style lang="scss">
html,
body {
  height: 100%;
}
#app {
  height: 100%;
  display: flex;
  flex-flow: column;
}
</style>
