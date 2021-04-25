# Développez un programme logiciel en Python

Quatrieme projet de la formation "Développeur d'application - Python" d'OpenClassrooms dont le but est de développer un logiciel de gestion de tournois d'echec. Ce logiciel doit permettre aux gestionnaires de:
- ajouter de nouveaux joueurs au championnat
- créer de nouveaux tournois
- gérer le matchmaking de ces tournois
- gérer les différents classements
- sauvegarder toutes ces données dans une base de données
- charger ces informations depuis une base de donnée
- afficher des rapports

## Pour commencer

Ces instructions vous permettent de récupérer une copie du projet pour le tester sur votre machine.

### Prerequis

Ce programme étant basé sur Python, il est nécessaire que celui-ci soit installé sur votre machine.
Vous pouvez télécharger Python [ici](https://www.python.org/downloads/)

### Installation

Pour ne pas entrer en conflit avec d'autres projets déjà existants, il est préférable d'exécuter le programme sous un environnement virtuel.

Voici les principales commandes pour:

1. créer l'environnement virtuel

```
python3 -m venv tutorial-env
```
2. activer l'environnement virtuel

```
tutorial-env\Scripts\activate.bat
```

Pour plus de détails sur l'installation d'un environnement virtuel, se reporter à [la documentation Python](https://docs.python.org/fr/3.6/tutorial/venv.html)

Il est également nécessaire d'installer les bibliothèques indispensables au bon fonctionnement du programme. 
Celles-ci sont listées dans le document `requirement.txt` et leur installation se fait via la commande suivante exécutée dans l'environnement virtuel que vous venez de créer:
```
pip install -r requirements.txt
```

## Exécution du programme

Une fois la console placée dans le dossier du programme, il suffit d'exécuter la commande suivante dans l'environnement virtuel:
```
python3 controleur.py
```
Un fichier `db.json` est créé: ce fichier correspond à la base de données dans laquelle vous pourrez sauvegarder l'état du programme ou à partir de laquelle vous pourrez importer des données. Il est déconseillé de la manipuler manuellement au risque de corrompre son formatage et empêcher sa lecture.

Vous êtes par la suite emmené à suivre les instructions affichées sur le terminal. Il vous sera demandé d'entrer des informations dans la console du terminal pour naviguer dans le programme.

## Rapport flake8

Pour vous assurer de la bonne conformité du code aux directives PEP 8, vous pouvez générer un rapport grâce à l'outil flak8. Le fichier `setup.cfg` contient le nombre maximal de caractère par ligne que doit prendre en compte flake8 pour générer le rapport.
Vous pouvez générer le rapport grâce à la commande suivante:
```
flake8 --format=html --htmldir=flake-report
```
Un dossier "flake-report" est créé. Il contient un rapport au format html pour chaque fichier python analysé.

## Auteur

**Léo CAPOU** 

## Remerciements

* Tim