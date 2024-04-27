'''
Fazer um programa em Python que:

• Salve estes dados em um arquivo. Os dados devem ser salvos registro a
registro, obedecendo o seguinte formato:
i. número inteiro contendo o tamanho em char do nome do aluno.
ii. sequência de chars correspondente à string que contém o nome do
aluno.
iii. duas notas na forma de números inteiros.
Fazer um programa em python para:
• ler os dados contidos no arquivo gerado pelo programa anterior
• calcular e mostrar: quais alunos foram aprovados, quais foram para exame,
quais foram reprovados e a média da turma.
'''
import os
class Sistema:
    def __init__(self):
        self.__Nome = ""
        self.__Portugues = 0.0
        self.__Matematica = 0.0

    #Acesso variaveis
    def getNome (self) -> str:
        return self.__Nome

    def setNome (self, nome:str):
        self.__Nome = nome

    def getPortugues (self) -> float:
        return self.__Portugues

    def setPortugues (self, portugues:float):
        self.__Portugues = portugues 

    def getMatematica (self) -> float:
        return self.__Matematica

    def setMatematica (self, matematica:float):
        self.__Matematica = matematica
    #Acesso variaveis

    def Arquivar(self):
        Arquivo = os.path.join("Alunos", self.__Nome + ".txt")
        with open(Arquivo, "w") as arquivo:
            arquivo.write(f"{self.__Nome}\n{self.__Portugues}\n{self.__Matematica}")

    def Calcular (self, nome:str):
        Arquivo = os.path.join("Alunos", nome + ".txt")
        with open(Arquivo, "r") as arquivo:
            self.setNome(nome)
            arquivo.readline()
            self.setPortugues(float(arquivo.readline()))
            self.setMatematica(float(arquivo.readline()))
            
            if self.getPortugues() >= 7.0 and self.getMatematica() >= 7.0:
                 print(f"{self.getNome()} foi Aprovado em Portugues e Matematica\n")

            elif self.getPortugues() < 7.0 and self.getMatematica() < 7.0:
                 print(f"{self.getNome()} foi Reprovado em Portugues e Matematica\n")

            else:
                if self.getPortugues() >= 7.0:
                    print(f"{self.getNome()} foi Aprovado em Portugues", end="")

                else:
                    print(f"{self.getNome()} foi Reprovado em Portugues", end="")

                if self.getMatematica() >= 7.0:
                    print(f" e foi Aprovado em Matematica\n")

                else:
                    print(f" e foi Reprovado em Matematica\n")

def MediaPortugues(Alunos):
    media = 0.0
    quant = 0

    for Alunos in Alunos:
        Arquivo = os.path.join("Alunos", Alunos + ".txt")
        with open(Arquivo, "r") as arquivo:
            arquivo.readline()
            linha = float(arquivo.readline())
            quant +=1
            media += linha

    media = media/quant
    print(f"Media da turma em Portugues: {media:.2f}")

def MediaMatematica(Alunos):
    media = 0.0
    quant = 0

    for Alunos in Alunos:
        Arquivo = os.path.join("Alunos", Alunos + ".txt")
        with open(Arquivo, "r") as arquivo:
            arquivo.readline()
            arquivo.readline()
            linha = float(arquivo.readline())
            quant +=1
            media += linha

    media = media/quant
    print(f"Media da turma em Matematica: {media:.2f}")




    