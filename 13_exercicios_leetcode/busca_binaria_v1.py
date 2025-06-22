def busca_binaria(lista: list, valor: int) -> bool:
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            return True
        i += 1
    return False

def test_busca_binaria():
    assert busca_binaria([1, 3, 5, 7, 9, 11, 13, 15], 7)
    assert not busca_binaria([1, 3, 5, 7, 9, 11, 13, 15], 8)

print(busca_binaria([1, 3, 5, 7, 9, 11, 13, 15], 7))
print(busca_binaria([1, 3, 5, 7, 9, 11, 13, 15], 8))
