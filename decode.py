from Crypto.Cipher import AES
import base64
import pyqrcode
import qrtools


path = input("Enter the path of the qr")
qr = qrtools.QR()
qr.decode(path)
msg = qr.data
key = input("Enter the secret key")
secret_key = key
cipher = AES.new(secret_key,AES.MODE_ECB)
decoded = cipher.decrypt(base64.b64decode(msg))
print (decoded.strip())

