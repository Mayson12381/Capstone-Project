<template>
  <header class="bg-white shadow">
    <div class="flex">
      <div class="w-1/2 ml-6 py-4 border-r border-gray-300">
        <h3 class="text-lg leading-6 font-medium text-gray-900">Prediction</h3>
      </div>
      <div class="w-1/2 ml-6 py-4">
        <h3 class="text-lg leading-6 font-medium text-gray-900">Past Results</h3>
      </div>
    </div>
  </header>
  <main>
    <div class="flex">
      <div class="w-1/2 border-r border-gray-300">
        <Prediction />
      </div>
      <div class="w-1/2">
        <PastResults />
      </div>
    </div>
  </main>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import PastResults from './PastResults'
import Prediction from './Prediction'

export default defineComponent({
  components: {
    PastResults,
    Prediction,
  },
  setup() {
    return {}
  },
})
</script>
