from requirements import *
while True:
    print('')
    print('welcome to cryptogrphy tool')
    print('')
    print('1. encrypt')
    print('2. decrypt')
    print('0. exit')

    usrinput = int(input(': '))

    if usrinput == 0:
        exit()
    elif usrinput == 1 or usrinput == 2:
        key = str(input('enter key: '))
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
                print('invalid byte text')

    else:
        print('enter valid selection')

    