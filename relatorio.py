from datetime import date
from config import connection


class Relatorio:
    id: int
    data: date
    saldo: float
    
    def toTuple(relatorio):
        return (relatorio.id, relatorio.data, relatorio.saldo)
    
    def selectAll():
        cursor = connection.cursor()

        cursor.execute("select * from relatorio")
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results
    
    