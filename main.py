from Data.dao_salle import DataSalle
from Data.dao_salle import Salle


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
