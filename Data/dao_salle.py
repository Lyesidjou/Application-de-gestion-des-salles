import json
import mysql.connector
from Models.salle import Salle

class DataSalle:
    def get_connection(self):
        with open("Data/config.json","r",encoding="utf-8") as f:
            config = json.load(f)
            connexion = mysql.connector.connect(
                host=config["host"],
                user=config["user"],
                password=config["password"],
                database=config["database"],
            )
            return connexion

    def insert_salle(self,salle):
        con= self.get_connection()
        crs= con.cursor()
        crs.execute(
            "INSERT INTO salle (code,description,categorie,capacite) VALUES (%s,%s,%s,%s)",
            (salle.code,salle.description,salle.categorie,salle.capacite)
        )
        con.commit()
        crs.close()
        con.close()

    def update_salle(self,salle):
        con= self.get_connection()
        crs= con.cursor()
        crs.execute(
            "UPDATE salle SET description=%s,categorie=%s,capacite=%s WHERE code=%s",
            (salle.description,salle.categorie,salle.capacite,salle.code)
        )
        con.commit()
        crs.close()
        con.close()

    def delete_salle(self,code):
        con= self.get_connection()
        crs= con.cursor()
        crs.execute(
            "DELETE FROM salle WHERE code=%s",
            (code,)
        )
        con.commit()
        crs.close()
        con.close()

    def get_salle(self,code):
        con= self.get_connection()
        crs= con.cursor()
        crs.execute(
            "SELECT * FROM salle WHERE code=%s",
            (code,)
        )
        salle = crs.fetchone()
        crs.close()
        con.close()
        return salle

    def get_salles(self):
        con= self.get_connection()
        crs= con.cursor()
        crs.execute(
            "SELECT * FROM salle ORDER BY code"
        )
        salles = crs.fetchall()
        crs.close()
        con.close()
        return salles










