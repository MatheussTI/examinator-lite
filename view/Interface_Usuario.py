import csv

class InterfaceUsuario:
    def __init__(self, exame_controller, paciente_controller, medico_controller, splash_screen):
        self.exame_controller = exame_controller
        self.paciente_controller = paciente_controller
        self.medico_controller = medico_controller
        self.splash_screen = splash_screen

    def mostrar_contagem_registros(self):
        print("\n-------------------- Listagem Geral --------------------")
        print(f"TOTAL DE REGISTROS: ")
        print(f"1. Exames:     {str(self.splash_screen.get_documents_count('exames')).rjust(6)}")
        print(f"2. Pacientes:  {str(self.splash_screen.get_documents_count('pacientes')).rjust(5)}")
        print(f"3. Médicos:    {str(self.splash_screen.get_documents_count('medicos')).rjust(5)}")
        print("--------------------------------------------------------")

    def menu_principal(self):
        """Menu principal do sistema"""
        while True:
            print("\nMenu Principal:" +
                  "\n1. Acessar Exames" +
                  "\n2. Acessar Pacientes" +
                  "\n3. Acessar Médicos" +
                  "\n4. Relatórios" +
                  "\n5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.menu_exames()
            elif opcao == '2':
                self.menu_pacientes()
            elif opcao == '3':
                self.menu_medicos()
            elif opcao == '4':
                self.menu_relatorios()  # Chamando o menu de relatórios
            elif opcao == '5':
                print("Saindo do sistema...")
                self.splash_screen.get_updated_screen()  # Exibe o SplashScreen antes de sair
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_exames(self):
        """Menu de opções para Exames"""
        while True:
            self.mostrar_contagem_registros()
            print("1. Inserir Exame" +
                  "\n2. Remover Exame" +
                  "\n3. Atualizar Exame" +
                  "\n4. Listar Exames" +
                  "\n5. Voltar ao menu principal")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.exame_controller.inserir_exame()
                self.mostrar_contagem_registros()
            elif opcao == '2':
                self.exame_controller.remover_exame()
                self.mostrar_contagem_registros()
            elif opcao == '3':
                self.exame_controller.atualizar_exame()
                self.mostrar_contagem_registros()
            elif opcao == '4':
                self.exame_controller.listar_exames_detalhados()
            elif opcao == '5':
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_pacientes(self):
        """Menu de opções para Pacientes"""
        while True:
            self.mostrar_contagem_registros()
            print("1. Inserir Paciente" +
                  "\n2. Remover Paciente" +
                  "\n3. Atualizar Paciente" +
                  "\n4. Listar Pacientes" +
                  "\n5. Voltar ao menu principal")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.paciente_controller.inserir_paciente()
                self.mostrar_contagem_registros()
            elif opcao == '2':
                self.paciente_controller.remover_paciente()
                self.mostrar_contagem_registros()
            elif opcao == '3':
                self.paciente_controller.atualizar_paciente()
                self.mostrar_contagem_registros()
            elif opcao == '4':
                self.paciente_controller.listar_pacientes_detalhados()
            elif opcao == '5':
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_medicos(self):
        """Menu de opções para Médicos"""
        while True:
            self.mostrar_contagem_registros()
            print("1. Inserir Médico" +
                  "\n2. Remover Médico" +
                  "\n3. Atualizar Médico" +
                  "\n4. Listar Médicos" +
                  "\n5. Voltar ao menu principal")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.medico_controller.inserir_medico()
                self.mostrar_contagem_registros()
            elif opcao == '2':
                self.medico_controller.remover_medico()
                self.mostrar_contagem_registros()
            elif opcao == '3':
                self.medico_controller.atualizar_medico()
                self.mostrar_contagem_registros()
            elif opcao == '4':
                self.medico_controller.listar_medicos_detalhados()
            elif opcao == '5':
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_relatorios(self):
        """Menu de Relatórios"""
        while True:
            print("\nMenu de Relatórios:" +
                  "\n1. Exibir Relatórios" +
                  "\n2. Exportar Relatório" +
                  "\n3. Voltar ao menu principal")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.exibir_relatorios()
            elif opcao == '2':
                self.exportar_relatorio()  # Chamando a função de exportação
            elif opcao == '3':
                break
            else:
                print("Opção inválida! Tente novamente.")

    def exibir_relatorios(self):
        """Exibe os relatórios de sumarização e junção"""
        print("\nRelatórios Disponíveis:")
        print("1. Relatório de Sumarização")
        print("2. Relatório de Junção de Coleções")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            self.relatorio_sumarizacao()  # Chama o método de sumarização
        elif opcao == '2':
            self.relatorio_juncao()  # Chama o método de junção de coleções
        else:
            print("Opção inválida! Tente novamente.")

    def relatorio_sumarizacao(self):
        """Relatório de sumarização de exames por especialidade"""
        especialidades = self.medico_controller.get_exames_por_especialidade()
        for especialidade, total_exames in especialidades.items():
            print(f"Especialidade: {especialidade} | Total de Exames: {total_exames}")

    def relatorio_juncao(self):
        """Relatório de junção entre médicos e seus exames"""
        medicos_exames = self.medico_controller.get_exames_por_medico()
        for medico, dados in medicos_exames.items():
            print(f"Médico: {medico} | Especialidade: {dados['especialidade']} | Total de Exames: {dados['numero_exames']}")

    def exportar_relatorio(self):
        """Exporta relatório de médicos, exames e especialidades para CSV"""
        medicos = self.medico_controller.get_exames_por_medico()

        # Abre o arquivo CSV para escrita
        with open('relatorio_medicos.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Cabeçalho do CSV
            writer.writerow(['Nome', 'Total de Exames', 'Especialidade'])

            # Adiciona os dados de cada médico
            for medico, dados in medicos.items():
                writer.writerow([medico, dados['numero_exames'], dados['especialidade']])

        print("Relatório exportado com sucesso como 'relatorio_medicos.csv'!")
