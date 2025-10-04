import os
import io
import base64
from flask import Flask, render_template, request, jsonify, send_file
from generate_qr_code import create_qr_code

app = Flask(__name__)

# Speicher für QR-Codes (Liste von Dictionnaries)
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

        qr_img = create_qr_code(data, color, bgcolor, size, with_logo)

        # Base64 kodieren
        img_bytes = io.BytesIO()
        qr_img.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        encoded_img = base64.b64encode(img_bytes.read()).decode("utf-8")
        img_data = f"data:image/png;base64,{encoded_img}"

        generated_qrs.insert(0, {"id": len(generated_qrs) + 1, "img": img_data, "text": data})

    return render_template("index.html", generated_qrs=generated_qrs)

@app.route("/delete/<int:qr_id>", methods=["POST"])
def delete_qr(qr_id):
    global generated_qrs
    generated_qrs = [qr for qr in generated_qrs if qr["id"] != qr_id]
    return jsonify({"success": True})

@app.route("/download/<int:qr_id>")
def download_qr(qr_id):
    for qr in generated_qrs:
        if qr["id"] == qr_id:
            img_data = qr["img"].split(",")[1]
            img_bytes = io.BytesIO(base64.b64decode(img_data))
            return send_file(img_bytes, mimetype="image/png", as_attachment=True, download_name=f"qr_{qr_id}.png")
    return "QR not found", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

