from datetime import datetime, timedelta
from backend import OracleDatabase


def inserer_donnees():

    try:
        db = OracleDatabase.OracleDatabase()
        print("Début de l'insertion des données...")

        print("🏨 Insertion des hôtels...")
        hotels = [
            (1, 'Hôtel Plaza Athénée', '25 Avenue Montaigne', 'Paris', 5),
            (2, 'Le Negresco', '37 Promenade des Anglais', 'Nice', 5),
            (3, 'InterContinental Lyon', '66 Quai Charles de Gaulle', 'Lyon', 5),
            (4, 'Hôtel de Crillon', '10 Place de la Concorde', 'Paris', 5),
            (5, 'Grand Hôtel de Bordeaux', '2-5 Place de la Comédie', 'Bordeaux', 4),
            (6, 'Hôtel Mercure Centre', '15 Rue Dr Charles Cazalis', 'Marseille', 3),
            (7, 'Hôtel de la Cité', 'Place Auguste Pierre Pont', 'Carcassonne', 4),
            (8, 'Hôtel Régina', '2 Place des Pyramides', 'Paris', 4),
            (9, 'Hôtel Cour des Loges', '6 Rue du Boeuf', 'Lyon', 4),
            (10, 'Hôtel Martinez', '73 Boulevard de la Croisette', 'Cannes', 5)
        ]

        for hotel in hotels:
            print(hotel[0], hotel[1], hotel[2], hotel[3], hotel[4])
            db.executer_requete(
                "INSERT INTO HOTELS (NUMHO, NOMHO, RUEADRHO, VILLEHO, NBETOILESHO) VALUES (:1, :2, :3, :4, :5)",
                hotel
            )
        print(f"✅ {len(hotels)} hôtels insérés")

        print("🛏️ Insertion des types de chambre...")
        types_chambre = [
            (1, 'Chambre Simple Standard', 89.00),
            (2, 'Chambre Double Classique', 129.00),
            (3, 'Chambre Double Supérieure', 169.00),
            (4, 'Suite Junior', 249.00),
            (5, 'Suite Exécutive', 349.00),
            (6, 'Suite Présidentielle', 599.00),
            (7, 'Chambre Familiale 4 personnes', 199.00),
            (8, 'Chambre Confort Vue Mer', 229.00),
            (9, 'Chambre Luxe avec Balcon', 279.00),
            (10, 'Suite Honeymoon', 459.00)
        ]

        for type_ch in types_chambre:
            db.executer_requete(
                "INSERT INTO TYPESCHAMBRE (NUMTY, NOMTY, PRIXTY) VALUES (:1, :2, :3)",
                type_ch
            )
        print(f"✅ {len(types_chambre)} types de chambre insérés")

        print("🚪 Insertion des chambres...")
        chambres = []
        chambre_id = 100

        for hotel_id in range(1, 11):
            for i in range(10):
                type_chambre = (i % 10) + 1
                chambres.append((chambre_id, hotel_id, type_chambre))
                chambre_id += 1

        for chambre in chambres:
            db.executer_requete(
                "INSERT INTO CHAMBRES (NUMCH, NUMHO, NUMTY) VALUES (:1, :2, :3)",
                chambre
            )
        print(f"✅ {len(chambres)} chambres insérées")

        print("👥 Insertion des clients...")
        clients = [
            (1, 'Martin', 'Sophie', '15 Rue de la République', 'Lyon'),
            (2, 'Dubois', 'Pierre', '22 Avenue Victor Hugo', 'Paris'),
            (3, 'Bernard', 'Marie', '8 Rue du Moulin', 'Marseille'),
            (4, 'Thomas', 'Jean', '45 Boulevard Gambetta', 'Bordeaux'),
            (5, 'Robert', 'Catherine', '3 Place Bellecour', 'Lyon'),
            (6, 'Petit', 'Philippe', '67 Rue de la Paix', 'Nice'),
            (7, 'Durand', 'Isabelle', '12 Cours Mirabeau', 'Aix-en-Provence'),
            (8, 'Leroy', 'Antoine', '89 Quai des Chartrons', 'Bordeaux'),
            (9, 'Moreau', 'Élise', '34 Rue de Rivoli', 'Paris'),
            (10, 'Simon', 'Nicolas', '56 Promenade des Anglais', 'Nice'),
            (11, 'Laurent', 'Camille', '78 Rue Saint-Jacques', 'Toulouse'),
            (12, 'Michel', 'David', '23 Place du Capitole', 'Toulouse'),
            (13, 'Garcia', 'Laura', '41 Cours Alsace-Lorraine', 'Bordeaux'),
            (14, 'Fournier', 'Julien', '9 Rue de la Pompe', 'Paris'),
            (15, 'Lemoine', 'Chloé', '31 Avenue Jean Médecin', 'Nice')
        ]

        for client in clients:
            db.executer_requete(
                "INSERT INTO CLIENTS (NUMCL, NOMCL, PRENOMCL, RUEADRCL, VILLECL) VALUES (:1, :2, :3, :4, :5)",
                client
            )
        print(f"✅ {len(clients)} clients insérés")

        print("📅 Insertion des réservations...")
        reservations = []

        aujourdhui = datetime.now()


        for i in range(20):
            num_cl = (i % 15) + 1
            num_ho = (i % 10) + 1
            num_ty = (i % 10) + 1

            date_arrivee = aujourdhui + timedelta(days=10 + (i * 3))

            nb_jours = (i % 7) + 1

            nb_chambres = 1 if i % 3 == 0 else 2

            reservations.append((
                num_cl, num_ho, num_ty,
                date_arrivee,
                nb_jours,
                nb_chambres
            ))

        for reserv in reservations:
            db.executer_requete(
                "INSERT INTO RESERVATIONS (NUMCL, NUMHO, NUMTY, DATEA, NBJOURS, NBCHAMBRES) VALUES (:1, :2, :3, :4, NUMTODSINTERVAL(:5, 'DAY'), :6)",
                (reserv[0], reserv[1], reserv[2], reserv[3], reserv[4], reserv[5])
            )
        print(f"✅ {len(reservations)} réservations insérées")

        print("🏠 Insertion des occupations...")
        occupations = []

        for i in range(30):
            num_cl = (i % 15) + 1
            num_ho = (i % 10) + 1
            num_ch = 100 + (i % (100-1))

            if i < 15:
                date_arrivee = aujourdhui - timedelta(days=30 + (i * 2))
                date_depart = date_arrivee + timedelta(days=(i % 5) + 1)
            else:
                date_arrivee = aujourdhui - timedelta(days=(i % 3))
                date_depart = aujourdhui + timedelta(days=(i % 4) + 1)

            cle_unique = (num_ho, num_ch, date_arrivee)
            combinaisons_uniques = set()

            if cle_unique not in combinaisons_uniques:
                combinaisons_uniques.add(cle_unique)
                occupations.append((num_cl, num_ho, num_ch, date_arrivee, date_depart))


        for occup in occupations:
            db.executer_requete(
                "INSERT INTO OCCUPATIONS (NUMCL, NUMHO, NUMCH, DATEA, DATED) VALUES (:1, :2, :3, :4, :5)",
                occup
            )
        print(f"✅ {len(occupations)} occupations insérées")

        print("\n🎉 INSERTION TERMINÉE AVEC SUCCÈS !")
        print("📊 Récapitulatif des données insérées :")

        tables = ['HOTELS', 'TYPESCHAMBRE', 'CHAMBRES', 'CLIENTS', 'RESERVATIONS', 'OCCUPATIONS']
        for table in tables:
            result = db.executer_requete(f"SELECT COUNT(*) FROM {table}")
            count = result['donnees'][0][0]
            print(f"   - {table}: {count} enregistrements")

        db.fermer_connexion()

    except Exception as e:
        print(f"❌ Erreur lors de l'insertion: {e}")
        import traceback
        traceback.print_exc()


