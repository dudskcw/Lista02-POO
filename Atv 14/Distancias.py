class Distancia:
    def __init__(self):
        self.__Kilometros = [
            [0, 15, 30, 5, 12],
            [15, 0, 10, 17, 28],
            [30, 10, 0, 3, 11],
            [5, 17, 3, 0, 80],
            [12, 28, 11, 80, 0]
        ]

        self.__Percurso = []
        self.Total = 0.0

    def getPercurso(self) -> float:
        return self.__Percurso

    def setPercurso(self, percurso:float):
        self.__Percurso = percurso

    def CalcularDistancia(self):
        percurso = self.getPercurso()
        for i in range(len(percurso) - 1):
            origem = percurso[i]
            destino = percurso[i + 1]
            self.Total += self.__Kilometros [origem][destino]
            
        print(f"{self.Total}")
    

