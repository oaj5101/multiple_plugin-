import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = input("Enter the website: ")

# Generate QR code
url = pyqrcode.create(s)

# Create and save the QR code
name = input("Enter the name for the file: ")
url.svg(name + ".svg", scale = 8)
