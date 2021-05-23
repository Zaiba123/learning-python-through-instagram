import pyqrcode
import png
from pyqrcode import QRCode

s= "https://zaiba.netlify.app/"

url= pyqrcode.create(s)

url.svg("zaiba.svg",scale=8)
url.png('zaiba.png', scale = 6)
