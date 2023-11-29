# GenMotiv.IA

## Table des matières
1. [Description du projet](#description-du-projet)
2. [Tech Stack](#tech-stack)
3. [Auteur](#auteur)
4. [Fonctionnalités](#fonctionnalités)
5. [Installation](#installation)

## Description du projet <a id="description-du-projet"></a>

GenMotiv.IA est un projet qui utilise Python et l'API OpenAI GPT pour générer des lettres de motivation personnalisées. Il prend en entrée l'URL d'une annonce d'emploi et les informations du profil LinkedIn du candidat, puis génère une lettre de motivation en se basant sur les détails fournis.

## Tech Stack <a id="tech-stack"></a>

### Langage 
- Python 3.10

### Intelligence Artificielle
- All GPT Model (GPT4  par défault)

## Auteur <a id="auteur"></a>
- [@anthonydt16](https://github.com/Anthonydt16)

## Fonctionnalités <a id="fonctionnalités"></a>
- Récupération des informations du profil LinkedIn via un json exporté
- Utilisation de l'API OpenAI GPT-3.5 Turbo pour générer des textes
- Génération d'une lettre de motivation personnalisée en se basant sur l'annonce d'emploi et les informations du profil

## Installation <a id="installation"></a>
### Dépendances
Pour installer les dépendances requises, exécutez la commande suivante :
```bash
pip install -r requirements.txt
```

### Clé API
Assurez-vous d'avoir une clé d'API OpenAI valide et mettez-la dans un fichier .env sous le nom de : "API_KEY"


### Exécution du script
Exécutez le script principal avec la commande suivante :
```bash
python main.py
```

### Séléction du modèle
Dans le fichier .env vous trouverez une variable MODEL, changez la en fonction de vos besoin.

### Extension LinkedIn
Installez l'extension [JSON Resume Exporter](https://chromewebstore.google.com/detail/json-resume-exporter/caobgmmcpklomkcckaenhjlokpmfbdec) pour pouvoir exporter votre profil LinkedIn en json. Enregistrez le fichier json à la racine du projet et indiquez son emplacement dans le fichier .env sous le nom de : "PROFILE"
