from datetime import date
from config import connection


class Lancamento:
    id: int
    tipo: int
    data: date
    observacao: str
    valor: float
    
    def toTuple(lancamento):
        return (lancamento.id, lancamento.tipo, lancamento.data, lancamento.observacao, lancamento.valor)

    def inserir(lancamento):
        cursor = connection.cursor()
        sql = f"""
            INSERT INTO lancamentos (lancamento) 
            VALUES ('{lancamento.tipo, lancamento.data, lancamento.observacao, lancamento.valor}')
            """

        cursor.execute(sql)

        last_id = cursor.lastrowid

        connection.commit()
        cursor.close()
        connection.close()
        return last_id

    def update(lancamento):
        cursor = connection.cursor()
        sql = """
            UPDATE lancamentos
            SET lancamento = ?
            WHERE id = ?
        """
        data = lancamento.toTuple(lancamento)
        cursor.execute(sql, data)

        rows_affecteds = cursor.rowcount
        cursor.close()
        connection.close()

        return rows_affecteds

    def delete(lancamento):
        cursor = connection.cursor()
        sql = """
            DELETE lancamentos
            WHERE id = ?
        """
        data = (lancamento.id)
        cursor.execute(sql, data)

        rows_affecteds = cursor.rowcount
        cursor.close()
        connection.close()

        return rows_affecteds

    def selectAll():
        cursor = connection.cursor()

        cursor.execute("select * from lancamento")
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    def selectById(id):
        cursor = connection.cursor()

        cursor.execute("""
                       select id, lancamento
                       from lancamentos
                       where id = ?""", (id))
        results = cursor.fetchall()

        lancamento = lancamento()
        for result in results:
            lancamento.id = result[0]
            lancamento.lancamento = result[2]

        cursor.close()
        connection.close()

        return lancamento