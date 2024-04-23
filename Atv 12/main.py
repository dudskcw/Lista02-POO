from src.Funcionario import Funcionario

funcionario = Funcionario()
funcionario.setNome("João")
funcionario.setSobrenome("Vieira")
funcionario.setSalario(1769.00)
print(funcionario)

funcionario.setAdicional(0.1)
funcionario.addAumento()
print(funcionario)
