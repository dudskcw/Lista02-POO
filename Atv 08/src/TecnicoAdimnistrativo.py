from src.Assistente import Assistente

class Admnistrativo(Assistente):
    def __init__(self):
        self.__Turno = ""
        self.__addNoturno = 0.0
        self.__DiasNoturno = 0

    #Acessando variaveis
    def getTurno(self) -> str:
        return self.__Turno

    def setTurno(self, turno:str):
        self.__Turno = turno

    def getaddNoturno(self) -> float:
        return self.__addNoturno

    def setaddNoturno(self, addnoturno:float):
        self.__addNoturno = addnoturno

    def getDiasNoturno(self) -> int:
        return self.__DiasNoturno

    def setDiasNoturno(self, diasnoturno:int):
        self.__DiasNoturno = diasnoturno
    #Acessando variaveis

    def calculosalario (self):
        novosalario = self.getSalario()

        novosalario += self.getaddNoturno() * self.getDiasNoturno()
        self.setSalario(novosalario)
        novosalario *=13
        self.setAnual(novosalario)

    def exibeDados (self):
        print(f"Nome: {self.getNome()}\nMatricula: {self.getMatricula()}\nSalario: {self.getSalario():.2f}")
        print(f"Turno: {self.getTurno()}\nAumento: {self.getAdicional()*100}%\nGanho Anual: {self.getAnual():.2f}")

class Tecnico(Assistente):
    def __init__(self):
        self.__Bonus = 0.0

    #Acessando variaveis
    def getBonus(self) -> float:
        return self.__Bonus

    def setBonus(self, bonus:float):
        self.__Bonus = bonus
    #Acessando variaveis

    def calculosalario (self):
        novosalario = self.getSalario()

        novosalario += self.getBonus()
        self.setSalario(novosalario)
        novosalario *=13
        self.setAnual(novosalario)

    def exibeDados (self):
        print(f"Nome: {self.getNome()}\nMatricula: {self.getMatricula()}\nSalario: {self.getSalario():.2f}")
        print(f"Aumento: {self.getAdicional()*100}%\nGanho Anual: {self.getAnual():.2f}")