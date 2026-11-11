import pandas as pd
import csv
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# CHEMIN DU FICHIER CSV crée pour stocker les id/questions/réponses (id | Q | R)

BASE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "base_ynov.csv")


# BDD ANNOTÉE (id | Q | R)

base_initiale = [
    {"id": 1,  "Q": "bonjour",                               "R": "Bonjour ! Je suis l'assistant YNOV. Comment puis-je vous aider ?"},
    {"id": 2,  "Q": "quelles sont les filières",             "R": "YNOV propose : Informatique, Cybersécurité, IA & Data, Design, Audiovisuel, Management Digital."},
    {"id": 3,  "Q": "comment s'inscrire",                    "R": "Remplissez le dossier sur maroc.ynov.com, joignez CV + lettre de motivation, puis passez un entretien."},
    {"id": 4,  "Q": "où est le campus",                      "R": "Le campus YNOV Maroc est situé à Casablanca, équipé de labs, studio et espaces coworking."},
    {"id": 5,  "Q": "quels sont les frais de scolarité",     "R": "Les frais varient selon la filière. Contactez maroc.ynov.com pour un devis personnalisé."},
    {"id": 6,  "Q": "l'alternance est possible",             "R": "Oui ! Toutes les filières proposent l'alternance : 3 jours entreprise / 2 jours école, avec rémunération."},
    {"id": 7,  "Q": "quel diplôme je reçois",                "R": "Un Bachelor Bac+3 (Niveau 6) reconnu par l'État français, ou un MBA Bac+5."},
    {"id": 8,  "Q": "c'est quoi la cybersécurité",           "R": "La cybersécurité protège les systèmes contre les attaques. Formation 3 ans avec ethical hacking et certifications."},
]


#  CHARGEMENT GPT-2 il vas etre chargé une seule fois au lancement du programme c'est un gain de temps pour les réponses suivantes

print("⏳ Chargement du modèle GPT-2...")
tokenizer_gpt2 = GPT2Tokenizer.from_pretrained("gpt2")
model_gpt2     = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer_gpt2.pad_token = tokenizer_gpt2.eos_token
print("✅ GPT-2 prêt !\n")


# CRÉER et CHARGER LA BASE CSV

def creer_base():
    if not os.path.exists(BASE_FILE):
        with open(BASE_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "Q", "R"])
            writer.writeheader()
            writer.writerows(base_initiale)
        print(f"✅ Base créée : {BASE_FILE} ({len(base_initiale)} questions)")
    else:
        print(f"📂 Base chargée : {BASE_FILE}")

def charger_base():
    return pd.read_csv(BASE_FILE, encoding="utf-8")

def sauvegarder_question(question, reponse):
    df = charger_base()
    nouvel_id = int(df["id"].max()) + 1
    nouvelle_ligne = {"id": nouvel_id, "Q": question, "R": reponse}
    with open(BASE_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "Q", "R"])
        writer.writerow(nouvelle_ligne)
    print(f"   💾 Appris et sauvegardé (id={nouvel_id})")


#  MOTEUR 1 : TF-IDF + Similarité cosinus  // Term Frequency-Inverse Document Frequency // Fréquence inverse en document

def trouver_reponse(question, df, seuil=0.3):
    questions_base = df["Q"].tolist()
    questions_base.append(question)

    vectorizer   = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(questions_base)

    similarites    = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    meilleur_index = similarites.argmax()
    meilleur_score = similarites[0][meilleur_index]

    if meilleur_score >= seuil:
        reponse = df["R"].iloc[meilleur_index]
        return reponse, True
    else:
        return None, False


# MOTEUR 2 : GPT-2 (génération de texte)

def generer_reponse_gpt2(question, max_tokens=80):
    prompt = f"Question: {question}\nAnswer:"
    inputs = tokenizer_gpt2.encode(prompt, return_tensors="pt")

    outputs = model_gpt2.generate(
        inputs,
        max_new_tokens=max_tokens,
        do_sample=True,
        temperature=0.7,        # créativité du modèle
        top_p=0.9,              # diversité des mots choisis
        pad_token_id=tokenizer_gpt2.eos_token_id,
        eos_token_id=tokenizer_gpt2.eos_token_id,
    )

    texte_complet = tokenizer_gpt2.decode(outputs[0], skip_special_tokens=True)

    # Extraire uniquement la réponse après "Answer:"
    if "Answer:" in texte_complet:
        reponse = texte_complet.split("Answer:")[-1].strip()
    else:
        reponse = texte_complet.strip()

    return reponse


# BOUCLE PRINCIPALE
def chatbot():
    creer_base()
    print("\n" + "=" * 55)
    print("   🤖 CHATBOT INTELLIGENT V1 — YNOV Campus Maroc")
    print("   TF-IDF (base CSV)  +  GPT-2 (génération IA)")
    print("=" * 55)
    print("   Tapez 'voir base' pour afficher la base")
    print("   Tapez 'quit'      pour quitter\n")

    while True:
        question = input("Vous : ").strip().lower()

        if not question:
            continue

        if question == "quit":
            print("Bot  : Au revoir ! 👋")
            break

        if question == "voir base":
            df = charger_base()
            print("\n📋 BASE DE DONNÉES ANNOTÉE :")
            print(df.to_string(index=False))
            print()
            continue

        df = charger_base()

        # ÉTAPE 1 : chercher dans la base (TF-IDF)
        reponse, trouve = trouver_reponse(question, df)

        if trouve:
            print(f"Bot  : {reponse}\n")

        else:
            # ÉTAPE 2 : générer avec GPT-2
            print("   🤖 [GPT-2] Question inconnue, génération en cours...")
            reponse_gpt2 = generer_reponse_gpt2(question)
            print(f"Bot  : {reponse_gpt2}\n")

            # ÉTAPE 3 : valider et apprendre
            print("   💬 Cette réponse GPT-2 est-elle correcte ? (o/n)")
            choix = input("Vous : ").strip().lower()

            if choix == "o":
                sauvegarder_question(question, reponse_gpt2)
                print("Bot  : Merci ! J'ai sauvegardé cette réponse.\n")
            else:
                print("Bot  : Pouvez-vous me donner la bonne réponse ?")
                bonne_reponse = input("Vous (réponse) : ").strip()
                if bonne_reponse:
                    sauvegarder_question(question, bonne_reponse)
                    print(f"Bot  : Merci ! J'ai appris : '{question}' → '{bonne_reponse}'\n")
                else:
                    print("Bot  : OK, je passerai au suivant.\n")


#LANCEMENT DU CHATBOT

if __name__ == "__main__":
    chatbot()