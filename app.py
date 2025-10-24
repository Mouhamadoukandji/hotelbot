import streamlit as st
import pandas as pd
from OracleDatabase import OracleDatabase
import CreateTables
import insertData
from backend import config_claude_model



def page_admin():
    st.title("Administration Base de Données")

    try:
        db = OracleDatabase()
        st.success("Connecté à la base de données Oracle")
    except Exception as e:
        st.error(f"Erreur de connexion: {e}")
        return

    # Section 1: Vérification des tables
    st.header("Vérification des Tables")

    if st.button("Vérifier toutes les tables"):
        try:
            # Récupérer la liste des tables
            result = db.executer_requete("""
                SELECT table_name, num_rows 
                FROM user_tables 
                ORDER BY table_name
            """)

            if result['donnees']:
                st.success(f"{len(result['donnees'])} tables trouvées")

                # Afficher sous forme de tableau
                df_tables = pd.DataFrame(result['donnees'], columns=result['colonnes'])
                st.dataframe(df_tables, use_container_width=True)

                # Vérifier les tables spécifiques à votre schéma
                tables_attendues = ['HOTELS', 'TYPESCHAMBRE', 'CHAMBRES', 'CLIENTS', 'RESERVATIONS', 'OCCUPATIONS']
                tables_trouvees = [row[0] for row in result['donnees']]

                st.subheader("Validation du schéma")
                for table in tables_attendues:
                    if table in tables_trouvees:
                        st.success(f"{table}")
                    else:
                        st.error(f"{table} - MANQUANTE")
            else:
                st.warning("Aucune table trouvée dans la base")

        except Exception as e:
            st.error(f"Erreur lors de la vérification: {e}")

    st.header("🔎 Explorer les données")

    table_selectionnee = st.selectbox(
        "Choisir une table à explorer:",
        ["HOTELS", "TYPESCHAMBRE", "CHAMBRES", "CLIENTS", "RESERVATIONS", "OCCUPATIONS"]
    )

    if st.button(f"Afficher {table_selectionnee}"):
        try:
            result = db.executer_requete(f"SELECT * FROM {table_selectionnee}")

            if result['donnees']:
                st.success(f"{len(result['donnees'])} enregistrements dans {table_selectionnee}")

                df = pd.DataFrame(result['donnees'], columns=result['colonnes'])
                st.dataframe(df, use_container_width=True)

                # Statistiques simples
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Nombre total", len(df))
                with col2:
                    st.metric("Colonnes", len(df.columns))
                with col3:
                    if not df.empty:
                        st.metric("Exemple", df.iloc[0, 0])
            else:
                st.warning(f"La table {table_selectionnee} est vide")

        except Exception as e:
            st.error(f"Erreur lors de l'accès à {table_selectionnee}: {e}")

    st.header("Statistiques Globales")

    if st.button("Calculer les statistiques"):
        try:
            stats_queries = {
                "Hôtels par ville": "SELECT VILLEHO, COUNT(*) FROM HOTELS GROUP BY VILLEHO",
                "Types de chambre et prix": "SELECT NOMTY, PRIXTY FROM TYPESCHAMBRE ORDER BY PRIXTY",
                "Nombre de clients": "SELECT COUNT(*) FROM CLIENTS",
                "Réservations actives": "SELECT COUNT(*) FROM RESERVATIONS WHERE DATEA > SYSDATE"
            }

            for titre, requete in stats_queries.items():
                st.subheader(titre)
                try:
                    result = db.executer_requete(requete)
                    if result['donnees']:
                        df = pd.DataFrame(result['donnees'], columns=result['colonnes'])
                        st.dataframe(df, use_container_width=True)
                except Exception as e:
                    st.warning(f"Données non disponibles: {e}")

        except Exception as e:
            st.error(f"Erreur lors du calcul des statistiques: {e}")


def askquestion():
    db = OracleDatabase()
    with st.form("hotel_query_form"):
        user_query = st.text_input(
            "Posez votre question :",
            placeholder="Ex: Trouve-moi un hôtel à Paris avec une chambre double"
        )

        submitted = st.form_submit_button("Rechercher")

        if submitted and user_query:
            st.write("**Votre demande :**", user_query)
            response = config_claude_model.generer_requete_sql(user_query)
            result = db.executer_requete(response)
            explication_sql = config_claude_model.sql_to_translation(result)
            reponse_formatter = config_claude_model.formater_elegant(explication_sql)

            with st.spinner("🤖 Recherche en cours..."):
                st.info("Connexion à la base de données Oracle...")
                st.success(reponse_formatter)



def main():
    st.sidebar.title("HotelBot Navigation")

    page = st.sidebar.radio(
        "Choisir une page:",
        ["Chatbot", "Administration BD"]
    )

    if page == "Chatbot":
        askquestion()

    elif page == "Administration BD":
        page_admin()


if __name__ == "__main__":
    CreateTables.creer_tables()
    insertData.inserer_donnees()
    main()