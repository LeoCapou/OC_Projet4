from modeles.tournoi import Tournoi
from vues.rapports import Rapport

class GestionTournoi:
    
    def creation_tournoi(self, joueurs):
        """ creation d un modele de tournoi """
        print("Nom du tournoi : ")
        nom = input()
        print("Lieu : ")
        lieu = input()
        print("Date (DD/MM/YYYY) : ")
        date = input()
        # remise a 0 total_point de chaque joueur
        for joueur in joueurs:
            joueur.total_points = 0
        tournoi = Tournoi(nom, lieu, date, "tournoi de test", joueurs)

        return tournoi


    def ajout_joueurs_tournoi(self, championnat, rapport):
        """ creation liste de joueurs qui participent au tournoi """
        joueurs = []
        rapport.affichage_classement_championnat(championnat)
        championnat = sorted(championnat, key=lambda x: x.classement)  # tri joueurs du championnat par classement
        print("Sélectionnez un nouveau joueur à ajouter au tournoi en indiquant son classement")
        print("ou (0) pour quand vous avez terminé la sélection (nb de joueurs pair)")
        choix_joueur = int(input())
        joueur = championnat[choix_joueur-1]
        joueurs.append(joueur)
        print(joueur.nom + " ajouté au tournoi")
        print("Sélectionnez un nouveau joueur à ajouter au tournoi en indiquant son classement")
        print("ou (0) pour quand vous avez terminé la sélection (nb de joueurs pair)")
        choix_joueur = int(input())
        while choix_joueur != 0 and len(joueurs) > 0:
            joueur = championnat[choix_joueur-1]
            joueurs.append(joueur)
            print(joueur.nom + " ajouté au tournoi")
            print("Sélectionnez un nouveau joueur à ajouter au tournoi en indiquant son classement")
            print("ou (0) pour quand vous avez terminé la sélection (nb de joueurs pair)")
            choix_joueur = int(input())
        if len(joueurs) % 2 != 0:  # nb joueurs impair
            print("NB JOUEURS IMPAIR, ajoutez un dernier joueur au tournoi en indiquant son classement")
            choix_joueur = int(input())
            joueur = championnat[choix_joueur-1]
            joueurs.append(joueur)
            print(joueur.nom + " ajouté au tournoi")

        return joueurs        



    def resultat_match(self, match):
        """ definir vainqueur du match ou egalite """
        print("Veuillez entrer le résultat du match")
        print("Vainqueur: " + str(match.joueur1[0].nom) + " (1) " + str(match.joueur2[0].nom) + " (2) ou égalité (0)")
        choix = int(input())
        if choix == 0:  # egalite
            match.joueur1[1] = 0.5
            match.joueur1[0].total_points += 0.5
            match.joueur2[1] = 0.5
            match.joueur2[0].total_points += 0.5
        elif choix == 1:  # joueur 1 vainqueur
            match.joueur1[1] = 1
            match.joueur1[0].total_points += 1
            match.joueur2[1] = 0
        elif choix == 2:  # joueur 2 vainqueur
            match.joueur1[1] = 0
            match.joueur2[1] = 1
            match.joueur2[0].total_points = match.joueur2[0].total_points + 1

        return match       

    def load_or_save_during_game(self):
        """ permet de charger ou sauvegarder l'etat du programme au cours d'une partie """
        print("(1) TOUR SUIVANT | (2) SAUVEGARDER | (3) MODIFIER CLASSEMENT JOUEUR")
        choix = int(input())
        return choix         