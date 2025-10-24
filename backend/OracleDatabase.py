import oracledb
import os
from dotenv import load_dotenv

load_dotenv()


class OracleDatabase:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        """Établir la connexion à Oracle"""
        try:
            # Configuration de la connexion
            self.connection = oracledb.connect(
                user=os.getenv("ORACLE_USER", "system"),
                password=os.getenv("ORACLE_PASSWORD", "Password123"),
                host=os.getenv("ORACLE_HOST", "oracle-db"),
                port=os.getenv("ORACLE_PORT", "1521"),
                service_name=os.getenv("ORACLE_SERVICE", "XEPDB1")
            )
            print("Connexion Oracle établie")
        except Exception as e:
            print(f"❌ Erreur connexion Oracle: {e}")
            raise

    def executer_requete(self, requete_sql, params=None):
        try:
            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(requete_sql, params)
                else:
                    cursor.execute(requete_sql)

                if requete_sql.strip().upper().startswith('SELECT'):
                    colonnes = [col[0] for col in cursor.description]
                    resultats = cursor.fetchall()
                    return {"colonnes": colonnes, "donnees": resultats}
                else:
                    self.connection.commit()
                    return {"message": "Requête exécutée avec succès"}

        except Exception as e:
            print(f"❌ Erreur SQL: {e}")
            self.connection.rollback()
            raise

    def fermer_connexion(self):
        if self.connection:
            self.connection.close()
            print("🔌 Connexion Oracle fermée")