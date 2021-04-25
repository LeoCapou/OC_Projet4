class MenuAcceuil:

    def menu_acceuil(self):
        """ choix nouveau tournoi ou ajouter joueurs """
        print("| NOUVEAU TOURNOI (1) | AJOUTER JOUEUR CHAMPIONNAT (2) | MODIFIER CLASSEMENT JOUEUR (3) |" +
            " CHARGER DONNEES (4) | AFFICHER RAPPORT (5) | SAUVEGARDER (6) | EXIT (0) |")
        choix = int(input())
        return choix    