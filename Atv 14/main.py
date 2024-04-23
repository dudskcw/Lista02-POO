from Distancias import Distancia

distacia = Distancia()

percurso = []
local = -99

while local != 0:
    local = int(input("Digite o local: "))
    percurso.append(local - 1)

distacia.setPercurso(percurso)
distacia.CalcularDistancia()
