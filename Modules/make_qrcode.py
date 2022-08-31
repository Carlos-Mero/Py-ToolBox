'''二维码,二维码'''
import qrcode

from main import Dir_Path

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1)

def main(a):
    qr.add_data(a)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("二维码.png")

if __name__ == '__main__':
    main(None)
