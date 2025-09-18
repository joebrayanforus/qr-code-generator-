import qrcode

def generate_qr_code(data, filename):
    # Crée un objet QRCode avec des paramètres personnalisés
    qr = qrcode.QRCode(
        version=1,  # Taille du QR code (1 à 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur
        box_size=10,  # Taille de chaque carré
        border=4,  # Bordure autour du QR code
    )
    
    # Ajoute les données à encoder
    qr.add_data(data)
    qr.make(fit=True)

    # Génère l'image du QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Sauvegarde l'image dans un fichier
    img.save(filename)
    print(f"✅ QR code généré et enregistré sous : {filename}")

# Exemple d'utilisation
generate_qr_code("https://www.instagram.com", "example.png")