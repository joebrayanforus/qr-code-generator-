import os
import qrcode
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
qr_folder = os.path.join(app.static_folder, 'qr_codes')
os.makedirs(qr_folder, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('data')
        if data:
            filename = f"{data.replace('https://', '').replace('/', '_')}.png"
            filepath = os.path.join(qr_folder, filename)
            generate_qr_code(data, filepath)
            return redirect(url_for('index'))

    qr_files = [f for f in os.listdir(qr_folder) if f.endswith('.png')]
    return render_template('index.html', qr_files=qr_files)

@app.route('/delete/<filename>', methods=['POST'])
def delete_qr(filename):
    filepath = os.path.join(qr_folder, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect(url_for('index'))

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == '__main__':
    app.run(debug=True)
