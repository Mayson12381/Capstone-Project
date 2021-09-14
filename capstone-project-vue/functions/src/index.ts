import * as functions from "firebase-functions";

/* 
predictionObject: {
  gameDataObject
  parametersObject
}

gameDataObject: {
  mapString
  player1Object
  player2Object
  player3Object
  player4Object
  player5Object
  userIdString
}
*/

export const getPrediction = functions.https.onRequest((request, response) => {
  functions.logger.info("Get Prediction triggered", {structuredData: true});
  response.send("Hello from prediction!");
});

export const getGameData = functions.https.onRequest((request, response) => {
  functions.logger.info("Get Game Data triggered", {structuredData: true});
  response.send("Hello from gamedata!");
});
