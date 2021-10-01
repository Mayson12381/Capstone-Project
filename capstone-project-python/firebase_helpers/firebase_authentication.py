import requests
import json

FIREBASE_WEB_API_KEY = f'AIzaSyC7pLo35rF3kV7v12MXjQ7GGK6gAJb7WsM'
rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"


def _sign_in_with_email_and_password(email: str,
                                    password: str,
                                    return_secure_token: bool = True):
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": return_secure_token
    })

    r = requests.post(rest_api_url,
                      params={"key": FIREBASE_WEB_API_KEY},
                      data=payload)

    return r.json()



def login_user(user: str, password: str):
    token = _sign_in_with_email_and_password(user, password)
    try:
        token['registered']
        return True
    except KeyError:
        return False