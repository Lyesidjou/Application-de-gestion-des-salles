from Data.dao_salle import DataSalle
from Data.dao_salle import Salle


con= DataSalle().get_connection()
print(con)
con.close()

S1=Salle("BK098","Grande","Conference",70)
S2=Salle("GF987","Moyenne","RÉSEAUTIQUE",40)
DataSalle().insert_salle(S1)
DataSalle().insert_salle(S2)