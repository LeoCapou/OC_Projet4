import copy
from modeles.joueur import Joueur
from modeles.tournoi import Tournoi
from modeles.match import Match
from modeles.tour import Tour

class Database:

    def serialize_player(self,joueur):
        """ serialize un joueur """
        serialized_player = {
                'nom': joueur.nom,
                'prenom': joueur.prenom,
                'birthday': joueur.birthday,
                'sexe': joueur.sexe,
                'classement': joueur.classement,
                'total_points': joueur.total_points
            }
        return serialized_player


    def serialize_match(self,match):
        """ serialize un match """
        serialized_match = {
                'joueur1': self.serialize_player(match.joueur1[0]),
                'score1': match.joueur1[1],
                'joueur2': self.serialize_player(match.joueur2[0]),
                'score2': match.joueur2[1]
            }
        return serialized_match


    def serialize_tour(self,tour):
        """ serialize un tour """
        serialized_matchs = []
        for match in tour.matchs:
            serialized_match = self.serialize_match(match)
            serialized_matchs.append(serialized_match)
        serialized_tour = {
                'nom': tour.nom,
                'date_debut': tour.date_debut,
                'heure_debut': tour.heure_debut,
                'date_fin': tour.heure_debut,
                'heure_fin': tour.heure_fin,
                'matchs': serialized_matchs
            }
        return serialized_tour


    def db_save_championnat(self, db, championnat):
        """ sauvegarde championnat dans base de donnees """
        players_table = db.table('players')
        players_table.truncate()
        for joueur in championnat:
            serialized_player = self.serialize_player(joueur)
            players_table.insert(serialized_player)

        return db


    def db_load_championnat(self, db):
        """ retourne championnat a partir de base de donnees """
        serialized_players = db.table('players').all()
        championnat = []
        for player in serialized_players:
            joueur = Joueur(player['nom'], player['prenom'], player['birthday'], player['sexe'], player['classement'])
            championnat.append(joueur)
        return championnat


    def db_save_tournois(self, db, tournois):
        """ sauvegarde championnat dans base de donnees """
        tournois_table = db.table('tournois')
        tournois_table.truncate()
        for tournoi in tournois:
            serialized_players = []
            for joueur in tournoi.joueurs:
                serialized_player = self.serialize_player(joueur)
                serialized_players.append(serialized_player)
            serialized_tours = []
            for tour in tournoi.tours:
                serialized_tour = self.serialize_tour(tour)
                serialized_tours.append(serialized_tour)
            serialized_tournoi = {
                'nom': tournoi.nom,
                'lieu': tournoi.lieu,
                'date': tournoi.date,
                'description': tournoi.description,
                'joueurs': serialized_players,
                'tours': serialized_tours
            }
            tournois_table.insert(serialized_tournoi)

        return db


    def db_load_tournois(self, db):
        """ retourne liste tournois a partir de base de donnees """
        serialized_tournois = db.table('tournois').all()
        deserialized_tournois = []
        for tournoi in serialized_tournois:
            deserialized_joueurs = []  # remise a zero liste joueurs tournoi
            # deserialization de chaque joueur du tournoi
            for joueur in tournoi['joueurs']:
                deserialized_joueur = Joueur(joueur['nom'], joueur['prenom'],
                                            joueur['birthday'], joueur['sexe'], joueur['classement'])
                deserialized_joueur.total_points = joueur['total_points']
                deserialized_joueurs.append(deserialized_joueur)
            # creation instance Tournoi
            deserialized_tournoi = Tournoi(tournoi['nom'], tournoi['lieu'], tournoi['date'],
                                        tournoi['description'], deserialized_joueurs)
            # deserialization tours du tournoi
            for tour_serialized in tournoi['tours']:
                tour = Tour(tour_serialized['nom'], tour_serialized['date_debut'], tour_serialized['heure_debut'],
                            tour_serialized['date_fin'], tour_serialized['heure_fin'])
                for match_serialized in tour_serialized['matchs']:
                    joueur1_serialized = match_serialized['joueur1']
                    joueur2_serialized = match_serialized['joueur2']
                    joueur1 = Joueur(joueur1_serialized['nom'], joueur1_serialized['prenom'],
                                    joueur1_serialized['birthday'], joueur1_serialized['sexe'],
                                    joueur1_serialized['classement'])
                    joueur2 = Joueur(joueur2_serialized['nom'], joueur2_serialized['prenom'],
                                    joueur2_serialized['birthday'], joueur2_serialized['sexe'],
                                    joueur2_serialized['classement'])
                    match = Match(joueur1, match_serialized['score1'], joueur2, match_serialized['score2'])
                    tour.matchs.append(match)
                # ajout tour deserialized a l'instance Tournoi
                deserialized_tournoi.tours.append(tour)
            # ajout tournoi deserialized a la liste des tournois
            deserialized_tournois.append(deserialized_tournoi)
        return deserialized_tournois


    def save_tournoi(self, tournoi):
        """ retourne tournoi avec copie des instances de joueurs """
        copy_joueurs = []
        for joueur in tournoi.joueurs:
            copy_joueur = copy.deepcopy(joueur)
            copy_joueurs.append(copy_joueur)
        tournoi.joueurs = copy_joueurs
        return tournoi