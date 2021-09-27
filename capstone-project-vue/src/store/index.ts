import { createStore, Store } from 'vuex'
import { InjectionKey } from 'vue'
import FirestoreService from '@/services/FirestoreService'

export interface State {
  companionStatus: string
  gameData: unknown
  predictions: Array<unknown>
  result: unknown
  user: any
}

export const key: InjectionKey<Store<State>> = Symbol()

export default createStore<State>({
  state: {
    companionStatus: '',
    gameData: {
      player1: {
        health_status: 1,
        nades: [],
        kevlar: null,
        weapon: null,
      },
      player2: {
        health_status: 1,
        nades: [],
        kevlar: null,
        weapon: null,
      },
      player3: {
        health_status: 1,
        nades: [],
        kevlar: null,
        weapon: null,
      },
      player4: {
        health_status: 1,
        nades: [],
        kevlar: null,
        weapon: null,
      },
      player5: {
        health_status: 1,
        nades: [],
        kevlar: null,
        weapon: null,
      },
    },
    predictions: [],
    result: {},
    user: {
      id: '',
    },
  },
  mutations: {
    overwrite(state, payload) {
      state[payload.key] = payload.value
    },
  },
  getters: {
    companionStatus: (state) => {
      return state.companionStatus
    },
    predictions: (state) => {
      return state.predictions
    },
    getUser: (state) => {
      return state.user
    },
  },
  actions: {
    fetchCompanionStatus: async ({ commit }) => {
      try {
        const response = await FirestoreService.fetchUserData()
        const compLastOnlineTime = response.data().last_online.toDate().getTime()
        const currentTime = Date.now()
        const intervalTime = new Date(currentTime - 60000 * 0.1).getTime()
        commit('overwrite', {
          key: 'companionStatus',
          value:
            currentTime > compLastOnlineTime && compLastOnlineTime > intervalTime
              ? 'online'
              : 'offline',
        })
      } catch (error) {
        console.error(error)
      }
    },
    fetchGameDataById: async ({ commit }, gameDataId) => {
      try {
        const response = await FirestoreService.fetchGameDataById(gameDataId)
        const gameData = response.data()
        commit('overwrite', {
          key: 'gameData',
          value: gameData,
        })
      } catch (error) {
        console.error(error)
      }
    },
    fetchPredictions: async ({ commit }) => {
      try {
        const response = await FirestoreService.fetchPredictions()
        const predictions: Array<unknown> = []
        response.forEach((doc: any) => {
          predictions.push({
            id: doc.id,
            game_data_id: doc.data().game_data_id,
            map: doc.data().map,
            predicted_on: doc.data().predicted_on.toDate().toDateString(),
            prediction: doc.data().prediction,
            user_id: doc.data().user_id,
            round_type: doc.data().round_type,
          })
        })
        commit('overwrite', {
          key: 'predictions',
          value: predictions,
        })
      } catch (error) {
        console.error(error)
      }
    },
    setGetDataFlag: async () => {
      try {
        const response = await FirestoreService.setGetDataFlag(true)
        return response
      } catch (error) {
        console.error(error)
        throw error
      }
    },
    getPredictionForLatestGameData: async ({ commit }, parameters) => {
      try {
        const response = await FirestoreService.getPredictionForLatestGameData(
          parameters.gameDataId,
          parameters.map,
          parameters.userId
        )
        const resultResponse = await FirestoreService.fetchResultById(response.id)
        commit('overwrite', {
          key: 'result',
          value: resultResponse.data(),
        })
        await new Promise((r) => setTimeout(r, 2000))
        return response.id
      } catch (error) {
        console.error(error)
      }
    },
    deleteResult: async ({ dispatch, commit }, resultId) => {
      try {
        const response = await FirestoreService.deleteResult(resultId)
        return response
      } catch (error) {
        console.error(error)
        throw error
      }
    },
  },
  modules: {},
})
