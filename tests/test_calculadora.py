import pytest 

from calculadora2.segundacalc import operadores

def test_adicao ():
   calcule = operadores
   resultado = calcule.adicao (1, 1)
   assert resultado == 2
   
def test_subtracao ():
   calcule = operadores
   resultado = calcule.subtracao (1, 1)
   assert resultado == 0
def test_multiplicacao ():
   calcule = operadores
   resultado = calcule.multiplicacao (1, 1)
   assert resultado == 1
def test_divisao ():
   calcule = operadores
   resultado = calcule.divisao (2, 1)
   assert resultado == 2


