<template>
  <button
    type="button"
    class="
      ml-3
      inline-flex
      justify-center
      py-2
      px-4
      border
      rounded-md
      shadow-sm
      text-sm
      font-medium
    "
    :class="{
      'bg-indigo-600 border-transparent text-white hover:bg-indigo-700':
        variant == 'primary',
      'bg-white border-gray-300 text-gray-700 hover:bg-gray-50': variant == 'secondary',
    }"
    @click.prevent.stop="$emit('on-click')"
  >
    {{ title }}
  </button>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'BaseButton',
  props: {
    title: {
      type: String,
      required: true,
    },
    variant: {
      type: String,
      default: 'primary',
      validator(value: string) {
        return ['primary', 'secondary'].includes(value)
      },
    },
  },
  emits: ['on-click'],
})
</script>
