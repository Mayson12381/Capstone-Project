<template>
  <div>
    <div class="relative flex items-start">
      <div class="flex items-center h-5">
        <input
          id="candidates"
          name="candidates"
          type="checkbox"
          class="h-4 w-4 text-indigo-600 border-gray-300 rounded"
          v-model="checked"
          @change="onChange"
        />
      </div>
      <div class="ml-3 text-sm">
        <label for="candidates" class="font-medium text-gray-700">{{ this.title }}</label>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'BaseCheckBox',
  props: {
    title: {
      type: String,
      required: true,
    },
    startSelected: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  data() {
    return {
      checked: this.startSelected,
    }
  },
  methods: {
    onChange() {
      this.$emit('on-click', this.checked)
    },
  },
})
</script>
