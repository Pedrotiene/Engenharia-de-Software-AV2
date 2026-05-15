from models.atleta import Atleta


class UsuarioFactory:

    @staticmethod
    def criar_usuario(
        tipo,
        nome,
        ra,
        curso,
        telefone
    ):

        if tipo == "atleta":

            return Atleta(
                nome,
                ra,
                curso,
                telefone
            )

        else:
            raise ValueError(
                "Tipo de usuário inválido!"
            )