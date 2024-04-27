from src.Departamento import Departamento
from src.Pessoa import Pessoa
from src.Universidade import Universidade

#Pessoa
Pessoa01 = Pessoa()
Pessoa01.setNome("Ana")

Pessoa02 = Pessoa()
Pessoa02.setNome("Marcelo")

Pessoa03 = Pessoa()
Pessoa03.setNome("Rafael")

Pessoa04 = Pessoa()
Pessoa04.setNome("Maria")

Pessoa05 = Pessoa()
Pessoa05.setNome("Carlão")
#Pessoa

#Departamento
Departamento01 = Departamento()
Departamento01.setDepartamento("Limpeza")
Departamento01.addTrabalhadores(Pessoa01)
Departamento01.addTrabalhadores(Pessoa03)

Departamento02 = Departamento()
Departamento02.setDepartamento("Administrativo")
Departamento02.addTrabalhadores(Pessoa02)
Departamento02.addTrabalhadores(Pessoa05)

Departamento03 = Departamento()
Departamento03.setDepartamento("Academico")
Departamento03.addTrabalhadores(Pessoa04)
#Departamento

#Universidade
Universidade01 = Universidade()
Universidade01.setInstituicao("UFMG")
Universidade01.AddDepartamentos(Departamento03)
Universidade01.AddDepartamentos(Departamento01)

Universidade02 = Universidade()
Universidade02.setInstituicao("UNIPAC")
Universidade02.AddDepartamentos(Departamento03)
Universidade02.AddDepartamentos(Departamento01)
Universidade02.AddDepartamentos(Departamento02)
#Universidade
Departamento01.addUniversidae(Universidade01)
Departamento01.addUniversidae(Universidade02)

Departamento02.addUniversidae(Universidade02)

Departamento03.addUniversidae(Universidade01)
Departamento03.addUniversidae(Universidade02)

#os prints
Departamento01.Printar()
Departamento02.Printar()
Departamento03.Printar()