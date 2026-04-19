from mysql.connector.constants import flag_is_set

from Data.dao_salle import DataSalle
from Models.salle import Salle

class ServiceSalle:
    def __init__(self):
        self.dao_salle=DataSalle()

    def ajouter_salle(self,salle):
        if not salle.code or not salle.description or not salle.categorie or not salle.capacite:
            print("toutes les données de la salle doivent etre presente")
            return False
        if salle.capacite < 1:
            print(" la capacité de la salle est strictement supérieure ou égale à 1")
            return False
        self.dao_salle.insert_salle(salle)
        print("toutes les conditions sont respectés et la salle vient d'etre ajouter")
        return True





