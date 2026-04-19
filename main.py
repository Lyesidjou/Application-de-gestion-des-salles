from Data.dao_salle import DataSalle
from Data.dao_salle import Salle
from Services.service_salle import ServiceSalle
from Views.view_salle import ViewSalle



con= DataSalle().get_connection()
print(con)
con.close()

S1=Salle("BK098","Grande","Conference",70)
S2=Salle("GF987","Moyenne","RÉSEAUTIQUE",40)
S3=Salle("VVS4","Petite","LANGUES",20)
DataSalle().insert_salle(S1)
DataSalle().insert_salle(S2)
DataSalle().insert_salle(S3)
DataSalle().delete_salle("BK098")

S2.description="Petite"
S2.categorie="MATH"
S2.capacite=35
DataSalle().update_salle(S2)

salle=DataSalle().get_salle("VVS4")
print(salle)

salles=DataSalle().get_salles()
for i in salles:
    print(i)

salles=ServiceSalle().recuperer_salles()
for i in salles:
    print(i)

S4=Salle("NM78","Grande","RÉUNION",80)
ServiceSalle().ajouter_salle(S4)

S4.description="Petite"
S4.category="PRESENTATION"
S4.capacite=30
ServiceSalle().modifier_salle(S4)

ServiceSalle().supprimer_salle("VVS4")

salle=ServiceSalle().rechercher_salle("GF987")
print(salle)

app=ViewSalle()
app.mainloop()

