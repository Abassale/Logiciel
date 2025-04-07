import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import io
import sys

API_BASE = "https://logiciel-wtq9.onrender.com"

# Récupérer la liste complète ou filtrée par utilisateur
def charger_donnees(username=None):
    try:
        if username == "Tous":
            url = f"{API_BASE}/data"
        else:
            url = f"{API_BASE}/data/{username.lower()}"
        response = requests.get(url)
        response.raise_for_status()
        return pd.read_json(io.StringIO(response.text))
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur de chargement : {e}")
        sys.exit()

# Interface principale
app = tk.Tk()
app.title("🔍 Recherche Excel (multi-utilisateurs)")
app.geometry("850x600")
app.configure(bg="#f0f4f7")

utilisateurs = ["Tous", "martin", "ludovic"]
selected_user = tk.StringVar(value="Tous")
df = charger_donnees(selected_user.get())

def rechercher():
    global df
    annee = entree_annee.get().strip()
    modele = entree_modele.get().strip().lower()
    heures = entree_heures.get().strip()

    resultats = df.copy()

    if annee:
        try:
            resultats = resultats[resultats['Années'] == int(annee)]
        except:
            messagebox.showwarning("⚠️", "L'année doit être un nombre entier.")
            return

    if modele:
        resultats = resultats[resultats['Modèles'].str.lower().str.contains(modele, na=False)]

    if heures:
        try:
            resultats = resultats[resultats['Heures'] == int(heures)]
        except:
            messagebox.showwarning("⚠️", "Les heures doivent être un nombre entier.")
            return

    tree.delete(*tree.get_children())
    for _, row in resultats.iterrows():
        tree.insert("", "end", values=list(row))

def reinitialiser():
    entree_annee.delete(0, tk.END)
    entree_modele.delete(0, tk.END)
    entree_heures.delete(0, tk.END)
    rechercher()

def changer_utilisateur(*args):
    global df
    df = charger_donnees(selected_user.get())
    rechercher()

# Choix utilisateur
frame_top = tk.Frame(app, bg="#f0f4f7")
frame_top.pack(pady=10)
tk.Label(frame_top, text="Source :", bg="#f0f4f7").pack(side="left", padx=5)
menu_utilisateur = ttk.Combobox(frame_top, values=utilisateurs, textvariable=selected_user, state="readonly")
menu_utilisateur.pack(side="left")
menu_utilisateur.bind("<<ComboboxSelected>>", changer_utilisateur)

# Recherche
cadre_recherche = tk.LabelFrame(app, text="Critères de recherche", bg="#f0f4f7", font=("Arial", 12, "bold"))
cadre_recherche.pack(padx=20, pady=10, fill="x")

label_annee = tk.Label(cadre_recherche, text="Année", bg="#f0f4f7")
label_annee.grid(row=0, column=0, padx=5, pady=10)
entree_annee = tk.Entry(cadre_recherche)
entree_annee.grid(row=0, column=1, padx=5, pady=10)

label_modele = tk.Label(cadre_recherche, text="Modèle", bg="#f0f4f7")
label_modele.grid(row=0, column=2, padx=5, pady=10)
entree_modele = tk.Entry(cadre_recherche)
entree_modele.grid(row=0, column=3, padx=5, pady=10)

label_heures = tk.Label(cadre_recherche, text="Heures", bg="#f0f4f7")
label_heures.grid(row=0, column=4, padx=5, pady=10)
entree_heures = tk.Entry(cadre_recherche)
entree_heures.grid(row=0, column=5, padx=5, pady=10)

btn_rechercher = tk.Button(cadre_recherche, text="🔍 Rechercher", command=rechercher, bg="#4CAF50", fg="white")
btn_rechercher.grid(row=0, column=6, padx=10)

btn_reset = tk.Button(cadre_recherche, text="♻️ Réinitialiser", command=reinitialiser, bg="#f44336", fg="white")
btn_reset.grid(row=0, column=7, padx=10)

# Résultats
cadre_resultats = tk.LabelFrame(app, text="Résultats", bg="#f0f4f7", font=("Arial", 12, "bold"))
cadre_resultats.pack(padx=20, pady=10, fill="both", expand=True)

tree = ttk.Treeview(cadre_resultats, columns=["Années", "Modèles", "Heures", "__provenance"], show="headings")
for col in ["Années", "Modèles", "Heures", "__provenance"]:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(expand=True, fill="both")

rechercher()
app.mainloop()
