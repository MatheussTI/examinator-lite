from pymongo import MongoClient

class ExameModel:
    def __init__(self, db):
        self.collection = db["exames"]

    def inserir_exame(self, nome_exame, medico_responsavel):
        exame = {
            "nome_exame": nome_exame,
            "medico_responsavel": medico_responsavel
        }
        self.collection.insert_one(exame)
        print(f"Exame {nome_exame} inserido com sucesso!")

    def listar_exames(self):
        exames = self.collection.find()
        for exame in exames:
            print(exame)
