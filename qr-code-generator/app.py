import os
import io
from flask import Flask, render_template, request, send_file
from generate_qr_code import create_qr_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.get("data")
        color = request.form.get("color", "black")
        bgcolor = request.form.get("bgcolor", "white")
        size = int(request.form.get("size", 10))
        with_logo = request.form.get("with_logo") == "on"

        qr_img = create_qr_code(data, color, bgcolor, size, with_logo)

        img_bytes = io.BytesIO()
        qr_img.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        return send_file(
            img_bytes,
            mimetype="image/png",
            as_attachment=True,
            download_name="qr_code.png"
        )

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


