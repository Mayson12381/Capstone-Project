<template>
  <table class="shadow min-w-full divide-y divide-gray-200">
    <thead class="bg-gray-50">
      <tr>
        <th
          scope="col"
          class="
            px-6
            py-3
            text-left text-xs
            font-medium
            text-gray-500
            uppercase
            tracking-wider
          "
        >
          Map
        </th>
        <th
          scope="col"
          class="
            px-6
            py-3
            text-left text-xs
            font-medium
            text-gray-500
            uppercase
            tracking-wider
          "
        >
          Predictions
        </th>
        <th
          scope="col"
          class="
            px-6
            py-3
            text-left text-xs
            font-medium
            text-gray-500
            uppercase
            tracking-wider
            hidden
            sm:table-cell
          "
        >
          Buy Type
        </th>
        <th
          scope="col"
          class="
            px-6
            py-3
            text-left text-xs
            font-medium
            text-gray-500
            uppercase
            tracking-wider
            hidden
            md:table-cell
          "
        >
          Predicted On
        </th>
        <th
          scope="col"
          class="
            px-6
            py-3
            text-left text-xs
            font-medium
            text-gray-500
            uppercase
            tracking-wider
          "
        />
      </tr>
    </thead>
    <tbody>
      <tr v-for="(result, index) in predictions" :key="index" class="bg-white">
        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
          {{ result.map.charAt(0).toUpperCase() + result.map.substring(1) }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
          A -
          <span :class="result.prediction.A < 50 ? 'text-red-400' : 'text-green-600'"
            >{{ result.prediction.A }}%</span
          >, B -
          <span :class="result.prediction.B < 50 ? 'text-red-400' : 'text-green-600'"
            >{{ result.prediction.B }}%</span
          >
        </td>
        <td
          class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 hidden sm:table-cell"
        >
          {{ result.round_type }}
        </td>
        <td
          class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 hidden md:table-cell"
        >
          {{ result.predicted_on }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
          <XIcon
            class="h-5 w-5 cursor-pointer stroke-current hover:text-red-400"
            aria-hidden="true"
            @click="$emit('delete-result', result.id)"
          />
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { XIcon } from '@heroicons/vue/solid'

export default defineComponent({
  name: 'PredictionsTable',
  components: {
    XIcon,
  },
  props: {
    predictions: {
      type: Array,
      required: true,
    },
  },
  emits: ['delete-result'],
})
</script>
