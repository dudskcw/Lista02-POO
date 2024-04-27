class Departamento: 
    def __init__(self):
        self.__Depatamento = ""
        self.__Trabalhadores = []
        self.__Universidade = []

    def getDepartamento(self) -> str:
        return self.__Departamento

    def setDepartamento(self, departamento:str):
        self.__Departamento = departamento

    def addUniversidae(self, universidade:str):
        self.__Universidade.append(universidade)

    def addTrabalhadores(self, trabalhador):
        self.__Trabalhadores.append(trabalhador)

    def getTrabalhadores(self)->str:
        return self.__Trabalhadores
    
    def getUniversidades(self)->str:
        return self.__Universidade

    def Printar(self):
        print(f"Universidades: ", end = "")
        for universidade in self.getUniversidades():
            print(universidade, end=", ")
        
        print(f"\nDepartamento: {self.getDepartamento()}")

        print(f"Trabalhadores: ", end = "")
        for pessoa in self.getTrabalhadores():
            print(pessoa, end=", ")

        print(f"\n")
              
              
        