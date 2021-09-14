import { ComponentCustomProperties } from 'vue'
import { Store } from 'vuex'

declare module '@vue/runtime-core' {
  interface State {
    companionStatus: string;
    gameData: any;
    predictions: any;
    result: any;
  }

  interface Actions {
    fetchCompanionStatus: string;
    setGetDataFlag: string;
    fetchGameDataById: string;
    fetchPredictions: string;
    getPredictionForLatestGameData: void;
  }

  interface Getters {
    companionStatus: string;
    gameData: any;
  }
  
  interface ComponentCustomProperties {
    $store: Store<State, Actions>
  }
}