import pytest 
from calculadora2.segundacalc import operadores

def test_realiza_operadores():
    calcule = operadores
    resultado = calcule.realiza_operacao(x, y)
    assert resultado == ()

