import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

SCHEMA_CONTEXT = """
Tu es un expert SQL Oracle spécialisé dans la réservation hôtelière.

SCHEMA DE LA BASE :
- HOTELS(NUMHO, NOMHO, RUEADRHO, VILLEHO, NBETOILESHO)
- TYPESCHAMBRE(NUMTY, NOMTY, PRIXTY) 
- CHAMBRES(NUMCH, NUMHO, NUMTY)
- CLIENTS(NUMCL, NOMCL, PRENOMCL, RUEADRCL, VILLECL)
- RESERVATIONS(NUMCL, NUMHO, NUMTY, DATEA, NBJOURS, NBCHAMBRES)
- OCCUPATIONS(NUMCL, NUMHO, NUMCH, DATEA, DATED)

Règles métier :
- Les prix sont en euros
- DATEA = date d'arrivée
- DATED = date de départ
- NBJOURS = intervalle en jours
"""

SCHEMA_TRANS = """"
"""
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.getenv("CLAUDE_API_KEY"),
)


def generer_requete_sql(question_utilisateur):
    prompt = f"""
    Question: {question_utilisateur}

    Génère UNIQUEMENT la requête SQL Oracle sans explications.
    Utilise le schéma fourni.
    
    Si la requête tente de faire autre chose (comme demande de suppression ou de modification)
     qu'une lecteur Génère une chaine VIDE
    """


    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system=SCHEMA_CONTEXT,
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    reponse_brute = response.content[0]
    requete_sql = extraire_sql_proprement(reponse_brute)
    return requete_sql

def sql_to_translation(requete_sql):
    prompt =  f"""
        En tant qu'assistant hôtelier expert, votre mission est de transformer des résultats bruts de base de données en une réponse élégante, chaleureuse et facile à comprendre pour un client.

        CONTEXTE :
        Un client a posé cette question : "{requete_sql}"
        
       

        VOTRE MISSION :
        Créez une réponse qui :
        1. 🌟 Commence par une phrase d'accueil chaleureuse
        2. 📊 Présente les résultats de manière claire et organisée
        3. 💫 Met en valeur les informations importantes
        4. 🏨 Utilise un vocabulaire hôtelier professionnel mais accessible
        5. 🤝 Se termine par une proposition d'aide supplémentaire

        TON :
        - Professionnel et élégant
        - Chaleureux et attentionné
        - Clair et pédagogique
        - Jamais technique ou jargonnant

        FORMATAGE :
        - Utilisez des émojis discrètement pour aérer le texte
        - Structurez avec des sauts de ligne naturels
        - Mettez en gras les informations importantes
        - Soyez concis mais complet

        Exemple de structure :
        "Je suis ravi de vous présenter les options correspondant à votre recherche...
        
        Voici ce que j'ai trouvé pour vous :
        • [Point clé 1]
        • [Point clé 2]
        • [Point clé 3]
        
        [Conclusion et proposition d'aide]"

        Maintenant, transformez ces résultats bruts en une magnifique réponse client.
        """
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt},
        ]
    )

    return response.content


def extraire_sql_proprement(reponse_claude):
    texte_brut = reponse_claude.text

    debut = texte_brut.find("```sql")
    if debut != -1:
        debut += 6
        fin = texte_brut.find("```", debut)
        if fin != -1:
            sql = texte_brut[debut:fin].strip()
            return sql
    debut = texte_brut.find("```")
    if debut != -1:
        debut += 3
        fin = texte_brut.find("```", debut)
        if fin != -1:
            sql = texte_brut[debut:fin].strip()
            if sql.lower().startswith("sql"):
                sql = sql[3:].strip()
            return sql

    return texte_brut.strip()


def formater_elegant(reponse_claude):

    texte_brut = reponse_claude.text if hasattr(reponse_claude, 'text') else str(reponse_claude)

    prompt = f"""
    Transformez cette réponse en un message magnifiquement formaté pour une application de réservation hôtelière de luxe :

    {texte_brut}

    STYLE À APPLIQUER :
    💫 Ton élégant et raffiné
    🏨 Vocabulaire hôtelier de prestige
    ✨ Formatage Markdown soigné
    🌟 Emojis discrets mais impactants
    📝 Structure aérée et professionnelle

    FORMATAGE :
    - **Noms d'hôtels en gras**
    - *Adresses en italique*  
    - Liste à puces avec emojis
    - Paragraphes bien espacés
    - Ponctuation soignée

    Retournez uniquement le texte formaté.
    """

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt},
        ]
    )

    return response.content[0].text

print(generer_requete_sql("Quels hôtels 4 étoiles à Paris ?"))