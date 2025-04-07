# 📊 Logiciel de Recherche Multi-Utilisateurs

Ce projet permet à plusieurs utilisateurs (comme Ludovic ou Martin) de déposer leur propre liste Excel sur un serveur, puis de rechercher dynamiquement dans toutes les données combinées via une interface graphique.

---

## 🔧 Fonctionnalités

- ✅ Upload de fichier Excel utilisateur (`uploader.py`)
- ✅ Recherche dans les listes via une interface Tkinter (`recherche.py`)
- ✅ API Flask hébergée sur Render (`api.py`)
- ✅ Multi-utilisateurs : chaque personne a sa propre liste, non écrasée
- ✅ Support des filtres : Année, Modèle, Heures

---

## 🚀 Utilisation

### 1. Déployer l’API

Ce projet est conçu pour être déployé sur [Render.com](https://render.com).  
Fichier principal : `api.py`  
Nécessite le fichier `requirements.txt`

API rendue accessible sur :
