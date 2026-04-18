class Salle:
    def __init__(self,code,description,categorie,capacite):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite
    def afficher_info(self):
        print(f"la salle sous le code : {self.code} avec la description : {self.description} {self.categorie} a une capacite de {self.capacite}")