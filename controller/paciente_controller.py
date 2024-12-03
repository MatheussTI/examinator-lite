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
            paciente_data = {
                "nome": nome_paciente,
                "idade": idade,
                "telefone": telefone,
                "exames": []  # Inicializando lista de exames para o paciente
            }
            self.paciente_collection.insert_one(paciente_data)
            print(f"Paciente '{nome_paciente}' inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir paciente: {e}")

    def remover_paciente(self):
        """Remover um paciente existente"""
        try:
            nome_paciente = input(
                "Digite o nome do paciente a ser removido: ").strip()
            if not nome_paciente:
                print("O nome do paciente não pode ser vazio.")
                return

            # Verifica se o paciente existe
            paciente = self.paciente_collection.find_one(
                {"nome": nome_paciente})
            if paciente:
                # Remover todos os exames associados ao paciente antes de deletá-lo
                exames_do_paciente = paciente.get("exames", [])
                for exame in exames_do_paciente:
                    self.exame_controller.remover_exame_associado_paciente(
                        exame, nome_paciente)
                self.paciente_collection.delete_one({"nome": nome_paciente})
                print(f"Paciente '{nome_paciente}' removido com sucesso!")
            else:
                print(f"Paciente '{nome_paciente}' não encontrado!")
        except Exception as e:
            print(f"Erro ao remover paciente: {e}")

    def listar_pacientes_detalhados(self):
        """Listar todos os pacientes detalhados"""
        try:
            pacientes = self.paciente_collection.find()
            if self.paciente_collection.count_documents({}) == 0:
                print("Nenhum paciente encontrado!")
                return

            print("\nLista de Pacientes:")
            for paciente in pacientes:
                print(f"Paciente: {paciente['nome']} | Idade: {paciente['idade']} | Telefone: {
                      paciente['telefone']} | Exames: {', '.join(paciente['exames'])}")
        except Exception as e:
            print(f"Erro ao listar pacientes: {e}")
