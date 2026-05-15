from models.atleta import Atleta
from database.conexao import Database
from services.usuarioFactory import UsuarioFactory

class AtletaController:

    def __init__(self):

        self.db = Database()
        self.cursor = self.db.get_cursor()

    def cadastrar_atleta(
        self,
        nome,
        ra,
        curso,
        telefone
    ):

        atleta = UsuarioFactory.criar_usuario(
            "atleta",
            nome,
            ra,
            curso,
            telefone
        )

        self.cursor.execute("""
            INSERT INTO atletas (
                nome,
                ra,
                curso,
                telefone
            )
            VALUES (?, ?, ?, ?)
        """, (
            atleta.nome,
            atleta.ra,
            atleta.curso,
            atleta.telefone
        ))

        self.db.get_connection().commit()

        print("Atleta cadastrado com sucesso!")

        atleta = UsuarioFactory.criar_usuario(
            "atleta",
            nome,
            ra,
            curso,
            telefone
        )

        self.cursor.execute("""
            INSERT INTO atletas (
                nome,
                ra,
                curso,
                telefone
            )
            VALUES (?, ?, ?, ?)
        """, (
            atleta.nome,
            atleta.ra,
            atleta.curso,
            atleta.telefone
        ))

        self.db.get_connection().commit()

        print("Atleta cadastrado com sucesso!")

    def listar_atletas(self):

        self.cursor.execute("""
            SELECT * FROM atletas
        """)

        resultados = self.cursor.fetchall()

        lista_atletas = []

        for atleta in resultados:

            novo_atleta = Atleta(
                id=atleta[0],
                nome=atleta[1],
                ra=atleta[2],
                curso=atleta[3],
                telefone=atleta[4]
            )

            lista_atletas.append(novo_atleta)

        return lista_atletas