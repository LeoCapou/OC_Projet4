import copy
from modeles.joueur import Joueur

class ModificationJoueur:

    def ajout_joueur(self):
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


    def maj_classement(self, joueurs_tournoi, championnat):
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


    def modifier_classement_joueur(self, championnat, rapport):
        """ modifier le classement d'un joueur """
        rapport.affichage_classement_championnat(championnat)
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


    def modifier_classement_joueur_tournoi(self, joueurs_tournoi, championnat, rapport):
        """ modifier le classement d'un joueur pendant un tournoi """
        rapport.affichage_classement_championnat(championnat)
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