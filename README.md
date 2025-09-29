# 📱 QR-Code-Generator – Webanwendung mit Flask

---
![Screenshot der Anwendung](https://github.com/user-attachments/assets/ffd64533-a85a-476e-b906-2f0b2b6d0d2f)

## 🧠 **Projektübersicht**

**Projekttitel**: QR-Code-Generator  
**Technologien**: Python · Flask · qrcode · HTML/CSS · Render

Dieses Projekt demonstriert die Entwicklung einer nativen Webanwendung zur Erstellung von QR-Codes. Ziel ist es, die Fähigkeit zur Umsetzung von Webprojekten mit Python und Flask zu zeigen – inklusive Frontend-Design, Serverlogik, Deployment und Fehlerbehandlung.

---

## 🎯 **Projektziele**

1. Entwicklung einer benutzerfreundlichen Weboberfläche zur QR-Code-Erstellung  
2. Integration von Flask zur Verwaltung von Routen und Formularen  
3. Nutzung der `qrcode`-Bibliothek zur Generierung von QR-Codes  
4. Bereitstellung von Funktionen zum Download und Löschen von QR-Codes  
5. Deployment der Anwendung auf Render mit stabiler Konfiguration

---

## 🛠️ **Technologien & Tools**

| Technologie     | Zweck                                 |
|----------------|----------------------------------------|
| Python & Flask | Backend-Logik und Routing              |
| qrcode         | QR-Code-Erstellung                     |
| Pillow         | Bildverarbeitung                       |
| HTML/CSS       | Benutzeroberfläche und Design          |
| Gunicorn       | WSGI-Server für Deployment              |
| Render         | Hosting der Anwendung                  |

---

## 📁 **Projektstruktur**

```bash
qr-code-generator/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   ├── logo.png
│   └── qr_codes/

🚀 Installation & Ausführung
bash
git clone https://github.com/joebrayanforus/qr-code-generator-.git

cd qr-code-generator-

pip install -r requirements.txt

python app.py
Dann öffne http://127.0.0.1:5000 im Browser.

🔗 Live-Version: qr-code-generator-m3dc.onrender.com

📸 Screenshot
html
![Screenshot der Anwendung](static/screenshot.png)

(Stelle sicher, dass screenshot.png im Ordner static/ liegt.)

🔄 Funktionen im Detail
🔤 Texteingabe oder URL-Eingabe über Webformular

🖼️ Sofortige QR-Code-Erstellung mit Vorschau

📥 Download als PNG-Datei

🗑️ Löschen generierter QR-Codes

🎨 Modernes Design mit CSS-Animationen und Google Fonts

📱 Responsive für Desktop und Mobile

🧩 Technische Herausforderungen & Lösungen
Problem	Lösung
UnicodeDecodeError beim Deployment	Umstellung auf DSN-Verbindung mit UTF-8-Encoding
Flask-App startet nicht lokal	Einrichtung eines sauberen venv, Anpassung der PowerShell-Richtlinien
404-Fehler auf Render	Korrektur der render.yaml und Konfiguration des Startbefehls mit Gunicorn
QR-Code wird nicht angezeigt	Pfadkorrektur und dynamische Dateibenennung im static/qr_codes-Ordner
📦 Abhängigkeiten
txt
Flask  
qrcode  
Pillow  
Gunicorn
📣 Autor & Lizenz
Erstellt von Joebrayan Forus, Informatikstudent an der Universität Siegen. Lizenz: MIT – frei zur Nutzung und Erweiterung mit Namensnennung.
