<template>
  <Navbar />
  <router-view />
</template>

<script lang="ts">
import Navbar from '@/components/Navbar'
import { defineComponent } from 'vue'
import firebase from 'firebase'

export default defineComponent({
  components: {
    Navbar,
  },
  created() {
    const db = firebase.firestore()
    let lastGameDataId = ''
    db.collection('users')
      .doc('dev')
      .onSnapshot((doc: any) => {
        if (lastGameDataId !== doc.data().last_game_data_id) {
          lastGameDataId = doc.data().last_game_data_id
          this.$store.dispatch('fetchGameDataById', lastGameDataId)
        }
      })
  },
})
</script>

<style lang="scss">
html,
body {
  height: 100%;
}
#app {
  height: 100%;
  display: flex;
  flex-flow: column;
}
</style>
