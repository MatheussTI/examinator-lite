from pymongo import MongoClient

class PacienteModel:
    def __init__(self, db):
        self.collection = db["pacientes"]

    def inserir_paciente(self, nome, idade, condicao, exame_realizado, medico_responsavel, data_hora):
        paciente = {
            "nome": nome,
            "idade": idade,
            "condicao": condicao,
            "exame_realizado": exame_realizado,
            "medico_responsavel": medico_responsavel,
            "data_hora": data_hora
        }
        self.collection.insert_one(paciente)
        print(f"Paciente {nome} inserido com sucesso!")

    def listar_pacientes(self):
        pacientes = self.collection.find()
        for paciente in pacientes:
            print(paciente)
