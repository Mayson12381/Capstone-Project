<template>
  <PredictionsTable :predictions="predictions" @delete-result="onDeleteResult($event)" />
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import PredictionsTable from './PredictionsTable'

export default defineComponent({
  components: { PredictionsTable },
  computed: {
    predictions() {
      return this.$store.getters.predictions
    },
  },
  methods: {
    onDeleteResult(resultId: string) {
      this.$store.dispatch('deleteResult', resultId)
      this.$store.dispatch('fetchPredictions')
    },
  },
})
</script>
