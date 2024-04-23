from Ingresso import Ingresso
from Ingresso import IngressoVip

cliente1 = Ingresso()
cliente2 = IngressoVip()

cliente1.setValor(15.60)
cliente2.setValor(15.60)
cliente2.setAdicional(4.80)

cliente1.ImprimirValor()
cliente2.ImprimirValor2()
