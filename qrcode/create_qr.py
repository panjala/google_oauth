#from qrtools import QR
import png

import pyqrcode,qrcode
add='panja'
     
url =  big_code = pyqrcode.create(add)
url.png("horn.png", scale=6)
print(url.terminal(quiet_zone=1))

'''import qrtools
qr = qrtools.QR()
qr.decode("horn.png")
print qr.data'''
