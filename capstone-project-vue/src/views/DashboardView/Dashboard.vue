<template>
  <BaseModal
    :isActive="isModalActive"
    @close="isModalActive = false"
    :title="isPredictionLoading ? 'Getting Prediction...' : 'Prediction'"
  >
    <template v-slot:body>
      <div class="flex justify-center items-center" v-if="isPredictionLoading">
        <div
          class="
            animate-spin
            rounded-full
            h-10
            w-10
            border-t-2 border-b-2 border-indigo-600
          "
        ></div>
      </div>
      <prediction-stats v-else :prediction="prediction.prediction" />
    </template>
  </BaseModal>
  <header class="bg-white shadow">
    <div class="flex">
      <div class="w-1/2 ml-6 py-4 border-r border-gray-300">
        <h3 class="text-lg leading-6 font-medium text-gray-900">Prediction</h3>
      </div>
      <div class="w-1/2 ml-6 py-4">
        <h3 class="text-lg leading-6 font-medium text-gray-900">Past Results</h3>
      </div>
    </div>
  </header>
  <main class="flex flex-col flex-auto">
    <div class="flex flex-auto">
      <div class="w-1/2 border-r border-gray-300 flex flex-col">
        <Prediction
          :companionStatus="companionStatus"
          @get-data="onClickGetData"
          @predict="onClickPredict"
        />
      </div>
      <div class="w-1/2">
        <PastResults />
      </div>
    </div>
  </main>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import PastResults from './PastResults'
import Prediction from './Prediction'
import firebase from 'firebase'
import BaseModal from '@/components/BaseModal'
import PredictionStats from '@/components/PredictionStats/PredictionStats.vue'

export default defineComponent({
  components: {
    PastResults,
    Prediction,
    BaseModal,
    PredictionStats,
  },
  data() {
    return {
      isModalActive: false,
      isPredictionLoading: false,
      prediction: { A: 0, B: 0 },
    }
  },
  created() {
    const db = firebase.firestore()
    let lastGameDataId = ''
    db.collection('users')
      .doc('dev')
      .onSnapshot((doc: any) => {
        if (lastGameDataId !== doc.data().last_game_data_id) {
          console.log('new game data')
          lastGameDataId = doc.data().last_game_data_id
          this.$store.dispatch('fetchGameDataById', lastGameDataId)
        }
      })
  },
  mounted() {
    this.$store.dispatch('fetchPredictions')
  },
  computed: {
    companionStatus(): string {
      return this.$store.getters.companionStatus
    },
  },
  methods: {
    onClickGetData(): void {
      if (this.companionStatus === 'online') {
        this.$store.dispatch('setGetDataFlag')
      }
    },
    async onClickPredict(): Promise<void> {
      this.isPredictionLoading = true
      this.isModalActive = true
      const predictionID = await this.$store.dispatch('getPredictionForLatestGameData', {
        gameDataId: 'placeholder',
        map: 'inferno',
        userId: 'dev',
      })
      await this.$store.dispatch('fetchPredictions')
      console.log(this.$store.getters.predictions)
      this.prediction = this.$store.getters.predictions.find(
        (prediction: any) => prediction.id === predictionID
      )
      this.isPredictionLoading = false
    },
  },
})
</script>
