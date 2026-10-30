# Logiciel de recherche multi-utilisateurs — prototype Excel / Python

Projet Python permettant d'envoyer des classeurs Excel sur une API Flask, puis de consulter et filtrer les lignes avec une interface locale Tkinter.

> **État : prototype, non sécurisé pour un accès public.** Les routes de lecture et d'import sont actuellement accessibles sans authentification applicative. Ne pas l'exposer sur Internet avec des données privées avant refonte des contrôles d'accès.

## Arborescence

| Fichier | Rôle |
| --- | --- |
| [api.py](api.py) | API Flask : import `/upload/<username>`, lecture `/data` et `/data/<username>` |
| [Recherche.py](Recherche.py) | Interface Tkinter de recherche (respecter la casse du nom de fichier) |
| [uploader.py](uploader.py) | Client Python d'envoi d'un classeur Excel |
| [requirements.txt](requirements.txt) | Dépendances Flask, pandas, openpyxl, requests |
| `liste.xlsx` | Classeur actuellement versionné ; vérifier qu'il ne contient aucune donnée confidentielle |

## Installation

```bash
python -m venv .venv
# Activer l'environnement virtuel
pip install -r requirements.txt
```

En environnement local de test :

```bash
python api.py
```

Dans un autre terminal, vérifier et adapter l'adresse d'API utilisée dans `uploader.py` et `Recherche.py`, puis :

```bash
python uploader.py
python Recherche.py
```

**Attention :** les deux clients sont actuellement configurés pour contacter un endpoint Render, et non l'API locale ; vérifier l'adresse avant de les exécuter. Le serveur utilise un dossier `uploads/` pour les classeurs envoyés.

## Avant tout déploiement

- Ajouter une vraie authentification et une autorisation par utilisateur ; ne pas se fier au nom d'utilisateur passé dans les URL.
- Restreindre CORS, les chemins d'accès et la taille / nature des fichiers téléversés.
- Éviter tout stockage de classeurs utilisateurs dans un dépôt public ; vérifier également l'historique Git.
- Conserver les secrets hors du dépôt et procéder à des tests d'accès non autorisé avant mise en production.

Les modifications de documentation et de dépendances ne constituent pas une validation fonctionnelle ou de sécurité.
