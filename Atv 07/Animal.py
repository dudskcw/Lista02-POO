class Animal:
    def __init__(self, nome:str, raca:str):
        self.__Nome = nome
        self.__Raca = raca

class Cachorro(Animal):
    def __init__(self, nome:str, raca:str):
        super().__init__(nome, raca)

    def Latir(self):
        print(f"Au au au au au au")

    def Caminhar(self):
        print(f"O Cachorro esta andando")

class Gato(Animal):
    def __init__(self, nome:str, raca:str):
        super().__init__(nome, raca)

    def Caminhar(self):
        print(f"O Gato esta andando")

    def Miar(self):
        print(f"Miau miau miau miau miau")

