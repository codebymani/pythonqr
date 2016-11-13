from Crypto.Cipher import AES
import base64
import pyqrcode
from qrtools import QR


path = input("Enter the path of the qr")
qr = QR("qrimg.png")
qr.decode()
emsg = qr.data
msg = emsg.rjust(16)
key = input("Enter the secret key")
secret_key = key.rjust(16)
cipher = AES.new(secret_key,AES.MODE_ECB)
decoded = cipher.decrypt(base64.b64decode(msg))
print (decoded.strip())

