from src.Pessoa import Pessoa
from src.Universidade import Universidade

Pessoa01 = Pessoa()
Pessoa01.setNome('Isaac Newton')
Pessoa01.setNascimento('04/01/1643')
Universidade01 = Universidade()
Universidade01.setInstituicao("Princeton")
Universidade01.AddProfessor(Pessoa01)
Pessoa01.setUniversidade(Universidade01)
print(Pessoa01)

Pessoa02 = Pessoa()
Pessoa02.setNome('Albert Einstein')
Pessoa02.setNascimento('14/03/1879')
Universidade02 = Universidade()
Universidade02.setInstituicao("Cambridge")
Universidade02.AddProfessor(Pessoa02)
Pessoa02.setUniversidade(Universidade02)
print(Pessoa02)