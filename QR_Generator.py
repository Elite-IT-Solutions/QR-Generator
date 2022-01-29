import pyqrcode


class QR_Generator:
    def __init__(self, url, scale):
        self.url = url
        self.scale = scale
        self.generate()

    def generate(self):
        code = pyqrcode.create(self.url)
        code.svg('myQR.svg', scale=self.scale)


QR_Generator('https://github.com/Elite-IT-Solutions', 10)
