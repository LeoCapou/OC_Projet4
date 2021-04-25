class Joueur:

    instances = []

    def __init__(self, nom, prenom, birthday, sexe, classement):
        self.nom = nom
        self.prenom = prenom
        self.birthday = birthday
        self.sexe = sexe
        self.classement = classement
        self.total_points = 0
        self.instances.append(self)
        self.joueurs_affrontes = set()