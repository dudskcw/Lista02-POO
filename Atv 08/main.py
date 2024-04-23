from src.Funcionario import Funcionario
from src.TecnicoAdimnistrativo import Admnistrativo
from src.TecnicoAdimnistrativo import Tecnico

print("Funcionario 1 (Funcionario Comum")
func1 = Funcionario()
func1.setNome("Rogério")
func1.setSalario(1850.00)
func1.setAdicional(0.10)
func1.addAumento()
func1.ganhoAnual()
func1.exibeDados()

print("\n\nFuncionario 2 (Assistente Admnistrativo)")
func2 = Admnistrativo()
func2.setNome("Sheila")
func2.setSalario(1456.00)
func2.setAdicional(0.05)
func2.setMatricula("5446783")
func2.setTurno("Diurno")
func2.setaddNoturno(20)
func2.setDiasNoturno(4)
func2.addAumento()
func2.calculosalario()
func2.exibeDados()

print("\n\nFuncionario 3 (Assistente Tecnico)")
func3 = Tecnico()
func3.setNome("Dominique")
func3.setSalario(1654.00)
func3.setAdicional(0.02)
func3.setMatricula("7583659")
func3.setBonus(200)
func3.addAumento()
func3.calculosalario()
func3.exibeDados()


