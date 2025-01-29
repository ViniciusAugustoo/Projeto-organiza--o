from Program.matematica import matematica 

def test_somar():

    calcule = matematica()
    resultado = calcule.somar(1, 2)
    assert resultado == 3