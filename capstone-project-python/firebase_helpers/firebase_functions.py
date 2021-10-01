import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import time
import config
import pytz
import datetime
from typing import Dict, List
from proto.datetime_helpers import DatetimeWithNanoseconds

db = None


def init_firebase() -> None: # pragma: no cover
    """
    Initialize firebase app
    :return: None
    """
    cred = credentials.Certificate(
        './helper_modules/capstone-project-pweber-firebase-adminsdk-irp8n-a826099684.json'
    )
    firebase_admin.initialize_app(cred)

    user_ref = get_user_reference()
    user_watch = user_ref.on_snapshot(_on_snapshot)


def update_last_online() -> None: # pragma: no cover
    """
    Updates the last online time of the user on firestore
    :return: None
    """
    tz = pytz.timezone("Europe/Berlin")

    user_ref = get_user_reference()

    dateTimeObj = tz.localize(datetime.datetime.now())
    user_ref.update({u'last_online': dateTimeObj})


def get_user_reference() -> firestore.firestore.DocumentReference:
    """
    Returns the firestore user document reference
    :return: firestore user document reference
    """
    global db
    db = firestore.client()
    return db.collection(u'users').document(u'dev')


def _on_snapshot(doc_snapshot: firestore.firestore.DocumentSnapshot,
                 changes: List, read_time: DatetimeWithNanoseconds) -> None: # pragma: no cover
    """
    Callback function for firestore user document snapshot
    :param doc_snapshot: firestore user document snapshot
    :param changes: firestore user document changes
    :param read_time: firestore user document read time
    :return: None
    """
    for doc in doc_snapshot:
        if doc.to_dict(
        )['is_game_data_requested'] and config.is_game_data_requested == False:
            config.is_game_data_requested = True


def update_game_data(player_data: Dict) -> None: # pragma: no cover
    """
    Updates the game data on firestore
    :param player_data: player data
    :return: None
    """
    player_data['user_id'] = 'dev'
    docRef = db.collection('game_data').add(player_data)
    db.collection('users').document('dev').update({
        'is_game_data_requested':
        False,
        'last_game_data_id':
        docRef[1].id
    })
