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

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.getenv("CLAUDE-API-KEY"),
)


def generer_requete_sql(question_utilisateur):
    prompt = f"""
    Question: {question_utilisateur}

    Génère UNIQUEMENT la requête SQL Oracle sans explications.
    Utilise le schéma fourni.
    """


    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system=SCHEMA_CONTEXT,
        messages=[
            {"role": "user", "content": prompt},
        ]
    )

    return response.content


print(generer_requete_sql("Quels hôtels 4 étoiles à Paris ?"))