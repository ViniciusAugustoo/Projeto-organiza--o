import pytest 
from calculadora2.segundacalc import operadores

def test_somar():
    calcule = operadores
    resultado = calcule.somar(1, 2)
    assert resultado == 3

