
import cryptography
import base64
from werkzeug.security import generate_password_hash, check_password_hash
from crypt import methods
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from crypt import methods
from hashlib import sha256




print('welcome to cryptogrphy tool')
print('1. encrypt')
print('2. decrypt')

usrinput = int(input(': '))


key = str(input('enter key: '))
key1 = key
text = str(input('enter text: '))


password = key.encode()  # Convert to type bytes
salt = b"\x00\xe2q\xaf\xb9[\xa2~\xe5 \xc4\xef<h'\xc7"
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
f = Fernet(key)

if usrinput == 1:

    # encrypt
    text = text.encode()
# Encrypt the bytes. The returning object is of type bytes
    encrypted = f.encrypt(text)
    print(encrypted)



if usrinput == 2:
    # decrypt
    if text.startswith("b'"):
        decrypt = eval(text)
        # Decrypt the bytes. The returning object is of type bytes
        decrypted = f.decrypt(decrypt).decode()
        print(decrypted)
  

    else:
        error_statement = "cannot decrypt text"
