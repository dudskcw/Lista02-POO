from src.ContaBancaria import ContaBancaria
from src.ContaEspecial import ContaEspecial
from src.ContaPoupanca import ContaPoupanca

print("Cliente 1\n")
cliente1 = ContaBancaria()
cliente1.setNome("Rogerio")
cliente1.setNum("C785237579")
cliente1.setSaldo(86.90)
cliente1.sacar(58.80)
cliente1.depositar(164)
print(cliente1)

print("-------------------------------")
print("Cliente2\n")
cliente2 = ContaEspecial()
cliente2.setNome("Francisvo")
cliente2.setNum("E759831567")
cliente2.setSaldo(60.8)
cliente2.setLimite(0.1)
cliente2.SaqueEsp(64.0)
print(cliente2)

print("-------------------------------")
print("Cliente3\n")
cliente3 = ContaPoupanca()
cliente3.setNome("José")
cliente3.setNum("P742654902")
cliente3.setSaldo(58.00)
cliente3.setRend(0.008)
cliente3.calcularNovoSaldo()
print(cliente3)

from time import sleep
sleep(10)

