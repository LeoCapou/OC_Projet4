import copy


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


class Match:

    def __init__(self, joueur1, score1, joueur2, score2):
        self.joueur1 = [joueur1, score1]
        self.joueur2 = [joueur2, score2]


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


def matchmaking_premier_tour(joueurs, tour):
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


def matchmaking(joueurs, tour):
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
    matchs = association_paire_match(liste_globale_triee)
    print("MATCHS")
    for match in matchs:
        tour.ajouterMatch(match)
        match.joueur1[0].joueurs_affrontes.add(match.joueur2[0])
        match.joueur2[0].joueurs_affrontes.add(match.joueur1[0])
        print(match.joueur1[0].nom + " vs " + match.joueur2[0].nom)

    return tour


def association_paire_match(liste_joueurs_triee):
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


def serialize_player(joueur):
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


def serialize_match(match):
    """ serialize un match """
    serialized_match = {
            'joueur1': serialize_player(match.joueur1[0]),
            'score1': match.joueur1[1],
            'joueur2': serialize_player(match.joueur2[0]),
            'score2': match.joueur2[1]
        }
    return serialized_match


def serialize_tour(tour):
    """ serialize un tour """
    serialized_matchs = []
    for match in tour.matchs:
        serialized_match = serialize_match(match)
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


def db_save_championnat(db, championnat):
    """ sauvegarde championnat dans base de donnees """
    players_table = db.table('players')
    players_table.truncate()
    for joueur in championnat:
        serialized_player = serialize_player(joueur)
        players_table.insert(serialized_player)

    return db


def db_load_championnat(db):
    """ retourne championnat a partir de base de donnees """
    serialized_players = db.table('players').all()
    championnat = []
    for player in serialized_players:
        joueur = Joueur(player['nom'], player['prenom'], player['birthday'], player['sexe'], player['classement'])
        championnat.append(joueur)
    return championnat


def db_save_tournois(db, tournois):
    """ sauvegarde championnat dans base de donnees """
    tournois_table = db.table('tournois')
    tournois_table.truncate()
    for tournoi in tournois:
        serialized_players = []
        for joueur in tournoi.joueurs:
            serialized_player = serialize_player(joueur)
            serialized_players.append(serialized_player)
        serialized_tours = []
        for tour in tournoi.tours:
            serialized_tour = serialize_tour(tour)
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


def db_load_tournois(db):
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


def save_tournoi(tournoi):
    """ retourne tournoi avec copie des instances de joueurs """
    copy_joueurs = []
    for joueur in tournoi.joueurs:
        copy_joueur = copy.deepcopy(joueur)
        copy_joueurs.append(copy_joueur)
    tournoi.joueurs = copy_joueurs
    return tournoi