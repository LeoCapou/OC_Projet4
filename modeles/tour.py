class Tour:

    def __init__(self, nom, date_debut, heure_debut, date_fin, heure_fin):
        self.nom = nom
        self.date_debut = date_debut
        self.heure_debut = heure_debut
        self.date_fin = date_fin
        self.heure_fin = heure_fin
        self.matchs = []

    def ajouterMatch(self, match):
        self.matchs.append(match)