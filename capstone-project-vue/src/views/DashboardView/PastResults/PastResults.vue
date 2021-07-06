<template>
  <div class="flex flex-col">
    <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
        <div class="shadow overflow-hidden border-b border-gray-200">
          <table class="min-w-full divide-y divide-gray-200">
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
                  Map and Round
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
                  "
                >
                  Parameters
                </th>
              </tr>
            </thead>
            <tbody>
              <tr class="bg-white">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Inferno - Round 6
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  A - 80%, B - 30%
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Full Buy
                </td>
              </tr>
              <tr class="bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Inferno - Round 8
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  A - 30%, B - 25%
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Force-Buy
                </td>
              </tr>
              <tr class="bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Mirage - Round 17
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  A - 95%, B - 45%
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Full Buy
                </td>
              </tr>
              <tr class="bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Mirage - Round 20
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  A - 5%, B - 30%
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Eco</td>
              </tr>
              <tr class="bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Mirage - Round 25
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  A - 90%, B - 40%
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Full Buy
                </td>
              </tr>
              <tr class="bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Mirage - Round 26
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  A - 20%, B - 80%
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Half Buy
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {
    return {}
  },
})
</script>
