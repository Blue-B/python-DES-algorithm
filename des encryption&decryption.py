from Crypto.Cipher import DES
from secrets import *
key = token_bytes(8)

text='안녕하세요'
cipher = DES.new(key, DES.MODE_EAX)
nonce = cipher.nonce
print(f'nonce:{nonce}')
ciphertext,tag=cipher.encrypt_and_digest(text.encode('utf-8'))

print(f'암호문:{ciphertext}')


cipher = DES.new(key,DES.MODE_EAX,nonce=nonce)
plaintext= cipher.decrypt(ciphertext).decode('utf-8')
print(f'평문:{plaintext}')
