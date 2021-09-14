<template>
  <div
    class="
      relative
      inline-flex
      items-center
      rounded-full
      border border-gray-300
      px-3
      py-0.5
      text-sm
    "
  >
    <span class="absolute flex-shrink-0 flex items-center justify-center">
      <span
        class="bg-red-500 h-1.5 w-1.5 rounded-full"
        :class="{
          'bg-green-500': status === 'online',
          'bg-red-500': status !== 'online',
        }"
        aria-hidden="true"
      />
    </span>
    <span v-if="status === 'online'" class="ml-3.5 font-medium text-white"
      >Companion Online</span
    >
    <span v-else class="ml-3.5 font-medium text-white">Companion Offline</span>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    status: {
      type: String,
      default: '',
    },
  },
  setup() {
    return {}
  },
})
</script>
