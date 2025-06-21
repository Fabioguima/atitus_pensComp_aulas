def soma_dois(lista: list, alvo: int) -> list:
    indices_soma = []
    for n in lista:
        for i in lista:
            if n == i:
                pass
            else:
                if (i + n) == alvo:
                    indice1 = lista.index(n)
                    indice2 = lista.index(i)
                    indices_soma.append(indice1)
                    indices_soma.append(indice2)
                    return indices_soma
    return None

def test():
    assert soma_dois([2, 7, 11, 15], 9) == [0, 1]  # l[0]+l[1] == 9
    assert soma_dois([3, 2, 4], 6) == [1, 2]
    assert soma_dois([3, 4], 7) == [0, 1]
    assert soma_dois([], 6) is None
    assert soma_dois([1], 6) is None
    assert soma_dois([1, 2], 6) is None

print(soma_dois([2, 7, 11, 15], 9) == [0, 1])
print(soma_dois([3, 2, 4], 6) == [1, 2])
print(soma_dois([3, 4], 7) == [0, 1])
print(soma_dois([], 6) is None)
print(soma_dois([1], 6) is None)
print(soma_dois([1, 2], 6) is None)