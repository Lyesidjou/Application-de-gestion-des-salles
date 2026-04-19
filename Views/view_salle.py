import customtkinter as ctk
from Services.service_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.service_salle=ServiceSalle()
        self.title("Gestion des salles")
        self.geometry("900x500")
        ctk.set_appearance_mode("light")
