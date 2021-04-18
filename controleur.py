from models import Tour, matchmaking_premier_tour, matchmaking, db_save_championnat, db_load_championnat
from models import db_save_tournois, db_load_tournois, save_tournoi
from vue import modifier_classement_joueur_tournoi, load_or_save_during_game, afficher_rapport, menu_acceuil
from vue import creation_tournoi, ajout_joueur, resultat_match, affichage_classement_tournoi, maj_classement
from vue import affichage_classement_championnat, affichage_tournois, modifier_classement_joueur, ajout_joueurs_tournoi
from datetime import date, datetime
from tinydb import TinyDB


def main():

    championnat = []  # liste des joueurs du championnat
    tournois = []  # liste des tournois
    joueurs = []  # liste des joueurs d'un tournoi
    db = TinyDB('db.json')  # base de donnees

    choix_menu = menu_acceuil()
    while choix_menu != 0:
        # ajouter joueur championnat
        if choix_menu == 2:
            championnat.append(ajout_joueur())
            affichage_classement_championnat(championnat)
        # modifier classement joueur
        if choix_menu == 3:
            championnat = modifier_classement_joueur(championnat)
            affichage_classement_championnat(championnat)
        # charger donnees de la bdd
        if choix_menu == 4:
            championnat = db_load_championnat(db)
            affichage_classement_championnat(championnat)
            tournois = db_load_tournois(db)
            affichage_tournois(tournois)
        # afficher rapports
        if choix_menu == 5:
            afficher_rapport(championnat, tournois)
        # sauvegarder etat programme
        if choix_menu == 6:
            db = db_save_championnat(db, championnat)
            db = db_save_tournois(db, tournois)
        # commencer nouveau tournoi
        if choix_menu == 1:
            joueurs = ajout_joueurs_tournoi(championnat)
            tournoi = creation_tournoi(joueurs)
            cpt_tours = 0
            # premier tour
            cpt_tours += 1
            premier_tour = Tour("Round 1", date.today().strftime("%d/%m/%Y"), datetime.now().strftime("%H:%M"),
                                "date_fin", "heure_fin")
            # matchmaking
            premier_tour = matchmaking_premier_tour(tournoi.joueurs, premier_tour)
            # resultats des matchs
            for match in premier_tour.matchs:
                match = resultat_match(match)
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
                tour = matchmaking(tournoi.joueurs, tour)
                # resultats des matchs
                for match in tour.matchs:
                    match = resultat_match(match)
                # enregistrement du tour dans liste tours du tournoi
                tour.date_fin = date.today().strftime("%d/%m/%Y")
                tour.heure_fin = datetime.now().strftime("%H:%M")
                tournoi.ajouterTour(tour)
                # passer au tour suivant ou sauvegarder etat programme ou modifier classement joueur
                choix = load_or_save_during_game()
                if choix == 2:  # sauvegarder
                    db = db_save_championnat(db, championnat)
                    db = db_save_tournois(db, tournois)
                if choix == 3:  # modifier classement joueur
                    joueurs, championnat = modifier_classement_joueur_tournoi(joueurs, championnat)
                    affichage_classement_championnat(championnat)

            print("FIN DU TOURNOI")
            affichage_classement_tournoi(tournoi)
            tournois.append(save_tournoi(tournoi))  # ajoute le tournoi a la liste des tournois
            championnat = maj_classement(joueurs, championnat)  # demande maj le classement des joueurs du tournoi
            affichage_classement_championnat(championnat)

        choix_menu = menu_acceuil()

    print("AU REVOIR")


if __name__ == "__main__":
    main()