import qrcode
import os

def generate_qr(data):
    folder_path = "accounts/qr"
    os.makedirs(folder_path, exist_ok=True)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(folder_path, f"{data}.png"))
