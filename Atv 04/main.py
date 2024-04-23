from Empregado import Empregado

Pessoa1 = Empregado()

Pessoa1.setNome("Francisco")
Pessoa1.setSobrenomeome("Augusto")
Pessoa1.setSalario(1675.90)
print(Pessoa1)

NovoSalario = Pessoa1.getSalario()

NovoSalario += NovoSalario * 0.01

Pessoa1.setSalario(NovoSalario)
print(Pessoa1)
