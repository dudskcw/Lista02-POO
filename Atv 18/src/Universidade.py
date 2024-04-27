class Universidade:
    def __init__(self):
        self.__Instituicao = ""
        self.__Departamentos = []

    def getInstituicao(self) -> str:
        return self.__Instituicao

    def setInstituicao(self, instituicao:str):
        self.__Instituicao = instituicao

    def AddDepartamentos(self, departamento):
        self.__Departamentos.append(departamento)
    
    def __str__(self) -> str:
        return f"{self.getInstituicao()}"
    
