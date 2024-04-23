from src.Funcionario import Funcionario
from src.Gerente import Gerente
from src.Vendedor import Vendedor

print("\nFuncionario 1")
funcionario1 = Funcionario()
funcionario1.setNome("Angela")
funcionario1.setSalario(1345.99)
funcionario1.toString()
print("-------------------------------------\n")

print("Funcionario 2")
funcionario2 = Gerente()
funcionario2.setNome("Mariano")
funcionario2.setSalario(2342.78)
funcionario2.setDepartamento("Gerente de Estoque")
funcionario2.toString()
print("-------------------------------------\n")

print("Funcionario 3")
funcionario3 = Vendedor()
funcionario3.setNome("Carlos")
funcionario3.setSalario(1345.39)
funcionario3.setComicao(0.09)
funcionario3.CalcularSalario()
funcionario3.toString()

