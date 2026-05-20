# 🩺 Prédiction du Risque de Mortalité Néonatale au Cameroun

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![EDS](https://img.shields.io/badge/Data-EDS%20Cameroun%202018-orange)](https://dhsprogram.com/)

> Application web interactive de prédiction du risque de mortalité néonatale basée sur les données de l'Enquête Démographique et de Santé (EDS) Cameroun 2018.

![Demo](https://img.shields.io/badge/Demo-En%20ligne-brightgreen)

---

## 📋 Table des matières

- [Aperçu](#-aperçu)
- [Fonctionnalités](#-fonctionnalités)
- [Architecture](#-architecture)
- [Installation locale](#-installation-locale)
- [Déploiement](#-déploiement)
  - [Streamlit Cloud (Gratuit)](#1-streamlit-cloud-recommandé)
  - [Render](#2-render)
  - [Heroku](#3-heroku)
  - [Docker](#4-docker)
- [Structure du projet](#-structure-du-projet)
- [Variables du modèle](#-variables-du-modèle)
- [Performance du modèle](#-performance-du-modèle)
- [Captures d'écran](#-captures-décran)
- [Auteurs](#-auteurs)
- [Citation](#-citation)
- [Licence](#-licence)

---

## 🎯 Aperçu

Cette application permet aux professionnels de santé d'évaluer le risque de mortalité néonatale d'un nouveau-né à partir de caractéristiques maternelles et obstétricales simples. Le modèle XGBoost (AUC-ROC = 0,695) a été entraîné sur **33 988 naissances** de l'EDS Cameroun 2018.

### Contexte scientifique

La mortalité néonatale au Cameroun est estimée à **31,8 décès pour 1 000 naissances vivantes** (EDS 2018). Les facteurs de risque identifiés incluent :
- Taille du bébé à la naissance (facteur dominant)
- Parité maternelle élevée
- Intervalle inter-génésique court
- Sexe masculin
- Contexte régional et socio-économique

---

## ✨ Fonctionnalités

- 🔮 **Prédiction en temps réel** : Probabilité de décès néonatal instantanée
- 📊 **Niveau de risque** : Classification Élevé / Modéré / Faible avec code couleur
- 📋 **Facteurs de risque identifiés** : Liste personnalisée selon le profil
- 🏥 **Recommandations cliniques** : Protocoles adaptés au niveau de risque
- 📱 **Interface responsive** : Design moderne avec CSS personnalisé
- 🎨 **Visualisations** : Jauge de risque, métriques interactives

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    STREAMLIT APP                            │
│  ┌─────────────┐    ┌─────────────────────────────────────┐ │
│  │   SIDEBAR   │    │           MAIN CONTENT              │ │
│  │             │    │                                     │ │
│  │  Inputs     │───▶│  • Header + Bannière                │ │
│  │  utilisateur│    │  • Prédiction du risque             │ │
│  │             │    │  • Métriques (probabilité, niveau)  │ │
│  │  Sliders    │    │  • Barre de progression             │ │
│  │  Selectbox  │    │  • Recommandations                  │ │
│  │             │    │  • Facteurs de risque               │ │
│  └─────────────┘    └─────────────────────────────────────┘ │
│                           │                                 │
│                    ┌──────┴──────┐                         │
│                    │  XGBOOST    │                         │
│                    │  MODEL      │                         │
│                    │  (.pkl)     │                         │
│                    └─────────────┘                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 💻 Installation locale

### Prérequis

- Python ≥ 3.9
- pip ou conda

### Étapes

1. **Cloner le repository**

```bash
git clone https://github.com/votre-username/neonatal-mortality-cameroon.git
cd neonatal-mortality-cameroon
```

2. **Créer un environnement virtuel (recommandé)**

```bash
# Avec venv
python -m venv venv

# Activation
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

4. **Lancer l'application**

```bash
streamlit run streamlit_app.py
```

5. **Ouvrir le navigateur**

L'application est accessible à l'adresse : `http://localhost:8501`

---

## 🚀 Déploiement

### 1. Streamlit Cloud (Recommandé - Gratuit)

Streamlit Cloud est la solution la plus simple et gratuite pour déployer une app Streamlit.

#### Prérequis
- Compte GitHub
- Compte Streamlit Cloud (gratuit sur [share.streamlit.io](https://share.streamlit.io))

#### Étapes

1. **Pousser le code sur GitHub**

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/votre-username/neonatal-mortality-cameroon.git
git push -u origin main
```

2. **Connecter Streamlit Cloud**
   - Aller sur [share.streamlit.io](https://share.streamlit.io)
   - Se connecter avec GitHub
   - Cliquer sur **"New app"**
   - Sélectionner le repository
   - Spécifier le fichier principal : `streamlit_app.py`
   - Cliquer sur **"Deploy"**

3. **Configuration avancée (optionnel)**

Créer un fichier `.streamlit/config.toml` :

```toml
[theme]
primaryColor = "#2a5298"
backgroundColor = "#f5f7fa"
secondaryBackgroundColor = "#ffffff"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
```

4. **Variables sensibles (si besoin)**

Créer un fichier `.streamlit/secrets.toml` (non poussé sur GitHub) :

```toml
# Exemple si vous utilisez une base de données
[database]
url = "postgresql://..."
```

> ⚠️ Ajoutez `.streamlit/secrets.toml` à votre `.gitignore` !

---

### 2. Render

Render offre un déploiement gratuit avec une meilleure disponibilité que Streamlit Cloud.

#### Étapes

1. Créer un compte sur [render.com](https://render.com)
2. Cliquer sur **"New Web Service"**
3. Connecter votre repository GitHub
4. Configurer :
   - **Runtime** : Python 3
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `streamlit run streamlit_app.py --server.port $PORT --server.headless true`
5. Cliquer sur **"Create Web Service"**

---

### 3. Heroku

> ⚠️ Heroku n'offre plus de tier gratuit depuis novembre 2022. Cette option nécessite un abonnement payant.

#### Fichier `Procfile`

```
web: streamlit run streamlit_app.py --server.port $PORT --server.headless true
```

#### Fichier `runtime.txt`

```
python-3.11.6
```

#### Déploiement

```bash
heroku create neonatal-mortality-cm
heroku config:set PYTHON_VERSION=3.11.6
git push heroku main
```

---

### 4. Docker

#### Fichier `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copie des fichiers
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exposition du port
EXPOSE 8501

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Commande de démarrage
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Fichier `.dockerignore`

```
__pycache__/
*.pyc
.env
venv/
.git/
.gitignore
README.md
```

#### Commandes Docker

```bash
# Build
docker build -t neonatal-mortality-app .

# Run
docker run -p 8501:8501 neonatal-mortality-app

# Push vers Docker Hub
docker tag neonatal-mortality-app votre-username/neonatal-mortality-app
docker push votre-username/neonatal-mortality-app
```

---

## 📁 Structure du projet

```
neonatal-mortality-cameroon/
│
├── 📄 streamlit_app.py          # Application principale Streamlit
├── 📄 requirements.txt          # Dépendances Python
├── 📄 README.md                 # Ce fichier
├── 📄 LICENSE                   # Licence MIT
│
├── 🗂️ .streamlit/
│   └── config.toml              # Configuration Streamlit (optionnel)
│
├── 🧠 best_neonatal_model.pkl   # Modèle XGBoost entraîné (à ajouter)
│
├── 🖼️ banner_neo.png            # Image bannière (optionnel)
│
├── 📁 data/                     # Données (optionnel, ne pas pousser sur Git)
│   └── neonatal_mortality_data.csv
│
├── 📁 notebooks/                # Notebooks d'analyse (optionnel)
│   ├── 01_eda.ipynb
│   ├── 02_modeling.ipynb
│   └── 03_evaluation.ipynb
│
└── 📁 src/                      # Scripts source (optionnel)
    ├── preprocessing.py
    ├── train_model.py
    └── evaluate_model.py
```

---

## 📊 Variables du modèle

| Variable | Type | Description | Valeurs |
|----------|------|-------------|---------|
| `maternal_age` | Numérique | Âge de la mère (ans) | 15 - 49 |
| `maternal_age_sq` | Numérique | Âge au carré (terme quadratique) | Calculé |
| `parity` | Numérique | Nombre d'enfants nés | 1 - 15 |
| `sex_child` | Catégorielle | Sexe du nouveau-né | Masculin, Feminin |
| `education` | Catégorielle | Niveau d'éducation | Aucun, Primaire, Secondaire, Superieur |
| `wealth` | Catégorielle | Quintile de richesse | Poorest, Poorer, Middle, Richer, Richest |
| `residence` | Catégorielle | Milieu de résidence | Urbain, Rural |
| `region` | Catégorielle | Région administrative | 12 régions du Cameroun |
| `baby_size` | Catégorielle | Taille perçue du bébé | Tres gros, Plus gros, Normal, Petit, Tres petit |
| `birth_interval` | Catégorielle | Intervalle inter-génésique | Premiere, <24 mois, 24-35 mois, >=36 mois |
| `anc_visits` | Catégorielle | Visites prénatales | Aucune, 1-3, 4-7, 8+, Missing |

---

## 📈 Performance du modèle

| Métrique | Valeur |
|----------|--------|
| **AUC-ROC** | **0,695** |
| F1-Score | ~0,15 |
| Accuracy | ~0,96 |
| Dataset d'entraînement | 27 190 naissances |
| Dataset de test | 6 798 naissances |
| Taux de mortalité | 3,23% |

> ⚠️ Le F1-Score est faible en raison du fort déséquilibre des classes (3,2% vs 96,8%). L'AUC-ROC constitue la métrique la plus fiable ici.

---

## 📸 Captures d'écran

### Interface principale
```
┌─────────────────────────────────────────────────────────────┐
│  🩺 Prédiction du Risque de Mortalité Néonatale             │
│  EDS Cameroun 2018 — Modèle Machine Learning XGBoost        │
├──────────────────┬──────────────────────────────────────────┤
│                  │                                          │
│  📋 Caractérist. │  🔮 Prédiction du Risque                 │
│                  │                                          │
│  Âge: [25]       │  [🔍 Analyser le Risque]                 │
│  Parité: [3]     │                                          │
│  Sexe: Masculin  │  ┌─────────────────────────────┐         │
│  Éducation: ...  │  │  ⚠️ RISQUE ÉLEVÉ            │         │
│  Richesse: ...   │  │  Surveillance immédiate     │         │
│  ...             │  └─────────────────────────────┘         │
│                  │                                          │
│  👶 Grossesse    │  ┌────────┬────────┬────────┐           │
│                  │  │ 12.3%  │ 🔴 ÉL. │ Tres   │           │
│  Taille: Normal  │  │ Proba. │ Risque │ petit  │           │
│  Intervalle: ... │  └────────┴────────┴────────┘           │
│  ANC: 4-7        │  [████████░░░░░░░░░░]                    │
│                  │                                          │
│                  │  📊 Facteurs de Risque Identifiés        │
│                  │  🔴 Taille très petite (OR=1,82)         │
│                  │  🟠 Parité élevée                        │
│                  │                                          │
└──────────────────┴──────────────────────────────────────────┘
```

---

## 👥 Auteurs

- **Votre Nom** - *Concepteur & Développeur* - [GitHub](https://github.com/votre-username)
- **Encadrant** - *Supervision académique*

### Contact

Pour toute question ou suggestion :
- 📧 Email : votre.email@exemple.com
- 🐛 Issues : [GitHub Issues](https://github.com/votre-username/neonatal-mortality-cameroon/issues)

---

## 📚 Citation

Si vous utilisez cette application ou ces données dans vos travaux, veuillez citer :

```bibtex
@misc{neonatal_mortality_cameroon_2024,
  title={Déterminants de la mortalité néonatale au Cameroun : 
         Approche mixte Régression Logistique et Machine Learning},
  author={Votre Nom},
  year={2024},
  publisher={GitHub},
  howpublished={\url{https://github.com/votre-username/neonatal-mortality-cameroon}}
}
```

### Sources de données

> Institut National de la Statistique (INS) et ICF. (2018). 
> *Enquête Démographique et de Santé du Cameroun 2018*. 
> Yaoundé, Cameroun et Rockville, Maryland, USA : ICF. 
> Disponible sur : https://dhsprogram.com/

---

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
MIT License

Copyright (c) 2024 [Votre Nom]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🙏 Remerciements

- **DHS Program** (ICF) pour la mise à disposition des données EDS Cameroun 2018
- **Ministère de la Santé Publique du Cameroun** pour la coordination de l'enquête
- **Streamlit** pour le framework web open-source
- **XGBoost Team** pour la bibliothèque de gradient boosting

---

<div align="center">

🏥 *Cet outil est destiné à l'aide à la décision médicale et ne remplace pas l'examen clinique.*

**[⬆ Retour en haut](#-prédiction-du-risque-de-mortalité-néonatale-au-cameroun)**

</div>
