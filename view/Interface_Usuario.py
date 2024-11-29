from controller.ExameController import ExameController
from controller.MedicoController import MedicoController
from controller.PacienteController import PacienteController

class UsuarioInterface:
    def __init__(self, db):
        self.db = db
        self.exame_controller = ExameController(db)
        self.medico_controller = MedicoController(db)
        self.paciente_controller = PacienteController(db)

    def exibir_menu(self):
        while True:
            print("\nEscolha uma opção:" +
            "\n1 - Relatórios"+
            "\n2 - Inserir Documentos"+
            "\n3 - Remover Documentos"+
            "\n4 - Atualizar Documentos"+
            "\n0 - Sair")
            opcao = input("Digite a opção: ")

            if opcao == "1":
                self.gerar_relatorio()
            elif opcao == "2":
                self.inserir_documento()
            elif opcao == "3":
                self.remover_documento()
            elif opcao == "4":
                self.atualizar_documento()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

    def gerar_relatorio(self):
        print("\nEscolha o tipo de relatório:")
        print("1 - Relatório Geral")
        print("2 - Relatório Específico")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            self.relatorio_geral()
        elif opcao == "2":
            self.relatorio_especifico()
        else:
            print("Opção inválida!")

    def relatorio_geral(self):
        # Relatório Geral: Quantos Pacientes e Médicos
        pacientes_count = self.paciente_controller.contar_pacientes()
        medicos_count = self.medico_controller.contar_medicos()
        
        print(f"\nRelatório Geral:")
        print(f"Quantidade de Pacientes: {pacientes_count}")
        print(f"Quantidade de Médicos: {medicos_count}")

    def relatorio_especifico(self):
        print("\nEscolha o tipo de relatório específico:")
        print("1 - Relatório de Pacientes")
        print("2 - Relatório de Médicos")
        print("3 - Relatório de Exames")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            self.paciente_controller.listar_pacientes_detalhados()
        elif opcao == "2":
            self.medico_controller.listar_medicos_detalhados()
        elif opcao == "3":
            self.exame_controller.listar_exames_detalhados()
        else:
            print("Opção inválida!")

    def inserir_documento(self):
        print("\nInserir Documento:")
        print("1 - Inserir Paciente")
        print("2 - Inserir Médico")
        print("3 - Inserir Exame")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            self.paciente_controller.inserir_paciente()
        elif opcao == "2":
            self.medico_controller.inserir_medico()
        elif opcao == "3":
            self.exame_controller.inserir_exame()
        else:
            print("Opção inválida!")

    def remover_documento(self):
        print("\nRemover Documento:")
        print("1 - Remover Paciente")
        print("2 - Remover Médico")
        print("3 - Remover Exame")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            self.paciente_controller.remover_paciente()
        elif opcao == "2":
            self.medico_controller.remover_medico()
        elif opcao == "3":
            self.exame_controller.remover_exame()
        else:
            print("Opção inválida!")

    def atualizar_documento(self):
        print("\nAtualizar Documento:")
        print("1 - Atualizar Paciente")
        print("2 - Atualizar Médico")
        print("3 - Atualizar Exame")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            self.paciente_controller.atualizar_paciente()
        elif opcao == "2":
            self.medico_controller.atualizar_medico()
        elif opcao == "3":
            self.exame_controller.atualizar_exame()
        else:
            print("Opção inválida!")
