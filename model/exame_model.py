class Exame:
    def __init__(self, nome_exame: str = None, medico_responsavel: str = None):
        self.set_nome_exame(nome_exame)
        self.set_medico_responsavel(medico_responsavel)

    def set_nome_exame(self, nome_exame: str):
        self.nome_exame = nome_exame

    def set_medico_responsavel(self, medico_responsavel: str):
        self.medico_responsavel = medico_responsavel

    def get_nome_exame(self) -> str:
        return self.nome_exame

    def get_medico_responsavel(self) -> str:
        return self.medico_responsavel

    def to_string(self) -> str:
        return f"Exame: {self.get_nome_exame()} | Médico Responsável: {self.get_medico_responsavel()}"
