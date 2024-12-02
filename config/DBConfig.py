from pymongo import MongoClient, errors

class DBConfig:
    def __init__(self):
        self.mongo_db_infos = {
            "DB_NAME": "Cluster0",
            "USER": "normal",
            "PASSWORD": "normal"
        }
        self.connection_string = f"mongodb+srv://{self.mongo_db_infos['USER']}:{self.mongo_db_infos['PASSWORD']}@cluster0.aub74.mongodb.net/?retryWrites=true&w=majority&appName={self.mongo_db_infos['DB_NAME']}"
        self.client = None
        self.db = None
        self.verify_connection()

    def verify_connection(self):
        # Primeiro tenta uma conexão sem autenticação
        try:
            print("Tentando conectar com o banco em nuvem...")
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.mongo_db_infos["DB_NAME"]]
            # Tentando listar as coleções para garantir que a conexão seja válida
            self.db.list_collection_names()
            print("Conexão bem-sucedida.")
        except errors.OperationFailure:
            print("Falha na conexão")
            self.ask_for_credentials()

    # Verifica se a coleção existe no banco de dados.
    def verificar_colecao(self, nome_colecao):
        if nome_colecao not in self.db.list_collection_names():
            print(f"Coleção '{nome_colecao}' não encontrada.")
            return False
        print(f"Coleção '{nome_colecao}' já existe.")
        return True

    # Cria uma coleção no banco de dados.
    def criar_colecao(self, nome_colecao):
        print(f"Coleção '{nome_colecao}' não encontrada. Criando...")
        self.db.create_collection(nome_colecao)
        print(f"Coleção '{nome_colecao}' criada com sucesso!")

    # Verifica se as coleções necessárias existem e cria se não existirem.
    def criar_colecao_se_necessario(self):
        colecoes_necessarias = ["medicos", "exames", "pacientes"]
        for colecao in colecoes_necessarias:
            if not self.verificar_colecao(colecao):
                self.criar_colecao(colecao)

    def list_collections(self):
        try:
            collections = self.db.list_collection_names()
            if collections:
                print("Coleções no banco de dados:")
                for collection in collections:
                    print(f"- {collection}")
            else:
                print("O banco de dados não contém coleções.")
        except Exception as e:
            print(f"Erro ao listar coleções: {e}")

    def get_db(self):
        return self.db

    def query_count(self, collection_name):
        # Retorna o número de documentos de uma coleção
        collection = self.db[collection_name]
        count = collection.count_documents({})
        return count
    

########## TESTE DOS MÉTODOS IMPLEMENTADOS ##############
# Criando e utilizando a classe
db_config = DBConfig()
db = db_config.get_db()

# Exibindo as coleções no banco de dados
db_config.list_collections()

# Verificando e criando coleções necessárias
db_config.criar_colecao_se_necessario()
