<template>
  <div>
    <dl
      class="
        mt-5
        grid grid-cols-1
        rounded-lg
        border border-gray-200
        bg-white
        overflow-hidden
        shadow-md
        divide-y divide-gray-200
        md:grid-cols-2 md:divide-y-0 md:divide-x
      "
    >
      <div class="px-4 py-5 sm:p-6">
        <dt class="text-xl font-normal text-gray-900">A Site</dt>
        <div
          class="text-2xl font-semibold"
          :class="prediction.A < 50 ? 'text-red-400' : 'text-green-600'"
        >
          {{ prediction.A }}
        </div>
      </div>
      <div class="px-4 py-5 sm:p-6">
        <dt class="text-xl font-normal text-gray-900">B Site</dt>
        <div
          class="text-2xl font-semibold"
          :class="prediction.B < 50 ? 'text-red-400' : 'text-green-600'"
        >
          {{ prediction.B }}
        </div>
      </div>
    </dl>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'PredictionStats',
  props: {
    prediction: {
      type: Object,
      required: true,
    },
  },
})
</script>
