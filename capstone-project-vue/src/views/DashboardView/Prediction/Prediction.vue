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
                  Player
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
                  Weapon
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
                  Armor
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
                  Utility
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
                  Status
                </th>
              </tr>
            </thead>
            <tbody>
              <tr class="bg-white">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Player 1
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">AWP</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Kevlar</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Smoke, 2xFlash
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Alive</td>
              </tr>
              <tr class="bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Player 2
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">AK-47</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Kevlar and Helmet
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Smoke, Molo, HE, Flash
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Alive</td>
              </tr>
              <tr class="bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Player 3
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Galil AR
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Kevlar and Helmet
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Smoke, Molo, 2xFlash
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Alive</td>
              </tr>
              <tr class="bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Player 4
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">-</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">-</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">-</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Dead</td>
              </tr>
              <tr class="bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Player 5
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Deagle</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">None</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Smoke, Molo, 2xFlash
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">Alive</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  <form class="space-y-8 divide-y divide-gray-200 p-6">
    <div class="space-y-8 divide-y divide-gray-200 sm:space-y-5">
      <div class="divide-y divide-gray-200 space-y-6 sm:space-y-5">
        <div>
          <h3 class="text-lg leading-6 font-medium text-gray-900">
            Prediction Parameters
          </h3>
          <p class="mt-1 max-w-2xl text-sm text-gray-500">
            Most parameters can be ignored when using the “Get Data” feature, but can be
            fine-tuned if needed.
          </p>
        </div>
        <div class="space-y-6 sm:space-y-5 divide-y divide-gray-200">
          <div class="pt-6 sm:pt-5">
            <div role="group" aria-labelledby="label-email">
              <div class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-baseline">
                <div>
                  <div
                    class="
                      text-base
                      font-medium
                      text-gray-900
                      sm:text-sm sm:text-gray-700
                    "
                    id="label-email"
                  >
                    Strategies/Bombsites
                  </div>
                </div>
                <div class="mt-4 sm:mt-0 sm:col-span-1">
                  <div class="max-w-lg space-y-4">
                    <div class="relative flex items-start">
                      <div class="flex items-center h-5">
                        <input
                          id="comments"
                          name="comments"
                          type="checkbox"
                          class="
                            focus:ring-indigo-500
                            h-4
                            w-4
                            text-indigo-600
                            border-gray-300
                            rounded
                          "
                        />
                      </div>
                      <div class="ml-3 text-sm">
                        <label for="comments" class="font-medium text-gray-700"
                          >A Site</label
                        >
                      </div>
                    </div>
                  </div>
                </div>
                <div class="mt-4 sm:mt-0 sm:col-span-1">
                  <div class="max-w-lg space-y-4">
                    <div>
                      <div class="relative flex items-start">
                        <div class="flex items-center h-5">
                          <input
                            id="candidates"
                            name="candidates"
                            type="checkbox"
                            class="
                              focus:ring-indigo-500
                              h-4
                              w-4
                              text-indigo-600
                              border-gray-300
                              rounded
                            "
                          />
                        </div>
                        <div class="ml-3 text-sm">
                          <label for="candidates" class="font-medium text-gray-700"
                            >B Site</label
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="pt-6 sm:pt-5">
            <div role="group" aria-labelledby="label-email">
              <div class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-baseline">
                <div>
                  <div
                    class="
                      text-base
                      font-medium
                      text-gray-900
                      sm:text-sm sm:text-gray-700
                    "
                    id="label-email"
                  >
                    Options
                  </div>
                </div>
                <div class="mt-4 sm:mt-0 sm:col-span-1">
                  <div class="max-w-lg space-y-4">
                    <div class="relative flex items-start">
                      <div class="flex items-center h-5">
                        <input
                          id="comments"
                          name="comments"
                          type="checkbox"
                          class="
                            focus:ring-indigo-500
                            h-4
                            w-4
                            text-indigo-600
                            border-gray-300
                            rounded
                          "
                        />
                      </div>
                      <div class="ml-3 text-sm">
                        <label for="comments" class="font-medium text-gray-700"
                          >Fast Evaluation</label
                        >
                      </div>
                    </div>
                  </div>
                </div>
                <div class="mt-4 sm:mt-0 sm:col-span-1">
                  <div class="max-w-lg space-y-4">
                    <div>
                      <div class="relative flex items-start">
                        <div class="flex items-center h-5">
                          <input
                            id="candidates"
                            name="candidates"
                            type="checkbox"
                            class="
                              focus:ring-indigo-500
                              h-4
                              w-4
                              text-indigo-600
                              border-gray-300
                              rounded
                            "
                          />
                        </div>
                        <div class="ml-3 text-sm">
                          <label for="candidates" class="font-medium text-gray-700"
                            >Save Result</label
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="pt-5">
      <div class="flex justify-end">
        <button
          type="button"
          class="
            bg-white
            py-2
            px-4
            border border-gray-300
            rounded-md
            shadow-sm
            text-sm
            font-medium
            text-gray-700
            hover:bg-gray-50
            focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500
          "
        >
          Get Data
        </button>
        <button
          type="submit"
          class="
            ml-3
            inline-flex
            justify-center
            py-2
            px-4
            border border-transparent
            shadow-sm
            text-sm
            font-medium
            rounded-md
            text-white
            bg-indigo-600
            hover:bg-indigo-700
            focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500
          "
        >
          Predict
        </button>
      </div>
    </div>
  </form>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {
    return {}
  },
})
</script>
