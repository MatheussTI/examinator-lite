class ExameController:
    def __init__(self, db):
        self.db = db
        self.exame_collection = db["exames"]
        self.medico_collection = db["medicos"]
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

    def buscar_medico_por_nome(self, nome):
        """Busca um médico pelo nome"""
        return self.medico_collection.find_one({"nome": nome})

    def buscar_exame_por_nome(self, nome):
        """Busca um exame pelo nome"""
        return self.exame_collection.find_one({"nome_exame": nome})

    def inserir_exame(self):
        """Inserir um novo exame"""
        nome_exame = input("Digite o nome do exame: ").strip()
        if not nome_exame:
            print("O nome do exame não pode ser vazio.")
            return

        medico_responsavel = input("Digite o nome do médico responsável pelo exame: ").strip()
        if not medico_responsavel:
            print("O nome do médico responsável não pode ser vazio.")
            return

        # Verificar se o médico existe
        medico = self.buscar_medico_por_nome(medico_responsavel)
        if medico:
            exame = Exame(nome_exame, medico_responsavel)
            exame_data = {
                "nome_exame": nome_exame,
                "medico_responsavel": medico_responsavel
            }
            self.exame_collection.insert_one(exame_data)
            print(f"Exame '{nome_exame}' inserido com sucesso!")
        else:
            print(f"Médico {medico_responsavel} não encontrado!")

    def remover_exame(self):
        """Remover um exame existente"""
        try:
            nome_exame = input("Digite o nome do exame a ser removido: ").strip()
            if not nome_exame:
                print("O nome do exame não pode ser vazio.")
                return

            # Verifica se o exame existe
            exame = self.buscar_exame_por_nome(nome_exame)
            if exame:
                self.exame_collection.delete_one({"nome_exame": nome_exame})
                print(f"Exame '{nome_exame}' removido com sucesso!")
            else:
                print(f"Exame '{nome_exame}' não encontrado!")
        except Exception as e:
            print(f"Erro ao remover exame: {e}")

    def atualizar_exame(self):
        """Atualizar um exame existente"""
        try:
            nome_exame = input("Digite o nome do exame a ser atualizado: ").strip()
            if not nome_exame:
                print("O nome do exame não pode ser vazio.")
                return

            # Verifica se o exame existe
            exame = self.buscar_exame_por_nome(nome_exame)
            if exame:
                novo_nome = input(f"Digite o novo nome do exame (atual: {nome_exame}): ").strip()
                if not novo_nome:
                    print("O novo nome do exame não pode ser vazio.")
                    return
                novo_medico = input(f"Digite o nome do novo médico responsável: ").strip()

                if not novo_medico:
                    print("O nome do novo médico responsável não pode ser vazio.")
                    return

                # Verifica se o novo médico existe
                medico = self.buscar_medico_por_nome(novo_medico)
                if medico:
                    self.exame_collection.update_one(
                        {"nome_exame": nome_exame},
                        {"$set": {"nome_exame": novo_nome, "medico_responsavel": novo_medico}}
                    )
                    print(f"Exame '{nome_exame}' atualizado com sucesso!")
                else:
                    print(f"Médico {novo_medico} não encontrado!")
            else:
                print(f"Exame '{nome_exame}' não encontrado!")
        except Exception as e:
            print(f"Erro ao atualizar exame: {e}")

    def listar_exames_detalhados(self):
        """Listar todos os exames detalhados"""
        try:
            exames = self.exame_collection.find()
            if self.exame_collection.count_documents({}) == 0:
                print("Nenhum exame encontrado!")
                return

            print("\nLista de Exames:")
            for exame in exames:
                print(f"Exame: {exame['nome_exame']} | Médico Responsável: {exame['medico_responsavel']}")
        except Exception as e:
            print(f"Erro ao listar exames: {e}")

    def contar_exames(self):
        """Contar o total de exames"""
        try:
            total = self.exame_collection.count_documents({})
            print(f"Total de exames: {total}")
            return total
        except Exception as e:
            print(f"Erro ao contar exames: {e}")
            return 0

    # Método para obter todos os exames
    def get_exames(self):
        """Retorna todos os exames armazenados"""
        try:
            exames = self.exame_collection.find()
            return list(exames)
        except Exception as e:
            print(f"Erro ao buscar exames: {e}")
            return []
