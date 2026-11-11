# 🤖 Chatbot YNOV – Assistant hybride TF-IDF + GPT-2

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-TF--IDF-F7931E)
![Transformers](https://img.shields.io/badge/HuggingFace-GPT--2-FFD21E)

Projet du module **Fondamentaux de l'IA** (Bachelor 3, Ynov Campus) : un assistant conversationnel qui répond
aux questions des futurs étudiants (filières, inscription, alternance, diplômes…).

## 🧠 Fonctionnement

1. **Base de connaissances annotée** (`base_ynov.csv`) : paires question / réponse.
2. **Recherche sémantique** : la question est vectorisée en **TF-IDF** et comparée à la base par **similarité cosinus**.
3. **Réponse** :
   - si la similarité dépasse un seuil, la réponse de la base est renvoyée ;
   - sinon, **GPT-2** génère une réponse à partir de la question.
4. **Apprentissage** : l'utilisateur peut enrichir la base avec de nouvelles questions / réponses.

## 📁 Fichiers

| Fichier | Description |
|---|---|
| `chatbot_ynov.py` | Version 1 : recherche par similarité TF-IDF |
| `chatbot_ynov3.py` | Version hybride : TF-IDF + génération GPT-2 |
| `base_ynov.csv` | Base de connaissances (id, question, réponse) |

## ▶️ Lancer

```bash
pip install pandas scikit-learn transformers torch
python chatbot_ynov3.py
```

Le modèle GPT-2 est téléchargé automatiquement au premier lancement (environ 500 Mo).

## 🛠️ Compétences

`Python` · `NLP` · `TF-IDF` · `similarité cosinus` · `GPT-2` · `Hugging Face Transformers`

---
Khadija Ibisk – Bachelor Dev IA & Data Engineering, Ynov Campus
