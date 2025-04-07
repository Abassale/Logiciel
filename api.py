from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🔹 Envoi du fichier Excel d'un utilisateur
@app.route('/upload/<username>', methods=['POST'])
def upload_file(username):
    if 'file' not in request.files:
        return 'Aucun fichier fourni', 400

    file = request.files['file']
    filename = f"{username}.xlsx"
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)
    return f"Fichier de {username} reçu avec succès", 200

# 🔹 Lecture de la liste d'un utilisateur
@app.route('/data/<username>', methods=['GET'])
def get_user_data(username):
    path = os.path.join(UPLOAD_FOLDER, f"{username}.xlsx")
    if not os.path.exists(path):
        return jsonify([])
    df = pd.read_excel(path)
    df["__provenance"] = username  # pour identifier la source
    return df.to_json(orient='records')

# 🔹 Lecture de toutes les listes fusionnées
@app.route('/data', methods=['GET'])
def get_all_data():
    all_data = []
    for file in os.listdir(UPLOAD_FOLDER):
        if file.endswith('.xlsx'):
            username = file.replace('.xlsx', '')
            df = pd.read_excel(os.path.join(UPLOAD_FOLDER, file))
            df["__provenance"] = username
            all_data.append(df)
    if all_data:
        fusion = pd.concat(all_data, ignore_index=True)
        return fusion.to_json(orient='records')
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
