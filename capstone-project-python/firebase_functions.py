import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import time
import config
import pytz
import datetime


db = None


def init_firebase():
    cred = credentials.Certificate(
        './capstone-project-pweber-firebase-adminsdk-irp8n-a826099684.json')
    firebase_admin.initialize_app(cred)

    user_ref = get_user_reference()
    user_watch = user_ref.on_snapshot(_on_snapshot)


def update_last_online():
    tz = pytz.timezone("Europe/Berlin")

    user_ref = get_user_reference()

    dateTimeObj = tz.localize(datetime.datetime.now())
    user_ref.update({u'last_online': dateTimeObj})


def get_user_reference():
    global db
    db = firestore.client()
    return db.collection(u'users').document(u'dev')


def _on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        if doc.to_dict()['is_game_data_requested'] and config.is_game_data_requested == False:
            config.is_game_data_requested = True


def update_game_data(player_data):
    # data = {
    #     'player1': {
    #         'Weapon': 'AK',
    #     },
    #     'player2': {
    #         'Weapon': 'AK',
    #     },
    #     'player3': {
    #         'Weapon': 'AK',
    #     },
    #     'player4': {
    #         'Weapon': 'AK',
    #     },
    #     'player5': {
    #         'Weapon': 'AK',
    #     },
    #     'user_id': 'dev'
    # }
    player_data['user_id'] = 'dev'
    player_data['map'] = 'inferno'
    docRef = db.collection('game_data').add(player_data)
    db.collection('users').document('dev').update({
        'is_game_data_requested':
        False,
        'last_game_data_id':
        docRef[1].id
    })
