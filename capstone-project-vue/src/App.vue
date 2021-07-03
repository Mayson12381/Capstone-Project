<template>
  <Navbar />
  <Dashboard />
</template>

<script lang="ts">
import Navbar from '@/components/Navbar'
import Dashboard from '@/views/Dashboard'
import { defineComponent } from 'vue'

export default defineComponent({
  components: {
    Navbar,
    Dashboard,
  },
  setup() {
    return {
      open,
    }
  },
})
</script>
