class Universidade:
    def __init__(self):
        self.__Instituicao = ""
        self.__Professores = []

    def getInstituicao(self) -> str:
        return self.__Instituicao

    def setInstituicao(self, instituicao:str):
        self.__Instituicao = instituicao

    def AddProfessor(self, pessoa):
        self.__Professores.append(pessoa)
    
    def __str__(self) -> str:
        return f"Universidade: {self.getInstituicao()}"
    
