from pymongo import MongoClient


class MedicoModel:
    def __init__(self, db):
        self.collection = db["medicos"]

    def inserir_medico(self, nome, hierarquia):
        medico = {
            "nome": nome,
            "hierarquia": hierarquia
        }
        self.collection.insert_one(medico)
        print(f"Médico {nome} inserido com sucesso!")

    def listar_medicos(self):
        medicos = self.collection.find()
        for medico in medicos:
            print(medico)
