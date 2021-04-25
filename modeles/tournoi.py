class Tournoi:

    nb_tours = 4
    instances = []

    def __init__(self, nom, lieu, date, description, joueurs):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.tours = []
        self.joueurs = joueurs
        self.description = description
        self.instances.append(self)

    def ajouterTour(self, tour):
        self.tours.append(tour)

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)