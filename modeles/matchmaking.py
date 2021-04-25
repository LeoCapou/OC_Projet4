import copy
from modeles.match import Match

class MatchMaking:

    def matchmaking_premier_tour(self, joueurs, tour):
        """ tri des joueurs en fonction de leur classement """
        liste_globale_triee = sorted(joueurs, key=lambda x: x.classement, reverse=False)  # tri joueurs par classement
        # division en deux listes
        liste_superieure = liste_globale_triee[0:int(len(liste_globale_triee)/2)]
        liste_inferieure = liste_globale_triee[int(len(liste_globale_triee)/2):len(liste_globale_triee)]
        # associations des paires de joueurs
        for i in range(int(len(liste_globale_triee)/2)):
            match = Match(liste_superieure[i], 0, liste_inferieure[i], 0)
            # ajout joueur affronte
            liste_superieure[i].joueurs_affrontes.add(liste_inferieure[i])
            liste_inferieure[i].joueurs_affrontes.add(liste_superieure[i])
            tour.ajouterMatch(match)
        print("les matchs du premier tour sont les suivants")
        for m in tour.matchs:
            print(m.joueur1[0].nom + " vs " + m.joueur2[0].nom)

        return tour


    def matchmaking(self, joueurs, tour):
        """ association des joueurs en fonction de leur score """
        liste_globale_triee = sorted(joueurs, key=lambda x: x.total_points, reverse=True)  # tri joueurs par total_points
        scores_egalite = []
        # creation liste des total_points a egalite
        for joueur in liste_globale_triee:
            joueurs_egalite = [x for x in liste_globale_triee if x.total_points == joueur.total_points]
            if len(joueurs_egalite) > 1:
                if joueur.total_points not in scores_egalite:
                    scores_egalite.append(joueur.total_points)
        # tri des joueurs a egalite de total_points par classement
        if len(scores_egalite) > 0:
            for indice_score in range(len(scores_egalite)):
                liste_joueurs_exaequo = [x for x in liste_globale_triee if x.total_points == scores_egalite[indice_score]]
                liste_joueurs_exaequo_triee = sorted(liste_joueurs_exaequo, key=lambda x: x.classement, reverse=False)
                for j in liste_globale_triee:
                    if j.total_points == scores_egalite[indice_score]:
                        position = liste_globale_triee.index(j)
                        for i in range(len(liste_joueurs_exaequo_triee)):
                            test = position + i
                            liste_globale_triee[test] = liste_joueurs_exaequo_triee[i]
                        break
        # associations des paires de joueurs
        matchs = self.association_paire_match(liste_globale_triee)
        print("MATCHS")
        for match in matchs:
            tour.ajouterMatch(match)
            match.joueur1[0].joueurs_affrontes.add(match.joueur2[0])
            match.joueur2[0].joueurs_affrontes.add(match.joueur1[0])
            print(match.joueur1[0].nom + " vs " + match.joueur2[0].nom)

        return tour


    def association_paire_match(self, liste_joueurs_triee):
        """ association des joueurs en fonction de leur score en evitant de rejouer contre meme joueur """
        matchs = []
        copy_list = liste_joueurs_triee.copy()
        for joueur in liste_joueurs_triee:
            for player in copy_list:
                if joueur in copy_list:
                    # verifie si a deja joue contre joueur qui suit au classement
                    copy_joueur = copy_list[copy_list.index(joueur)]
                    joueur_suivant = copy_list[copy_list.index(joueur)+1]
                    if copy_joueur not in joueur_suivant.joueurs_affrontes:  # joueur et joueur suivant pas affrontes
                        match = Match(copy_joueur, 0, joueur_suivant, 0)
                        matchs.append(match)
                        copy_list.remove(copy_joueur)
                        copy_list.remove(joueur_suivant)
                    else:  # joueur et joueur suivant deja affrontes
                        position_joueur_suivant_2 = copy_list.index(joueur)+2
                        if position_joueur_suivant_2 < len(copy_list):  # si il existe joueur + 2
                            joueur_suivant_2 = copy_list[copy_list.index(joueur)+2]
                            if copy_joueur not in joueur_suivant_2.joueurs_affrontes:  # joueur/suivant 2 pas affrontes
                                match = Match(copy_joueur, 0, joueur_suivant_2, 0)
                                matchs.append(match)
                                copy_list.remove(copy_joueur)
                                copy_list.remove(joueur_suivant_2)
                            else:  # joueur et joueur suivant 2 deja affrontes, joueur affronte joueur suivant
                                match = Match(copy_joueur, 0, joueur_suivant, 0)
                                matchs.append(match)
                                copy_list.remove(copy_joueur)
                                copy_list.remove(joueur_suivant)
                        else:  # joueur suivant 2 existe pas, joueur affronte joueur suivant
                            match = Match(copy_joueur, 0, joueur_suivant, 0)
                            matchs.append(match)
                            copy_list.remove(copy_joueur)
                            copy_list.remove(joueur_suivant)

        return matchs    