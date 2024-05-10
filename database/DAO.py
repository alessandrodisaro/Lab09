from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAeroporti():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                    from airports"""

        cursor.execute(query,())
        results = []
        if cursor is None:
            print("cursore vuoto")
            return
        else:
            for row in cursor:
                results.append(Aeroporto(row["ID"], row["IATA_CODE"], row["AIRPORT"]))

        cursor.close()
        cnx.close()
        return results

    @staticmethod
    def getAllVoli(distanza):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                    from flights f 
                    where DISTANCE > %s"""

        cursor.execute(query, (distanza,))
        results = []
        if cursor is None:
            print("cursore vuoto")
            return
        else:
            for row in cursor:
                results.append(row)

        cursor.close()
        cnx.close()
        return results




