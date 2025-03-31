def fatorial(numero):
    if numero <= -1:
        return None
    resultado = 1
    contador = 1
    while contador <= numero:
        resultado = resultado * contador
        contador = contador + 1
    return resultado

def test():
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(3) == 6
    assert fatorial(4) == 24
    assert fatorial(5) == 120
    assert fatorial(-1) is None

print(fatorial(4))