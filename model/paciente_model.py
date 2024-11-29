class Paciente:
    def __init__(self, nome: str = None, CPF: str = None, idade: int = None, exames_realizados: list = None):
        self.set_nome(nome)
        self.set_CPF(CPF)
        self.set_idade(idade)
        self.set_exames_realizados(exames_realizados or [])

    def set_nome(self, nome: str):
        self.nome = nome

    def set_CPF(self, CPF: str):
        self.CPF = CPF

    def set_idade(self, idade: int):
        self.idade = idade

    def set_exames_realizados(self, exames_realizados: list):
        self.exames_realizados = exames_realizados

    def get_nome(self) -> str:
        return self.nome

    def get_CPF(self) -> str:
        return self.CPF

    def get_idade(self) -> int:
        return self.idade

    def get_exames_realizados(self) -> list:
        return self.exames_realizados

    def to_string(self) -> str:
        exames = ", ".join(self.get_exames_realizados())
        return f"Paciente: {self.get_nome()} | CPF: {self.get_CPF()} | Idade: {self.get_idade()} | Exames Realizados: {exames}"
