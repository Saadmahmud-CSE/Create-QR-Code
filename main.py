import pyqrcode
from pyqrcode import QRCode

s = "https://www.linkedin.com/in/mohammad-saad-uddin-chowdhury-920850202/"

url = pyqrcode.create(s)

url.svg("mylinkedin.svg", scale=6)