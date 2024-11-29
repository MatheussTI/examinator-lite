class Medico:
    def __init__(self, nome: str = None, especialidade: str = None, exames_possiveis: list = None):
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_exames_possiveis(exames_possiveis or [])

    def set_nome(self, nome: str):
        self.nome = nome

    def set_especialidade(self, especialidade: str):
        self.especialidade = especialidade

    def set_exames_possiveis(self, exames_possiveis: list):
        self.exames_possiveis = exames_possiveis

    def get_nome(self) -> str:
        return self.nome

    def get_especialidade(self) -> str:
        return self.especialidade

    def get_exames_possiveis(self) -> list:
        return self.exames_possiveis

    def to_string(self) -> str:
        exames = ", ".join(self.get_exames_possiveis())
        return f"Médico: {self.get_nome()} | Especialidade: {self.get_especialidade()} | Exames Possíveis: {exames}"
