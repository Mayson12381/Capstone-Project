<template>
  <div class="hidden md:block">
    <div class="ml-10 flex items-baseline space-x-4">
      <template v-for="item in navigationItems" :key="item">
        <template v-if="currentRoute === item">
          <div
            class="
              bg-gray-900
              text-white
              px-3
              py-2
              rounded-md
              text-sm
              font-medium
              cursor-pointer
            "
            @click="$emit('click-route', item)"
            data-test="active-tab"
          >
            {{ item }}
          </div>
        </template>
        <div
          v-else
          class="
            text-gray-300
            hover:bg-gray-700 hover:text-white
            px-3
            py-2
            rounded-md
            text-sm
            font-medium
            cursor-pointer
          "
          @click="$emit('click-route', item)"
        >
          {{ item }}
        </div>
      </template>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Tabs',
  props: {
    currentRoute: {
      type: String,
      required: false,
      default: '',
    },
    navigationItems: {
      type: Array,
      required: false,
      default: () => [],
    },
  },
})
</script>
