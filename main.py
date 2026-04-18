from Data.dao_salle import DataSalle


con= DataSalle().get_connection()
print(con)
con.close()