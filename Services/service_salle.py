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

    def modifier_salle(self,salle):
        if not salle.code or not salle.description or not salle.categorie or not salle.capacite:
            print("toutes les données de la salle doivent etre presente")
            return False
        if salle.capacite < 1:
            print("la capacité de la salle est strictement supérieure ou égale à 1")
            return False
        self.dao_salle.update_salle(salle)
        print("toutes les conditions sont respectés les informations de la salle sont modifier")
        return True

    def  supprimer_salle(self,code):
        self.dao_salle.delete_salle(code)
        print("salle supprimé")

    def  rechercher_salle(self,code):
        salle=self.dao_salle.get_salle(code)
        if salle is None:
            print("il n'existe presentement aucune salle sous ce code")
            return None
        return salle

    def recuperer_salles(self):
        salles=self.dao_salle.get_salles()
        return salles










