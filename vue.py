from models import Tournoi, Joueur
import copy


def ajout_joueurs_tournoi(championnat):
    """ creation liste de joueurs qui participent au tournoi """
    joueurs = []
    affichage_classement_championnat(championnat)
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


def creation_tournoi(joueurs):
    """ creation d un modele de tournoi """
    print("Nom du tournoi : ")
    nom = input()
    print("Lieu : ")
    lieu = input()
    print("Date (DD/MM/YYYY) : ")
    date = input()
    print("Nombre de tours : ")
    nb_tours = int(input())
    # remise a 0 total_point de chaque joueur
    for joueur in joueurs:
        joueur.total_points = 0
    tournoi = Tournoi(nom, lieu, date, "tournoi de test", joueurs)
    tournoi.nb_tours = nb_tours

    return tournoi


def afficher_joueurs(joueurs):
    """ affiche tous les joueurs du tournoi """
    print("| Nom Prenom | Classement | Points |")
    for joueur in joueurs:
        print("|" + joueur.nom + " " + joueur.prenom + "|" + str(joueur.classement) +
              "|" + str(joueur.total_points) + "|")


def menu_acceuil():
    """ choix nouveau tournoi ou ajouter joueurs """
    print("| NOUVEAU TOURNOI (1) | AJOUTER JOUEUR CHAMPIONNAT (2) | MODIFIER CLASSEMENT JOUEUR (3) |" +
          " CHARGER DONNEES (4) | AFFICHER RAPPORT (5) | SAUVEGARDER (6) | EXIT (0) |")
    choix = int(input())
    return choix


def afficher_rapport(championnat, tournois):
    """ affiche le rapport selectionne """
    print("Selectionnez le rapport que vous souhaitez afficher: ")
    print("| CLASSEMENT CHAMPIONNAT (1) | ALPHABETIQUE CHAMPIONNAT (2) | DETAILS TOURNOI (3) |")
    choix_rapport = int(input())
    if choix_rapport == 1:
        affichage_classement_championnat(championnat)
    if choix_rapport == 2:
        affichage_alphabetique_championnat(championnat)
    if choix_rapport == 3:
        affichage_tournois(tournois)


def ajout_joueur():
    """ creation joueur """
    print("Nom : ")
    nom = input()
    print("Prenom : ")
    prenom = input()
    print("Date de naissance (DD/MM/YYYY) : ")
    birthday = input()
    print("Sexe (H/F) : ")
    sexe = input()
    print("Classement : ")
    classement = int(input())
    return Joueur(nom, prenom, birthday, sexe, classement)


def resultat_match(match):
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


def affichage_alphabetique_tournoi(tournoi):
    """ affiche joueurs tournoi par ordre alphabetique """
    joueurs = tournoi.joueurs
    liste_triee = sorted(joueurs, key=lambda x: x.nom)  # tri des joueurs par ordre alphabetique
    print("JOUEURS TOURNOI PAR ORDRE ALPHABETIQUE")
    for joueur in liste_triee:
        print(joueur.nom)


def affichage_classement_tournoi(tournoi):
    """ affiche joueurs dans ordre des points """
    joueurs = tournoi.joueurs
    liste_triee = sorted(joueurs, key=lambda x: x.total_points, reverse=True)  # tri des joueurs par total_points
    print("CLASSEMENT TOURNOI")
    for joueur in liste_triee:
        print(joueur.nom + " : " + str(joueur.total_points) + " points")


def maj_classement(joueurs_tournoi, championnat):
    """ le responsable met a jour le classement des joueurs du tournoi """
    championnat = sorted(championnat, key=lambda x: x.classement)  # tri joueurs du championnat par classement
    print("VEUILLEZ METTRE A JOUR LE CLASSEMENT GENERAL DES JOUEURS AYANT PARTICIPES AU TOURNOI")
    for joueur in joueurs_tournoi:
        print("joueur: " + joueur.nom + ", nouveau classement:")
        nouveau_joueur = copy.deepcopy(joueur)
        nouveau_classement = int(input())
        nouveau_joueur.classement = nouveau_classement
        championnat.remove(joueur)  # enleve ancienne position du joueur dans classement
        championnat.append(nouveau_joueur)  # ajoute joueur avec classement actualise

    return championnat


def affichage_classement_championnat(championnat):
    """ affiche joueurs championnat dans ordre classement """
    liste_triee = sorted(championnat, key=lambda x: x.classement)  # tri des joueurs par classement
    print("CLASSEMENT CHAMPIONNAT")
    for joueur in liste_triee:
        print(str(joueur.classement) + ": " + joueur.nom)


def affichage_alphabetique_championnat(championnat):
    """ affiche joueurs championnat par ordre alphabetique """
    liste_triee = sorted(championnat, key=lambda x: x.nom)  # tri des joueurs par nom alphabetique
    print("JOUEURS CHAMPIONNAT PAR ORDRE ALPHABETIQUE")
    for joueur in liste_triee:
        print(joueur.nom)


def affichage_tournois(tournois):
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
            affichage_classement_tournoi(tournoi)
        # affichage joueurs tournoi par ordre aplhabetique
        if choix == 4:
            affichage_alphabetique_tournoi(tournoi)


def modifier_classement_joueur(championnat):
    """ modifier le classement d'un joueur """
    affichage_classement_championnat(championnat)
    championnat = sorted(championnat, key=lambda x: x.classement)  # tri joueurs du championnat par classement
    print("Veuillez indiquer le numéro du joueur à modifier:")
    choix = int(input())
    if choix <= len(championnat):  # test si choix numero joueur valide
        index = choix - 1  # car liste commence a 0
        joueur = championnat[index]
        nouveau_joueur = copy.deepcopy(joueur)
        print("Veuillez indiquer le nouveau classement de " + joueur.nom)
        nouveau_classement = int(input())
        nouveau_joueur.classement = nouveau_classement
        championnat.remove(joueur)  # enleve ancienne position du joueur dans classement
        championnat.append(nouveau_joueur)  # ajoute joueur avec classement actualise
        return championnat
    else:
        print("Numero joueur invalide")
        return


def load_or_save_during_game():
    """ permet de charger ou sauvegarder l'etat du programme au cours d'une partie """
    print("(1) TOUR SUIVANT | (2) SAUVEGARDER | (3) MODIFIER CLASSEMENT JOUEUR")
    choix = int(input())
    return choix


def modifier_classement_joueur_tournoi(joueurs_tournoi, championnat):
    """ modifier le classement d'un joueur pendant un tournoi """
    affichage_classement_championnat(championnat)
    championnat = sorted(championnat, key=lambda x: x.classement)  # tri joueurs du championnat par classement
    print("Veuillez indiquer le numéro du joueur à modifier:")
    choix = int(input())
    if choix <= len(championnat):  # test si choix numero joueur valide
        index = choix - 1  # car liste commence a 0
        joueur = championnat[index]
        nouveau_joueur = copy.deepcopy(joueur)
        print("Veuillez indiquer le nouveau classement de " + joueur.nom)
        nouveau_classement = int(input())
        nouveau_joueur.classement = nouveau_classement
        championnat.remove(joueur)  # enleve ancienne position du joueur dans classement
        joueurs_tournoi.remove(joueur)  # enleve ancienne position du joueur dans tournoi
        championnat.append(nouveau_joueur)  # ajoute joueur avec classement actualise
        joueurs_tournoi.append(nouveau_joueur)  # ajoute joueur classement actualise dans liste participants tournoi
        return joueurs_tournoi, championnat
    else:
        print("Numero joueur invalide")
        return