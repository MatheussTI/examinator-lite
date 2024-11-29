import time
from config.DBConfig import DBConfig


class SplashScreen:

    def __init__(self):
        # Nome(s) do(s) criador(es)
        self.created_by = "Matheus Andrade Rangel, William Alves Freitas Foca, Arthur Salles Soares Richard"
        self.professor = "Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2024/2"

        # Inicializa a configuração do banco de dados
        self.db_config = DBConfig()

    def get_documents_count(self, collection_name):
        # Retorna o total de registros computado pela query
        count_data = self.db_config.query_count(collection_name)
        return count_data  # Não é necessário acessar um índice, apenas retorna o valor inteiro

    def get_updated_screen(self):
        # Exibe a tela inicial com a contagem de documentos
        return f"""
        ########################################################
        #                   SISTEMA EXAMINATOR LITE
        #
        #  TOTAL DE REGISTROS:
        #      1 - EXAMES:         {str(self.get_documents_count("exames")).rjust(6)}
        #      2 - PACIENTES:       {str(self.get_documents_count("pacientes")).rjust(5)}
        #      3 - MEDICOS:         {str(self.get_documents_count("medicos")).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """

