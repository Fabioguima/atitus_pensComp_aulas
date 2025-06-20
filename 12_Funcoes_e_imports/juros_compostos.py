def calcular_juros_compostos(principal, taxa, tempo):
    valor = 0
    if tempo == 0:
        return principal
    else:
        valor += principal * (1 + taxa) ** tempo
    return valor

def calcular_juros_compostos_recursivo(principal, taxa, tempo):
    if tempo == 0:
        return principal
    else:
        return calcular_juros_compostos_recursivo(principal, taxa, tempo - 1) * (1 + taxa)
    
def test():
    assert calcular_juros_compostos(1000, 0.05, 5) == 1276.2815625000003
    assert calcular_juros_compostos(1000, 0.05, 10) == 1628.894626777442
    assert calcular_juros_compostos(1000, 0.05, 0) == 1000

    assert calcular_juros_compostos_recursivo(1000, 0.05, 5) == 1276.2815625000003
    #assert calcular_juros_compostos_recursivo(1000, 0.05, 10) == 1628.894626777442
    assert calcular_juros_compostos_recursivo(1000, 0.05, 0) == 1000

print(calcular_juros_compostos(1000, 0.05, 5) == 1276.2815625000003)
print(calcular_juros_compostos(1000, 0.05, 10) == 1628.894626777442)
print(calcular_juros_compostos(1000, 0.05, 0) == 1000)

print(calcular_juros_compostos_recursivo(1000, 0.05, 5) == 1276.2815625000003)
#print(calcular_juros_compostos_recursivo(1000, 0.05, 10) == 1628.894626777442)
print(calcular_juros_compostos_recursivo(1000, 0.05, 0) == 1000)
