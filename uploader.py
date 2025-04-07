import requests

# 🔧 Nom d'utilisateur toujours en minuscules
username = input("Nom d'utilisateur (ex: martin, ludovic) : ").strip().lower()

# 📄 Fichier Excel à envoyer
fichier_excel = "liste.xlsx"

# 🌐 API en ligne via Render
url = f"https://logiciel-wtq9.onrender.com/upload/{username}"

try:
    with open(fichier_excel, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
        response.raise_for_status()
        print(f"✅ Fichier envoyé avec succès pour {username} :", response.text)
except FileNotFoundError:
    print("❌ Fichier 'liste.xlsx' introuvable.")
except requests.exceptions.RequestException as e:
    print("❌ Erreur lors de l'envoi :", e)
