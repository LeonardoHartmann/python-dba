from config import connection


class Tipo:
    id: int
    tipo: str

    def toTuple(tipo):
        return (tipo.id, tipo.tipo)

    def inserir(tipo):
        cursor = connection.cursor()
        sql = f"""
            INSERT INTO tipo (tipo) 
            VALUES ('{tipo.tipo}')
            """

        cursor.execute(sql)

        last_id = cursor.lastrowid

        connection.commit()
        cursor.close()
        connection.close()
        return last_id

    def update(tipo):
        cursor = connection.cursor()
        sql = """
            UPDATE tipo
            SET tipo = ?
            WHERE id = ?
        """
        data = tipo.toTuple(tipo)
        cursor.execute(sql, data)

        rows_affecteds = cursor.rowcount
        cursor.close()
        connection.close()

        return rows_affecteds


    def selectAll():
        cursor = connection.cursor()

        cursor.execute("select * from tipo")
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    def selectById(id):
        cursor = connection.cursor()

        cursor.execute("""
                       select id, tipo 
                       from tipo 
                       where id = ?""", (id))
        results = cursor.fetchall()

        tipo = Tipo()
        for result in results:
            tipo.id = result[0]
            tipo.tipo = result[2]

        cursor.close()
        connection.close()

        return tipo

    def delete(tipo):
        cursor = connection.cursor()
        sql = """
            DELETE tipo
            WHERE id = ?
        """
        data = (tipo.id)
        cursor.execute(sql, data)

        rows_affecteds = cursor.rowcount
        cursor.close()
        connection.close()

        return rows_affecteds
