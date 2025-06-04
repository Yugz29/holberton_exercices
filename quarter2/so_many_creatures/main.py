import csv
import json

# Import des classes
from centaure import Centaure
from acromentule import Acromentule
from detraqueur import Detraqueur
from dragon import Dragon
from elfedemaison import ElfeDeMaison

def lire_csv():
    """Lit le fichier CSV et retourne les données"""
    try:
    # A completer    
    except FileNotFoundError:
        print(f"Erreur : Le fichier {} n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return []
    #TODO: Créer une fonction qui prend un paramètre nom_fichier. Cette fonction permettra de lire un fichier CSV et récupérer ces informations. Retournez une LISTE (avec la fonction liste) contenant toutes les informations des différentes créatures stockées dans le CSV.
    #TIPS: Utiliser la classe csv.DictReader

def creer_creature(type_creature, donnees):
    """Crée une instance de créature selon son type"""
    try:
        if type_creature == "Centaure":
            return Centaure(
                nom=donnees['nom'],
                force=donnees['attribut1'],
                agilite=donnees['attribut2'],
                age=donnees['attribut4']
            )
        elif type_creature == "Acromentule":
            return Acromentule(
                nom=donnees['nom'],
                taille=donnees['attribut1'],
                venin=donnees['attribut2'],
                nombre_pattes=donnees['attribut3'],
                territoire=donnees['attribut4']
            )
        elif type_creature == "Détraqueur":
            return Detraqueur(
                nom=donnees['nom'],
                puissance_aspiration=donnees['attribut1'],
                lieu_garde=donnees['attribut2'],
                dangerosite=donnees['attribut3']
            )
        elif type_creature == "Dragon":
            return Dragon(
                nom=donnees['nom'],
                type_dragon=donnees['attribut1'],
                souffle=donnees['attribut2'],
                tresor=donnees['attribut3'],
                age=donnees['attribut4']
            )
        elif type_creature == "Elfe de maison":
            return ElfeDeMaison(
                nom=donnees['nom'],
                maitre=donnees['attribut1'],
                loyaute=donnees['attribut2'],
                magie_domestique=donnees['attribut3']
            )
        else:
            print(f"Type de créature inconnu : {type_creature}")
            return None
    except Exception as e:
        print(f"Erreur lors de la création de la créature {type_creature} : {e}")
        return None

def sauvegarder_json(creatures, nom_fichier):
    """Sauvegarde les créatures dans un fichier JSON"""
    try:
        #TODO: Compléter la fonction pour sauvegarder les données de la liste creatures dans un fichir json nommé data.json
        
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

def main():
    #TODO: Compléter la fonction main qui utilisera la fonction lire_csv() et sauvegarder_json()

if __name__ == "__main__":
    main()
