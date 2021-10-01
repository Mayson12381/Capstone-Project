import unittest
from firebase_helpers.firebase_functions import get_user_reference, init_firebase
from firebase_helpers.firebase_authentication import _sign_in_with_email_and_password, login_user
from firebase_admin import firestore
from typing import Dict


class TestFirebaseFunctions(unittest.TestCase):
    def setUp(self):
        try:
            init_firebase()
        except:
            pass

    def test_get_user_reference(self):
        """
        Test that the get_user_reference function returns a valid reference
        """
        user_reference = get_user_reference()
        self.assertIsInstance(user_reference, firestore.DocumentReference)
        user_reference = get_user_reference()
        self.assertIsInstance(user_reference,
                              firestore.firestore.DocumentReference)


class TestFirebaseAuthentication(unittest.TestCase):
    def setUp(self):
        try:
            init_firebase()
        except:
            pass

    def test_sign_in_with_email_and_password(self):
        """
        Test that the sign_in_with_email_and_password function returns a valid id and has correct type
        """
        response = _sign_in_with_email_and_password('dev@capstone.com',
                                                   'Passw0rd!')
        self.assertIsInstance(response, Dict)
        self.assertEqual(response['localId'], 'xfWy9Jk3J7PGc8AqYZXRBKSsghQ2')

    def test_login_user(self):
        """
        Test that the login_user function logs in the user
        """
        response = login_user('dev@capstone.com', 'Passw0rd!')
        self.assertEqual(response, True)

    def test_login_user_wrong_email(self):
        """
        Test that the login_user function returns false if the email is wrong
        """
        response = login_user('dev-wrong@capstone.com', 'Passw0rd!')
        self.assertEqual(response, False)

    def test_login_user_wrong_password(self):
        """
        Test that the login_user function returns false if the password is wrong
        """
        response = login_user('dev@capstone.com', 'wrong')
        self.assertEqual(response, False)
