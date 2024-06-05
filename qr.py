from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_H, ERROR_CORRECT_Q

class MyQrCode:
    def __init__(self) -> None:
        self.version = 3
        self.box_size = 20
        self.border = 10
        self.QR = QRCode(
            version=self.version,
            box_size=self.box_size,
            border=self.border,
            error_correction=ERROR_CORRECT_M)
        
    def get_qr(self) -> QRCode:
        """ returns qrcode object """
        return self.QR

    def add_data(self, data: str):
        self.QR.add_data(data)

    def generate(self):
        ''' generate or make the QR '''
        self.QR.make(fit=True)

        image = self.QR.make_image(fill_color="black", back_color="white")

        # image.save("")
        # TODO: add logic to return an image and display in the API call
