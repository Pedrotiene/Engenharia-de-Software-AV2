from controllers.atletaController import AtletaController


class MenuView:

    def __init__(self):

        self.controller = AtletaController()

    def exibir_menu(self):

        while True:

            print("\n=== SISTEMA ATLÉTICA ===")
            print("1 - Cadastrar atleta")
            print("2 - Listar atletas")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_atleta()

            elif opcao == "2":
                self.listar_atletas()

            elif opcao == "0":
                print("Encerrando sistema...")
                break

            else:
                print("Opção inválida!")

    def cadastrar_atleta(self):

        print("\n=== CADASTRO DE ATLETA ===")

        nome = input("Nome: ")
        ra = input("RA: ")
        curso = input("Curso: ")
        telefone = input("Telefone: ")

        self.controller.cadastrar_atleta(
            nome,
            ra,
            curso,
            telefone
        )

    def listar_atletas(self):

        print("\n=== LISTA DE ATLETAS ===")

        atletas = self.controller.listar_atletas()

        if len(atletas) == 0:
            print("Nenhum atleta cadastrado.")
            return

        for atleta in atletas:
            print(atleta)