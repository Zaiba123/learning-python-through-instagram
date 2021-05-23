import pyqrcode
import png
from pyqrcode import QRCode

s= "https://zaiba.netlify.app/"

url= pyqrcode.create(s)

url.svg("qrcode.svg",scale=8)
url.png('qrcode.png', scale = 6)
