from ast import Return

from pdb import Restart
from this import s

from urllib3 import Retry


t1 = int(input("Entre com um número: "))
t2 = int(input("Entre com o segundo número: "))
t3 = int(input("Entre com o terceiro número: "))


RegraTriangulo = t1 + t2 + t3 < 181
if t1 > t2 + t3:
    print("O triângulo é inválido pela regra da soma dos lados, por favor insira outro valor: ")
    Retry
if t2 > t1 + t3: 
    print("O triângulo é inválido pela regra da soma dos lados, por favor insira outro valor: ")
    Retry
if t3 > t1 + t2: 
    print("O triângulo é inválido pela regra da soma dos lados, por favor insira outro valor: ")
    Retry 
if t1 + t2 + t3 >= 181:
    print("Esse triângulo é inválido")
if t1 + t2 + t3 != 180:
    print("Esse triângulo é inválido")


elif t1 == t2 == t3:
    print("Esse triângulo é equilátero")
elif t1 == t2 != t3:
    print("Esse triângulo é isóceles")
elif t1 == t3 != t2:
    print("Esse triângulo é isóceles")
elif t2 == t3 != t1:
    print("Esse triângulo é isóceles")
elif t1 != t2 != t3: 
    print("Esse triângulo é escaleno")

