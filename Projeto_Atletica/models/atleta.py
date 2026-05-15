class Atleta:

    def __init__(
        self,
        nome,
        ra,
        curso,
        telefone,
        id=None
    ):

        self.id = id
        self.nome = nome
        self.ra = ra
        self.curso = curso
        self.telefone = telefone

    def __str__(self):

        return (
            f"Atleta: {self.nome} | "
            f"RA: {self.ra} | "
            f"Curso: {self.curso}"
        )