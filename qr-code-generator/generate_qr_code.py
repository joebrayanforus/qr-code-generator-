import qrcode
from PIL import Image

def create_qr_code(data, color="black", bgcolor="white", size=10, with_logo=False):
    if not data:
        data = "https://example.com"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color=bgcolor).convert("RGB")

    if with_logo:
        try:
            logo = Image.open("logo.png.jpeg")
            basewidth = img.size[0] // 4
            wpercent = (basewidth / float(logo.size[0]))
            hsize = int((float(logo.size[1]) * float(wpercent)))
            logo = logo.resize((basewidth, hsize), Image.LANCZOS)

            pos = ((img.size[0] - logo.size[0]) // 2,
                   (img.size[1] - logo.size[1]) // 2)
            img.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)
        except Exception as e:
            print("⚠️ Logo konnte nicht eingefügt werden:", e)

    return img



