from Sistema import Sistema
from Sistema import MediaMatematica, MediaPortugues

#Pegando notas
aluno = Sistema()
aluno.setNome("PEDRO")
aluno.setPortugues(8.4)
aluno.setMatematica(2.7)
aluno.Arquivar()
aluno.Calcular("PEDRO")

Alunos = ["Carlos", "José", "Maria", "Miguel", "Jonnhy", "PEDRO"]
MediaMatematica(Alunos)
MediaPortugues(Alunos)
