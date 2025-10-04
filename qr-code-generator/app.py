import os
import io
import base64
from flask import Flask, render_template, request
from generate_qr_code import create_qr_code

app = Flask(__name__)

# Speicher für QR-Codes (Liste aus {img, text})
generated_qrs = []

@app.route("/", methods=["GET", "POST"])
def index():
    global generated_qrs
    if request.method == "POST":
        data = request.form.get("data")
        color = request.form.get("color", "black")
        bgcolor = request.form.get("bgcolor", "white")
        size = int(request.form.get("size", 10))
        with_logo = request.form.get("with_logo") == "on"

        # QR-Code generieren
        qr_img = create_qr_code(data, color, bgcolor, size, with_logo)

        # In Base64 umwandeln
        img_bytes = io.BytesIO()
        qr_img.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        encoded_img = base64.b64encode(img_bytes.read()).decode('utf-8')
        img_data = f"data:image/png;base64,{encoded_img}"

        # Neuen QR speichern
        generated_qrs.insert(0, {"img": img_data, "text": data})

    return render_template("index.html", generated_qrs=generated_qrs)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
