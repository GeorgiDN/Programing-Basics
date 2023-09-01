import pyqrcode

import png
from pyqrcode import QRCode

address = 'https://www.youtube.com/watch?v=n7HibvOu_lQ'
url = pyqrcode.create(address)
url.png('test.png', scale=8)
