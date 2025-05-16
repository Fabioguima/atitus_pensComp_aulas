def eh_primo(numero: int) -> bool:
    # Caso o número seja menor ou igual a 1, não é primo
    if numero <= 1:
        return False
    # Iteramos de 2 até o número - 1
    for i in range(2, numero):
        # Se o número for divisível por algum número diferente de 1 e ele mesmo, não é primo
        if numero % i == 0:
            return False
    # Se passar por todos os números sem ser divisível por nenhum, é primo
    return True

def lista_primos(num):
    lista = []
    for numero in range(num + 1):
        if eh_primo(numero):
            lista.append(numero)
    return lista

def test():
    assert lista_primos(10) == [2, 3, 5, 7]
    assert lista_primos(13) == [2, 3, 5, 7, 11, 13]
    assert lista_primos(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

print(lista_primos(10) == [2, 3, 5, 7])
print(lista_primos(13) == [2, 3, 5, 7, 11, 13])
print(lista_primos(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
