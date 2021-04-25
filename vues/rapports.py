
class Rapport:

    def afficher_joueurs(self,joueurs):
        """ affiche tous les joueurs du tournoi """
        print("| Nom Prenom | Classement | Points |")
        for joueur in joueurs:
            print("|" + joueur.nom + " " + joueur.prenom + "|" + str(joueur.classement) +
                "|" + str(joueur.total_points) + "|")

    def afficher_rapport(self, championnat, tournois):
        """ affiche le rapport selectionne """
        print("Selectionnez le rapport que vous souhaitez afficher: ")
        print("| CLASSEMENT CHAMPIONNAT (1) | ALPHABETIQUE CHAMPIONNAT (2) | DETAILS TOURNOI (3) |")
        choix_rapport = int(input())
        if choix_rapport == 1:
            self.affichage_classement_championnat(championnat)
        if choix_rapport == 2:
            self.affichage_alphabetique_championnat(championnat)
        if choix_rapport == 3:
            self.affichage_tournois(tournois)

    def affichage_alphabetique_tournoi(self, tournoi):
        """ affiche joueurs tournoi par ordre alphabetique """
        joueurs = tournoi.joueurs
        liste_triee = sorted(joueurs, key=lambda x: x.nom)  # tri des joueurs par ordre alphabetique
        print("JOUEURS TOURNOI PAR ORDRE ALPHABETIQUE")
        for joueur in liste_triee:
            print(joueur.nom)    


    def affichage_classement_tournoi(self, tournoi):
        """ affiche joueurs dans ordre des points """
        joueurs = tournoi.joueurs
        liste_triee = sorted(joueurs, key=lambda x: x.total_points, reverse=True)  # tri des joueurs par total_points
        print("CLASSEMENT TOURNOI")
        for joueur in liste_triee:
            print(joueur.nom + " : " + str(joueur.total_points) + " points")

    def affichage_classement_championnat(self,championnat):
        """ affiche joueurs championnat dans ordre classement """
        liste_triee = sorted(championnat, key=lambda x: x.classement)  # tri des joueurs par classement
        print("CLASSEMENT CHAMPIONNAT")
        for joueur in liste_triee:
            print(str(joueur.classement) + ": " + joueur.nom)


    def affichage_alphabetique_championnat(self, championnat):
        """ affiche joueurs championnat par ordre alphabetique """
        liste_triee = sorted(championnat, key=lambda x: x.nom)  # tri des joueurs par nom alphabetique
        print("JOUEURS CHAMPIONNAT PAR ORDRE ALPHABETIQUE")
        for joueur in liste_triee:
            print(joueur.nom)  


    def affichage_tournois(self, tournois):
        """ affiche liste de tous les tournois et des tours/matchs de chacun d'entre eux """
        print("LISTE DES TOURNOIS")
        i = 1
        for tournoi in tournois:
            print(str(i) + ": " + tournoi.nom)
            i += 1
        print("Voulez plus d'infos sur un tournoi? (0) NON / (numero tournoi) OUI")
        choix_tournoi = int(input())
        if choix_tournoi == 0:
            return
        else:
            tournoi = tournois[choix_tournoi-1]
            print("Que souhaitez-vous afficher? (1) Tous les tours / (2) tous les matchs /" +
                " (3) Classement / (4) Joueurs par ordre alphabetique")
            choix = int(input())
            # affichages tous les tours du tournoi
            if choix == 1:
                for tour in tournoi.tours:
                    print(tour.nom)
            # affichages tous les matchs du tournoi
            if choix == 2:
                for tour in tournoi.tours:
                    print(tour.nom)
                    for match in tour.matchs:
                        print(match.joueur1[0].nom + " (" + str(match.joueur1[1]) + ")" +
                            " vs " + match.joueur2[0].nom + " (" + str(match.joueur2[1]) + ")")
            # affichage classemennt tournoi
            if choix == 3:
                self.affichage_classement_tournoi(tournoi)
            # affichage joueurs tournoi par ordre aplhabetique
            if choix == 4:
                self.affichage_alphabetique_tournoi(tournoi)                                             