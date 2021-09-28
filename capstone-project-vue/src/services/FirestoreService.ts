import firebase from 'firebase'

const db = firebase.firestore()
let lastGameDataId = ''

db.collection('users')
  .doc('dev')
  .onSnapshot((doc: any) => {
    if (lastGameDataId !== doc.data().last_game_data_id) {
      lastGameDataId = doc.data().last_game_data_id
    }
  })

export default {
  fetchUserData(): any {
    return db
      .collection('users')
      .doc('dev')
      .get()
      .catch((error) => {
        console.error('Error fetching users: ', error)
      })
  },
  fetchGameDataById(gameDataId: string): any {
    return db
      .collection('game_data')
      .doc(gameDataId)
      .get()
      .catch((error) => {
        console.error('Error fetching game data: ', error)
      })
  },
  fetchResultById(resultId: string): any {
    return db
      .collection('results')
      .doc(resultId)
      .get()
      .catch((error) => {
        console.error('Error fetching result: ', error)
      })
  },
  fetchPredictions(): any {
    return db
      .collection('results')
      .where('user_id', '==', 'dev')
      .orderBy('predicted_on', 'desc')
      .get()
      .catch((error) => {
        console.error('Error fetching predictions: ', error)
      })
  },
  setGetDataFlag(value: boolean): any {
    const userRef = db.collection('users').doc('dev')
    return userRef.update({ is_game_data_requested: value }).catch((error) => {
      console.error('Error updating user get data flag: ', error)
    })
  },
  getPredictionForLatestGameData(gameDataId: string, map: string, userId: string): any {
    const buy_types = ['full', 'half', 'force', 'eco']
    return db.collection('results').add({
      game_data_id: gameDataId,
      map: map,
      predicted_on: firebase.firestore.Timestamp.now(),
      prediction: {
        A: Math.round(Math.random() * 100),
        B: Math.round(Math.random() * 100),
      },
      round_type: buy_types[Math.floor(Math.random() * buy_types.length)],
      user_id: userId,
    })
  },
  deleteResult(resultId: string): any {
    return db
      .collection('results')
      .doc(resultId)
      .delete()
      .catch((error) => {
        console.error('Error deleting result: ', error)
      })
  },
}
