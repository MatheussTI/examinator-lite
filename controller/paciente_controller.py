from model.paciente_model import Paciente


class PacienteController:
    def __init__(self, db):
        self.db = db
        self.paciente_collection = db["pacientes"]
        self.verificar_conexao()

    def verificar_conexao(self):
        """Verifica a conexão com o banco de dados"""
        try:
            self.db.command("ping")  # Comando MongoDB para verificar a conexão
            print("Conexão com o banco de dados estabelecida.")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def buscar_paciente_por_nome(self, nome):
        """Busca um paciente pelo nome"""
        return self.paciente_collection.find_one({"nome": nome})

    def inserir_paciente(self):
        """Inserir um novo paciente"""
        try:
            nome_paciente = input("Digite o nome do paciente: ").strip()
            if not nome_paciente:
                print("O nome do paciente não pode ser vazio.")
                return

            idade = input("Digite a idade do paciente: ").strip()
            if not idade.isdigit():
                print("A idade precisa ser um número válido.")
                return

            telefone = input("Digite o telefone do paciente: ").strip()
            if not telefone:
                print("O telefone do paciente não pode ser vazio.")
                return

            # Criando o paciente
            paciente = Paciente(nome_paciente, idade, telefone)
            paciente_data = {
                "nome": nome_paciente,
                "idade": idade,
                "telefone": telefone
            }
            self.paciente_collection.insert_one(paciente_data)
            print(f"Paciente '{nome_paciente}' inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir paciente: {e}")

    def remover_paciente(self):
        """Remover um paciente existente"""
        try:
            nome_paciente = input("Digite o nome do paciente a ser removido: ").strip()
            if not nome_paciente:
                print("O nome do paciente não pode ser vazio.")
                return

            # Verifica se o paciente existe
            paciente = self.buscar_paciente_por_nome(nome_paciente)
            if paciente:
                self.paciente_collection.delete_one({"nome": nome_paciente})
                print(f"Paciente '{nome_paciente}' removido com sucesso!")
            else:
                print(f"Paciente '{nome_paciente}' não encontrado!")
        except Exception as e:
            print(f"Erro ao remover paciente: {e}")

    def atualizar_paciente(self):
        """Atualizar um paciente existente"""
        try:
            nome_paciente = input("Digite o nome do paciente a ser atualizado: ").strip()
            if not nome_paciente:
                print("O nome do paciente não pode ser vazio.")
                return

            # Verifica se o paciente existe
            paciente = self.buscar_paciente_por_nome(nome_paciente)
            if paciente:
                novo_nome = input(f"Digite o novo nome do paciente (atual: {nome_paciente}): ").strip()
                if not novo_nome:
                    print("O novo nome do paciente não pode ser vazio.")
                    return
                nova_idade = input("Digite a nova idade do paciente: ").strip()
                if not nova_idade.isdigit():
                    print("A idade precisa ser um número válido.")
                    return
                novo_telefone = input(f"Digite o novo telefone do paciente: ").strip()

                if not novo_telefone:
                    print("O novo telefone não pode ser vazio.")
                    return

                # Atualiza o paciente
                self.paciente_collection.update_one(
                    {"nome": nome_paciente},
                    {"$set": {"nome": novo_nome, "idade": nova_idade, "telefone": novo_telefone}}
                )
                print(f"Paciente '{nome_paciente}' atualizado com sucesso!")
            else:
                print(f"Paciente '{nome_paciente}' não encontrado!")
        except Exception as e:
            print(f"Erro ao atualizar paciente: {e}")

    def listar_pacientes_detalhados(self):
        """Listar todos os pacientes detalhados"""
        try:
            pacientes = self.paciente_collection.find()
            if self.paciente_collection.count_documents({}) == 0:
                print("Nenhum paciente encontrado!")
                return

            print("\nLista de Pacientes:")
            for paciente in pacientes:
                print(f"Paciente: {paciente['nome']} | Idade: {paciente['idade']} | Telefone: {paciente['telefone']}")
        except Exception as e:
            print(f"Erro ao listar pacientes: {e}")

    def contar_pacientes(self):
        """Contar o total de pacientes"""
        try:
            total = self.paciente_collection.count_documents({})
            print(f"Total de pacientes: {total}")
            return total
        except Exception as e:
            print(f"Erro ao contar pacientes: {e}")
            return 0
    