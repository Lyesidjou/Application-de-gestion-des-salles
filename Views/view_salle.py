import customtkinter as ctk
from Services.service_salle import ServiceSalle
from Models.salle import Salle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.service_salle=ServiceSalle()
        self.title("Gestion des salles")
        self.geometry("900x500")
        ctk.set_appearance_mode("light")

        self.frame=ctk.CTkFrame(self)
        self.frame.pack(padx=5, pady=5,fill='x')

        self.label_code=ctk.CTkLabel(self.frame,text="Code")
        self.label_code.grid(row=0,column=0,padx=5,pady=5,sticky="w")
        self.entry_code=ctk.CTkEntry(self.frame, placeholder_text="code")
        self.entry_code.grid(row=0,column=1,padx=5,pady=5)

        self.label_description=ctk.CTkLabel(self.frame,text="Description")
        self.label_description.grid(row=1,column=0,padx=5,pady=5,sticky="w")
        self.entry_description=ctk.CTkEntry(self.frame,placeholder_text="description")
        self.entry_description.grid(row=1,column=1,padx=5,pady=5)

        self.label_categorie=ctk.CTkLabel(self.frame,text="Categorie")
        self.label_categorie.grid(row=2,column=0,padx=5,pady=5,sticky="w")
        self.entry_categorie=ctk.CTkEntry(self.frame,placeholder_text="categorie")
        self.entry_categorie.grid(row=2,column=1,padx=5,pady=5)

        self.label_capacite=ctk.CTkLabel(self.frame,text="Capacite")
        self.label_capacite.grid(row=3,column=0,padx=5,pady=5,sticky="w")
        self.entry_capacite=ctk.CTkEntry(self.frame,placeholder_text="capacite")
        self.entry_capacite.grid(row=3,column=1,padx=5,pady=5)

        self.frame_action=ctk.CTkFrame(self)
        self.frame_action.pack(padx=5,pady=5,fill='x')

        self.btn_Ajouter=ctk.CTkButton(self.frame_action,text="Ajouter", command=self.ajouter_salle)
        self.btn_Ajouter.grid(row=0,column=0,padx=5,pady=5)

        self.btn_Modifier=ctk.CTkButton(self.frame_action,text="Modifier", command=self.modifier_salle)
        self.btn_Modifier.grid(row=0,column=1,padx=5,pady=5)

        self.btn_Supprimer=ctk.CTkButton(self.frame_action,text="Supprimer")
        self.btn_Supprimer.grid(row=0,column=2,padx=5,pady=5)



        self.btn_Rechercher=ctk.CTkButton(self.frame_action,text="Rechercher")
        self.btn_Rechercher.grid(row=0,column=3,padx=5,pady=5)

    def ajouter_salle(self ):
        code=self.entry_code.get()
        description=self.entry_description.get()
        categorie=self.entry_categorie.get()
        capacite=self.entry_capacite.get()
        salle=Salle(code,description,categorie,capacite)
        self.service_salle.ajouter_salle(salle)

    def modifier_salle(self):
        code=self.entry_code.get()
        description=self.entry_description.get()
        categorie=self.entry_categorie.get()
        capacite=self.entry_capacite.get()
        salle=Salle(code,description,categorie,capacite)
        self.service_salle.modifier_salle(salle)


