import random, string
import base64
from hashlib import pbkdf2_hmac

class Hashing:

    @staticmethod
    def createHash (password=None, salt=None, iterations=100):
        if iterations<100:
            raise Exception("Iterations - value cannot be less than 100.")

        if salt is None:
            salt = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        elif len(salt)<32:
            raise Exception("Salt - value cannot be shorter than 32 characters.")

        salt_bytes = salt.encode('utf-8')
        salt_base64_bytes = base64.b64encode(salt_bytes)

        if password is None:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        elif len(password)<20:
                print('dsdsd')
                raise Exception("Password - value canot be shorter than 20 characters.")

        password_bytes = password.encode('utf-8')

        dk = pbkdf2_hmac('sha512',password_bytes , salt_bytes, iterations)
        base64_bytes = base64.b64encode(dk)
        base64_message = base64_bytes.decode('utf-8')

        username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        combined=f'{salt_base64_bytes.decode("utf-8") }:100:{base64_message }'
        return (password,salt,username,combined)
