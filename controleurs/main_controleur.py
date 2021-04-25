from datetime import date, datetime
from tinydb import TinyDB

from vues.rapports import Rapport
from vues.gestion_tournoi import GestionTournoi
from vues.modifications_joueur import ModificationJoueur
from vues.acceuil import MenuAcceuil

from modeles.joueur import Joueur
from modeles.match import Match
from modeles.matchmaking import MatchMaking
from modeles.tour import Tour
from modeles.tournoi import Tournoi

from controleurs.gestion_bdd import Database

class MainControleur:

    def run(self):
        championnat = []  # liste des joueurs du championnat
        tournois = []  # liste des tournois
        joueurs = []  # liste des joueurs d'un tournoi
        db = TinyDB('db.json')  # base de donnees

        rapport = Rapport()
        gestion_tournoi = GestionTournoi()
        modif_joueur = ModificationJoueur()
        menu_acceuil = MenuAcceuil()
        gestion_database = Database()
        gestion_matchmaking = MatchMaking()

        choix_menu = menu_acceuil.menu_acceuil()
        while choix_menu != 0:
            # ajouter joueur championnat
            if choix_menu == 2:
                championnat.append(modif_joueur.ajout_joueur())
                rapport.affichage_classement_championnat(championnat)
            # modifier classement joueur
            if choix_menu == 3:
                championnat = modif_joueur.modifier_classement_joueur(championnat,rapport)
                rapport.affichage_classement_championnat(championnat)
            # charger donnees de la bdd
            if choix_menu == 4:
                championnat = gestion_database.db_load_championnat(db)
                rapport.affichage_classement_championnat(championnat)
                tournois = gestion_database.db_load_tournois(db)
                rapport.affichage_tournois(tournois)
            # afficher rapports
            if choix_menu == 5:
                rapport.afficher_rapport(championnat, tournois)
            # sauvegarder etat programme
            if choix_menu == 6:
                db = gestion_database.db_save_championnat(db, championnat)
                db = gestion_database.db_save_tournois(db, tournois)
            # commencer nouveau tournoi
            if choix_menu == 1:
                joueurs = gestion_tournoi.ajout_joueurs_tournoi(championnat, rapport)
                tournoi = gestion_tournoi.creation_tournoi(joueurs)
                cpt_tours = 0
                # premier tour
                cpt_tours += 1
                premier_tour = Tour("Round 1", date.today().strftime("%d/%m/%Y"), datetime.now().strftime("%H:%M"),
                                    "date_fin", "heure_fin")
                # matchmaking
                premier_tour = gestion_matchmaking.matchmaking_premier_tour(tournoi.joueurs, premier_tour)
                # resultats des matchs
                for match in premier_tour.matchs:
                    match = gestion_tournoi.resultat_match(match)
                # enregistrement du premier tour dans tournoi
                premier_tour.date_fin = date.today().strftime("%d/%m/%Y")
                premier_tour.heure_fin = datetime.now().strftime("%H:%M")
                tournoi.ajouterTour(premier_tour)
                # suite tournoi
                while cpt_tours < tournoi.nb_tours:
                    cpt_tours += 1
                    nom_tour = "Round " + str(cpt_tours)
                    tour = Tour(nom_tour, date.today().strftime("%d/%m/%Y"), datetime.now().strftime("%H:%M"),
                                "date_fin", "heure_fin")
                    # matchmaking
                    tour = gestion_matchmaking.matchmaking(tournoi.joueurs, tour)
                    # resultats des matchs
                    for match in tour.matchs:
                        match = gestion_tournoi.resultat_match(match)
                    # enregistrement du tour dans liste tours du tournoi
                    tour.date_fin = date.today().strftime("%d/%m/%Y")
                    tour.heure_fin = datetime.now().strftime("%H:%M")
                    tournoi.ajouterTour(tour)
                    # passer au tour suivant ou sauvegarder etat programme ou modifier classement joueur
                    choix = gestion_tournoi.load_or_save_during_game()
                    if choix == 2:  # sauvegarder
                        db = db_save_championnat(db, championnat)
                        db = db_save_tournois(db, tournois)
                    if choix == 3:  # modifier classement joueur
                        joueurs, championnat = modif_joueur.modifier_classement_joueur_tournoi(joueurs, championnat, rapport)
                        rapport.affichage_classement_championnat(championnat)

                print("FIN DU TOURNOI")
                rapport.affichage_classement_tournoi(tournoi)
                tournois.append(gestion_database.save_tournoi(tournoi))  # ajoute le tournoi a la liste des tournois
                championnat = modif_joueur.maj_classement(joueurs, championnat)  # demande maj le classement des joueurs du tournoi
                rapport.affichage_classement_championnat(championnat)

            choix_menu = menu_acceuil.menu_acceuil()

        print("AU REVOIR")