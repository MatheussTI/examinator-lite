from model.medico_model import Medico

class MedicoController:
    def __init__(self, db, exame_controller):
        self.db = db
        self.medico_collection = db["medicos"]
        self.exame_controller = exame_controller  # Controlador de exames, já passado no construtor
        self.verificar_conexao()

    def verificar_conexao(self):
        """Verifica a conexão com o banco de dados"""
        try:
            self.db.command("ping")  # Comando MongoDB para verificar a conexão
            print("Conexão com o banco de dados estabelecida.")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def buscar_medico_por_nome(self, nome):
        """Busca um médico pelo nome"""
        return self.medico_collection.find_one({"nome": nome})

    def inserir_medico(self):
        """Inserir um novo médico"""
        try:
            nome_medico = input("Digite o nome do médico: ").strip()
            if not nome_medico:
                print("O nome do médico não pode ser vazio.")
                return

            especialidade = input("Digite a especialidade do médico: ").strip()
            if not especialidade:
                print("A especialidade do médico não pode ser vazia.")
                return

            telefone = input("Digite o telefone do médico: ").strip()
            if not telefone:
                print("O telefone do médico não pode ser vazio.")
                return

            # Criando o médico
            medico = Medico(nome_medico, especialidade, telefone)
            medico_data = {
                "nome": nome_medico,
                "especialidade": especialidade,
                "telefone": telefone
            }
            self.medico_collection.insert_one(medico_data)
            print(f"Médico '{nome_medico}' inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir médico: {e}")

    def remover_medico(self):
        """Remover um médico existente"""
        try:
            nome_medico = input("Digite o nome do médico a ser removido: ").strip()
            if not nome_medico:
                print("O nome do médico não pode ser vazio.")
                return

            # Verifica se o médico existe
            medico = self.buscar_medico_por_nome(nome_medico)
            if medico:
                self.medico_collection.delete_one({"nome": nome_medico})
                print(f"Médico '{nome_medico}' removido com sucesso!")
            else:
                print(f"Médico '{nome_medico}' não encontrado!")
        except Exception as e:
            print(f"Erro ao remover médico: {e}")

    def atualizar_medico(self):
        """Atualizar um médico existente"""
        try:
            nome_medico = input("Digite o nome do médico a ser atualizado: ").strip()
            if not nome_medico:
                print("O nome do médico não pode ser vazio.")
                return

            # Verifica se o médico existe
            medico = self.buscar_medico_por_nome(nome_medico)
            if medico:
                novo_nome = input(f"Digite o novo nome do médico (atual: {nome_medico}): ").strip()
                if not novo_nome:
                    print("O novo nome do médico não pode ser vazio.")
                    return
                nova_especialidade = input(f"Digite a nova especialidade do médico: ").strip()
                if not nova_especialidade:
                    print("A nova especialidade não pode ser vazia.")
                    return
                novo_telefone = input(f"Digite o novo telefone do médico: ").strip()
                if not novo_telefone:
                    print("O novo telefone não pode ser vazio.")
                    return

                # Atualiza o médico
                self.medico_collection.update_one(
                    {"nome": nome_medico},
                    {"$set": {"nome": novo_nome, "especialidade": nova_especialidade, "telefone": novo_telefone}}
                )
                print(f"Médico '{nome_medico}' atualizado com sucesso!")
            else:
                print(f"Médico '{nome_medico}' não encontrado!")
        except Exception as e:
            print(f"Erro ao atualizar médico: {e}")

    def listar_medicos_detalhados(self):
        """Listar todos os médicos detalhados"""
        try:
            medicos = self.medico_collection.find()
            if self.medico_collection.count_documents({}) == 0:
                print("Nenhum médico encontrado!")
                return

            print("\nLista de Médicos:")
            for medico in medicos:
                print(f"Médico: {medico['nome']} | Especialidade: {medico['especialidade']} | Telefone: {medico['telefone']}")
        except Exception as e:
            print(f"Erro ao listar médicos: {e}")

    def contar_medicos(self):
        """Contar o total de médicos"""
        try:
            total = self.medico_collection.count_documents({})
            print(f"Total de médicos: {total}")
            return total
        except Exception as e:
            print(f"Erro ao contar médicos: {e}")
            return 0

    def get_exames_por_medico(self):
        """Contabiliza o número de exames realizados por cada médico, incluindo especialidade"""
        medico_exames = {}

        try:
            # Obtém todos os exames através do exame_controller
            exames = self.exame_controller.exame_collection.find()
            for exame in exames:
                # Verifica qual médico é responsável pelo exame
                medico_responsavel = exame.get("medico_responsavel")
                medico = self.buscar_medico_por_nome(medico_responsavel)
                
                if medico:
                    nome_medico = medico.get("nome")
                    especialidade = medico.get("especialidade")  # Supondo que cada médico tem uma especialidade

                    # Se o médico já estiver no dicionário, apenas incrementa o contador
                    if nome_medico in medico_exames:
                        medico_exames[nome_medico]["numero_exames"] += 1
                    else:
                        # Se o médico não estiver no dicionário, cria uma entrada com o contador inicializado
                        medico_exames[nome_medico] = {
                            "numero_exames": 1,
                            "especialidade": especialidade
                        }
            
            # Retorna os dados organizados por médico
            return medico_exames
        except Exception as e:
            print(f"Erro ao contar exames por médico: {e}")
            return {}
    def get_exames_por_especialidade(self):
            """Contabiliza o número de exames realizados por especialidade de cada médico"""
            especialidades_exames = {}

            try:
                # Obtém todos os exames
                exames = self.exame_controller.exame_collection.find()
                for exame in exames:
                    medico_responsavel = exame.get("medico_responsavel")
                    medico = self.buscar_medico_por_nome(medico_responsavel)

                    if medico:
                        especialidade = medico.get("especialidade")  # Supondo que cada médico tem uma especialidade

                        # Se a especialidade já estiver no dicionário, apenas incrementa o contador
                        if especialidade in especialidades_exames:
                            especialidades_exames[especialidade]["numero_exames"] += 1
                        else:
                            # Se a especialidade não estiver no dicionário, cria uma entrada com o contador inicializado
                            especialidades_exames[especialidade] = {
                                "numero_exames": 1
                            }

                # Retorna os dados organizados por especialidade
                return especialidades_exames

            except Exception as e:
                print(f"Erro ao contar exames por especialidade: {e}")
                return {}