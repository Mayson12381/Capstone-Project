<template>
  <PlayerTable :players="players" />
  <form class="flex flex-col flex-auto space-y-8 divide-y divide-gray-200 p-6">
    <div class="space-y-8 divide-y divide-gray-200 sm:space-y-5 flex-auto">
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
                    <BaseCheckbox title="A Site" startSelected @update="ASite = $event" />
                  </div>
                </div>
                <div class="mt-4 sm:mt-0 sm:col-span-1">
                  <div class="max-w-lg space-y-4">
                    <BaseCheckbox title="B Site" startSelected @update="BSite = $event" />
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
                    <BaseCheckbox
                      title="Fast Evaluation"
                      @update="fastEvaluation = $event"
                    />
                  </div>
                </div>
                <div class="mt-4 sm:mt-0 sm:col-span-1">
                  <div class="max-w-lg space-y-4">
                    <BaseCheckbox
                      title="Save Result"
                      startSelected
                      @update="saveResult = $event"
                    />
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
                    Map
                  </div>
                </div>
                <div class="mt-4 sm:mt-0 sm:col-span-1">
                  <div class="max-w-lg space-y-4">
                    <BaseSelect @test="console.log('here')" />
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
        <BaseButton title="Get Data" @on-click="$emit('get-data')" variant="secondary" />
        <BaseButton title="Predict" @on-click="$emit('predict')" variant="primary" />
      </div>
    </div>
  </form>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import BaseCheckbox from '@/components/BaseCheckbox'
import BaseButton from '@/components/BaseButton'
import PlayerTable from './PlayerTable'
import BaseSelect from '@/components/BaseSelect'

export default defineComponent({
  components: {
    BaseCheckbox,
    BaseButton,
    PlayerTable,
    BaseSelect,
  },
  data() {
    return {
      fastEvaluation: false,
      saveResult: false,
      ASite: false,
      BSite: false,
    }
  },
  props: {
    companionStatus: {
      type: String,
      required: true,
    },
  },
  emits: ['get-data', 'predict'],
  computed: {
    players(): any {
      if (this.$store.state.gameData) {
        return [
          this.$store.state.gameData.player1,
          this.$store.state.gameData.player2,
          this.$store.state.gameData.player3,
          this.$store.state.gameData.player4,
          this.$store.state.gameData.player5,
        ]
      } else {
        return [
          {
            player1: {
              health_status: 1,
              nades: [],
              kevlar: null,
              weapon: '',
            },
          },
        ]
      }
    },
  },
})
</script>
