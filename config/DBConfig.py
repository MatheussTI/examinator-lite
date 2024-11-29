from pymongo import MongoClient, errors
import getpass  # Para esconder a senha ao solicitar no terminal


class DBConfig:
    def __init__(self):
        self.mongo_db_infos = {
            "HOST": "localhost",
            "PORT": "27017",
            "DB_NAME": "ExaminatorLite",
            "USER": None,
            "PASSWORD": None
        }
        self.connection_string = f"mongodb://{
            self.mongo_db_infos['HOST']}:{self.mongo_db_infos['PORT']}"
        self.client = None
        self.db = None
        self.verify_connection()

    def verify_connection(self):
        # Primeiro tenta uma conexão sem autenticação
        try:
            print("Tentando conectar sem autenticação...")
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.mongo_db_infos["DB_NAME"]]
            # Tentando listar as coleções para garantir que a conexão seja válida
            self.db.list_collection_names()
            print("Conexão bem-sucedida sem autenticação.")
        except errors.OperationFailure:
            print(
                "Falha na conexão sem autenticação. O MongoDB provavelmente exige autenticação.")
            self.ask_for_credentials()

    def ask_for_credentials(self):
        # Se a conexão sem autenticação falhar, pede as credenciais
        self.mongo_db_infos["USER"] = input("Digite o username: ").strip()
        self.mongo_db_infos["PASSWORD"] = getpass.getpass(
            "Digite a senha: ").strip()

        self.connection_string = f"mongodb://{self.mongo_db_infos['USER']}:{
            self.mongo_db_infos['PASSWORD']}@{self.mongo_db_infos['HOST']}:{self.mongo_db_infos['PORT']}"

        try:
            # Tentando conectar com as credenciais fornecidas
            print("Tentando conectar com autenticação...")
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.mongo_db_infos["DB_NAME"]]
            # Tentando listar as coleções para garantir que a conexão seja válida
            self.db.list_collection_names()
            print("Conexão bem-sucedida com autenticação.")
        except errors.OperationFailure:
            print(
                "Falha na autenticação. Certifique-se de que as credenciais estão corretas.")
        except Exception as e:
            print(f"Erro ao tentar conectar: {e}")

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


# Criando e utilizando a classe
db_config = DBConfig()
db = db_config.get_db()
