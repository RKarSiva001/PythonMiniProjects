# install all the libraries needed
# create a function that collects a text and converts is to a qr code
# save the qr code as an image
# run the function

from re import T
import qrcode

def generateQRCode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

url = input("Enter your url : ")
generateQRCode(url)