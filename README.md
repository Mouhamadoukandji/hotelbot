# 🏨 HotelBot - Système Intelligent de Réservation Hôtelière

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Oracle](https://img.shields.io/badge/Oracle-21c-red.svg)](https://www.oracle.com/database/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-Academic-green.svg)](LICENSE)

## 📋 Description

HotelBot est un système de réservation hôtelière intelligent qui révolutionne l'expérience utilisateur en combinant une base de données Oracle robuste avec l'intelligence artificielle de Claude (Anthropic). Ce projet académique démontre comment le traitement du langage naturel peut simplifier les interactions avec des systèmes de base de données complexes.

### ✨ Fonctionnalités Principales

- **Chatbot Intelligent** : Interagissez en langage naturel pour rechercher et réserver des chambres
- **Recherche Avancée** : Filtrage par ville, prix, catégorie d'étoiles et disponibilité
- **Gestion des Réservations** : Création et suivi des réservations en temps réel
- **Dashboard Administratif** : Supervision des données et statistiques d'utilisation
- *Génération SQL Automatique** : Claude traduit vos questions en requêtes SQL optimisées

## Architecture Technique

```
┌─────────────────┐
│   Interface     │
│   Streamlit     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────┐
│   Claude API    │◄────►│    Python    │
│   (Anthropic)   │      │   Backend    │
└─────────────────┘      └──────┬───────┘
                                │
                                ▼
                         ┌─────────────┐
                         │   Oracle    │
                         │  Database   │
                         │     21c     │
                         └─────────────┘
```

### 🛠️ Stack Technologique

| Composant | Technologie | Version |
|-----------|-------------|---|
| Frontend | Streamlit | Latest |
| Backend | Python | 3.10-slim|
| Base de données | Oracle Database | 21-slim |
| IA/NLP | Claude API (Anthropic) | 0.71.0 |
| Containerisation | Docker & Docker Compose | Latest |



## 🚀 Installation et Déploiement

### Prérequis

- Docker et Docker Compose installés
- Git pour cloner le dépôt
- (Optionnel) Python 3.9+ pour le développement local

### Installation avec Docker (Recommandé)

1. **Cloner le projet**
```bash
git clone https://github.com/Mouhamadoukandji/hotelbot.git
cd hotelbot
```

2. **Configurer les variables d'environnement**

Créer un fichier `.env` à la racine du projet :

```env
# Configuration Oracle Database
ORACLE_PASSWORD=Password123
ORACLE_DATABASE=HOTELDB
ORACLE_HOST=oracle-db
ORACLE_PORT=1521
ORACLE_USER=system
ORACLE_SERVICE=XEPDB1

# Configuration Claude API
CLAUDE_API_KEY="VOTRE CLEF"
```

⚠️ **Note de Sécurité** : Ce projet est à but académique. En production, utilisez un gestionnaire de secrets (AWS Secrets Manager, Azure Key Vault, etc.).

3. **Lancer l'application**
```bash
pip install -r requirements.txt OUBIEN pip3 install -r requirements.txt

docker-compose up --build
```

4. **Accéder à l'interface**

Ouvrez votre navigateur et accédez à : `http://localhost:8501`


```

## 💡 Utilisation

### Exemples de Requêtes en Langage Naturel

Le chatbot comprend des requêtes variées :

```
"Trouve-moi un hôtel à Paris avec une chambre double pour 2 nuits"

"Quels sont les hôtels 4 étoiles disponibles à Lyon ?"

"Je cherche une chambre pour moins de 100€ par nuit à Marseille"

"Montre-moi les disponibilités du 15 au 20 décembre"

"Réserve une suite pour Pierre Dupont du 1er au 5 janvier"
```

### Fonctionnalités Principales

#### 🔍 Recherche d'Hôtels
- Filtrage par ville, prix, nombre d'étoiles
- Recherche par type de chambre (simple, double, suite, etc.)
- Vérification de disponibilité par dates

#### 📝 Gestion des Réservations
- Création de réservations via conversation naturelle
- Consultation de l'historique des réservations
- Suivi en temps réel des occupations

#### 📊 Dashboard Administratif
- Vue d'ensemble des données
- Vérification de l'intégrité des tables
- Statistiques d'utilisation du système

## 📈 Données de Démonstration

Le système est préchargé avec des données réalistes :

- **10 hôtels** dans différentes villes françaises (Paris, Lyon, Marseille, Bordeaux, Nice, etc.)
- **10 types de chambres** avec tarification variée (de 50€ à 500€/nuit)
- **100 chambres** réparties entre les différents établissements
- **15 clients** avec profils diversifiés
- **Historique complet** de réservations et occupations

## 🔒 Sécurité

### Mesures Implémentées

- ✅ Validation des requêtes SQL générées par Claude
- ✅ Protection contre les injections SQL
- ✅ Gestion des erreurs et timeouts
- ✅ Validation stricte des entrées utilisateur
- ✅ Logs de débogage détaillés

### Bonnes Pratiques

- Séparation claire des couches (présentation, logique, données)
- Code documenté et maintenable
- Gestion appropriée des exceptions
- Configuration externalisée via variables d'environnement

## 🎓 Valeur Pédagogique

Ce projet couvre des concepts avancés en développement logiciel :

- **Bases de Données** : Modélisation relationnelle, requêtes SQL complexes, contraintes d'intégrité
- **Intelligence Artificielle** : Traitement du langage naturel, intégration d'API IA
- **Architecture Logicielle** : conteneurisation Docker
- **Développement Full-Stack** : Python, Streamlit
- **DevOps** : Docker Compose, gestion de configuration

## 🔮 Roadmap et Améliorations Futures

### Court Terme
- [ ] Interface administrateur avancée
- [ ] Export des données (PDF, Excel)
- [ ] Notifications par email pour les réservations

### Moyen Terme
- [ ] Système de recommandation personnalisé basé sur l'historique
- [ ] Intégration de paiements (Stripe, PayPal)
- [ ] API REST complète pour intégrations tierces



## 🤝 Contribution

Ce projet est académique et ouvert aux contributions. Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 License

Ce projet est sous licence académique. Il est destiné à des fins éducatives uniquement.

## 👥 Auteurs

Projet réalisé dans le cadre d'un cursus académique en informatique et bases de données.

## 📧 Contact

Pour toute question ou suggestion concernant ce projet académique, n'hésitez pas à ouvrir une issue sur GitHub.

## 🙏 Remerciements

- **Anthropic** pour l'API Claude
- **Oracle** pour la base de données
- **Streamlit** pour le framework d'interface
- La communauté open source pour les bibliothèques Python

---

⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile sur GitHub !

📚 Pour plus d'informations sur les technologies utilisées :
- [Documentation Claude API](https://docs.anthropic.com/)
- [Documentation Oracle Database](https://docs.oracle.com/en/database/)
- [Documentation Streamlit](https://docs.streamlit.io/)
