from database.connection import get_connection

class SessaoRepository:

    def salvar(self, sessao):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO sessoes (filme_id, cinema_id, data, horario, publico)
        VALUES (?, ?, ?, ?, ?)
        """, (
            sessao.filme_id,
            sessao.cinema_id,
            sessao.data,
            sessao.horario,
            sessao.publico
        ))

        connection.commit()
        connection.close()