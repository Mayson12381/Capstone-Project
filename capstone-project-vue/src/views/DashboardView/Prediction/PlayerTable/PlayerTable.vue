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
      <tr v-for="(player, index) in players" :key="player.name" class="bg-white">
        <td
          class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
          :class="{
            'text-red-400': !player.health_status,
            'text-green-600': player.health_status,
          }"
        >
          Player {{ index + 1 }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
          {{ player.weapon ? player.weapon : '-' }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
          {{ player.kevlar ? player.kevlar : '-' }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
          {{ player.nades.length > 0 ? player.nades.join(', ') : '-' }}
        </td>
        <td
          class="px-6 py-4 whitespace-nowrap text-sm text-gray-500"
          :class="{
            'text-red-400': !player.health_status,
            'text-green-600': player.health_status,
          }"
        >
          {{ player.health_status ? 'Alive' : 'Dead' }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'PlayerTable',
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
        return {
          player1: {
            health_status: 1,
            nades: [],
            kevlar: null,
            weapon: '',
          },
        }
      }
    },
  },
})
</script>
