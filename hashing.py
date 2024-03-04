"""Module providing a function create password, salt, username, combined string """
import random
import string
import base64
from hashlib import pbkdf2_hmac

class Hashing:
    """Class representing a hashing"""
    @staticmethod
    def check_data( password=None, salt=None, iterations=100):
        """Check data method """
        if iterations<100:
            raise ValueError("Iterations - value cannot be less than 100.")

        if salt is None:
            salt = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        elif len(salt)<32:
            raise ValueError("Salt - value cannot be shorter than 32 characters.")

        if password is None:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        elif len(password)<20:
            print('dsdsd')
            raise ValueError("Password - value canot be shorter than 20 characters.")
        return (password,salt,iterations)

    @staticmethod
    def create_hash (password=None, salt=None, iterations=100):
        """Create Hash method """
        (password,salt,iterations) = Hashing.check_data(password,salt,iterations)

        salt_bytes = salt.encode('utf-8')
        salt_base64_bytes = base64.b64encode(salt_bytes)

        password_bytes = password.encode('utf-8')

        dk = pbkdf2_hmac('sha512',password_bytes , salt_bytes, iterations)
        base64_bytes = base64.b64encode(dk)
        base64_message = base64_bytes.decode('utf-8')

        username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        combined=f'{salt_base64_bytes.decode("utf-8") }:100:{base64_message }'

        return (password,salt,username,combined)
