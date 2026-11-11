from nltk.chat.util import Chat, reflections

# Définir le dialogue
dialog = [

    # Salutations.
    ["bonjour",
        ["Bonjour ! Bienvenue sur YNOV Campus Maroc. Comment puis-je vous aider ?",
         "Bonjour ! Je suis le chatbot de YNOV Campus Maroc, que souhaitez-vous savoir ?"]],

    ["salut",
        ["Salut ! Ravi de vous accueillir sur YNOV Campus Maroc !"]],

    ["bonsoir",
        ["Bonsoir ! Comment puis-je vous aider ce soir ?"]],

    # Identité avec variable.
    ["je m'appelle (.*)",
        ["Enchanté %1 ! Je suis le chatbot officiel de YNOV Campus Maroc.",
         "Bienvenue %1 ! Comment puis-je vous aider dans votre orientation ?"]],

    ["mon nom est (.*)",
        ["Bonjour %1 ! Avez-vous des questions sur nos filières ou l'admission ?"]],

    ["je suis (.*) et je veux m'inscrire",
        ["Parfait %1 ! Pour vous inscrire, rendez-vous sur maroc.ynov.com et déposez votre dossier en ligne."]],

    # Questions sur le chatbot.
    ["qui es.?tu",
        ["Je suis le chatbot de YNOV Campus Maroc, propulsé par NLTK Python !"]],

    ["qu.?est.?ce que tu fais",
        ["Je réponds à toutes vos questions sur les filières, l'admission et la vie à YNOV Campus Maroc."]],

    # Filières.
    ["quelles sont les filières.*",
        ["Nous proposons : Informatique, Cybersécurité, IA & Data Science, Design, Audiovisuel, et Management Digital."]],

    ["je veux faire (.*)",
        ["Excellent choix ! La filière %1 est disponible à YNOV Campus Maroc. Souhaitez-vous connaître les conditions d'admission ?"]],

    ["parle.?moi de (.*)",
        ["La filière %1 est une formation de 3 ans (Bachelor). Elle prépare aux métiers du numérique avec des projects concrets et de l'alternance possible."]],

    # Admission.
    ["comment.*inscrire.*",
        ["Pour s'inscrire : 1) Remplissez le dossier sur maroc.ynov.com  2) Préparez CV + lettre de motivation  3) Passez un entretien de motivation."]],

    ["quel.*niveau.*requis.*",
        ["Le niveau requis est le Baccalauréat, toutes séries acceptées !"]],

    ["j.?ai un bac (.*)",
        ["Parfait ! Avec un bac %1, vous pouvez postuler à toutes nos filières. Nous acceptons tous les bacs !"]],

    # Campus.
    ["où.*campus.*",
        ["Le campus YNOV Maroc est situé à Casablanca. Il dispose de labs informatiques, studio audiovisuel et espaces coworking."]],

    [".*casablanca.*",
        ["Oui, notre campus principal est à Casablanca ! Un cadre moderne et équipé pour vos études."]],

    # Frais.
    [".*frais.*scolarité.*",
        ["Les frais varient selon la filière. Contactez-nous sur maroc.ynov.com pour un devis personnalisé."]],

    [".*bourse.*",
        ["YNOV propose des bourses d'excellence ainsi que la possibilité de financer ses études via l'alternance."]],

    # Alternance.
    [".*alternance.*",
        ["Oui ! Toutes nos filières proposent la voie alternance : 3 jours en entreprise / 2 jours à l'école, avec rémunération."]],

    # Diplôme.
    [".*diplôme.*",
        ["YNOV délivre un Bachelor (Bac+3) certifié Niveau 6, reconnu en France et à l'international. Un MBA Bac+5 est aussi possible."]],

    # Remerciements.
    ["merci.*",
        ["Avec plaisir ! N'hésitez pas si vous avez d'autres questions.",
         "De rien ! Bonne chance dans votre projet d'études à YNOV !"]],

    # Au revoir.
    ["au revoir",
        ["Au revoir ! On espère vous voir bientôt sur le campus YNOV Maroc !"]],

    ["bye.*",
        ["À bientôt ! N'hésitez pas à revenir."]],
]

#  Lancer le chatbot
print("=" * 55)
print("   🎓 CHATBOT YNOV CAMPUS MAROC — powered by NLTK")
print("=" * 55)
print("  Tapez 'quit' pour quitter.\n")

chatbot = Chat(dialog, reflections)
chatbot.converse()