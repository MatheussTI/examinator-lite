class InterfaceUsuario:
    def __init__(self, exame_controller, paciente_controller, medico_controller, splash_screen):
        self.exame_controller = exame_controller
        self.paciente_controller = paciente_controller
        self.medico_controller = medico_controller
        self.splash_screen = splash_screen

    def mostrar_contagem_registros(self):
        # Exibe a contagem de registros de forma mais bonita
        print("\n-------------------- Listagem Geral --------------------")
        print(f"TOTAL DE REGISTROS:")
        print(f"Exames:     {str(self.splash_screen.get_documents_count('exames')).rjust(5)}")
        print(f"Pacientes:  {str(self.splash_screen.get_documents_count('pacientes')).rjust(5)}")
        print(f"Médicos:    {str(self.splash_screen.get_documents_count('medicos')).rjust(5)}")
        print("--------------------------------------------------------")

    def menu_principal(self):
        """Menu principal do sistema"""
        while True:
            print("\nMenu Principal:" +
                  "\n1. Acessar Exames" +
                  "\n2. Acessar Pacientes" +
                  "\n3. Acessar Médicos" +
                  "\n4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.menu_exames()
            elif opcao == '2':
                self.menu_pacientes()
            elif opcao == '3':
                self.menu_medicos()
            elif opcao == '4':
                print("Saindo do sistema...")
                self.splash_screen.get_updated_screen()  # Exibe o SplashScreen novamente antes de sair
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
            self.mostrar_contagem_registros()  # Exibe a contagem de registros antes de cada ação
            print("1. Inserir Paciente" +
                  "\n2. Remover Paciente" +
                  "\n3. Atualizar Paciente" +
                  "\n4. Listar Pacientes" +
                  "\n5. Voltar ao menu principal")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.paciente_controller.inserir_paciente()
                self.mostrar_contagem_registros()  # Atualiza a contagem após inserção
            elif opcao == '2':
                self.paciente_controller.remover_paciente()
                self.mostrar_contagem_registros()  # Atualiza a contagem após remoção
            elif opcao == '3':
                self.paciente_controller.atualizar_paciente()
                self.mostrar_contagem_registros()  # Atualiza a contagem após atualização
            elif opcao == '4':
                self.paciente_controller.listar_pacientes_detalhados()
            elif opcao == '5':
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_medicos(self):
        """Menu de opções para Médicos"""
        while True:
            self.mostrar_contagem_registros()  # Exibe a contagem de registros antes de cada ação
            print("1. Inserir Médico" +
                  "\n2. Remover Médico" +
                  "\n3. Atualizar Médico" +
                  "\n4. Listar Médicos" +
                  "\n5. Voltar ao menu principal")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.medico_controller.inserir_medico()
                self.mostrar_contagem_registros()  # Atualiza a contagem após inserção
            elif opcao == '2':
                self.medico_controller.remover_medico()
                self.mostrar_contagem_registros()  # Atualiza a contagem após remoção
            elif opcao == '3':
                self.medico_controller.atualizar_medico()
                self.mostrar_contagem_registros()  # Atualiza a contagem após atualização
            elif opcao == '4':
                self.medico_controller.listar_medicos_detalhados()
            elif opcao == '5':
                break
            else:
                print("Opção inválida! Tente novamente.")
