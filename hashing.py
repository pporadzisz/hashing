import random, string
import base64
from hashlib import pbkdf2_hmac
import codecs

class Hashing:

    @staticmethod
    def createHash (password=None, salt=None, iterations=100):
        if not salt:
            salt = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        salt_bytes = salt.encode('utf-8')
        salt_base64_bytes = base64.b64encode(salt_bytes)
        if not password:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        password_bytes = password.encode('utf-8')
        password_base64_bytes = base64.b64encode(password_bytes)
        dk = pbkdf2_hmac('sha512',password_bytes , salt_bytes, iterations)
        base64_bytes = base64.b64encode(dk)
        base64_message = base64_bytes.decode('utf-8')
        combined=f'{salt_base64_bytes.decode("utf-8") }:100:{base64_message }'
        return (password,salt,username,combined)
