def maior_numero(lista):
    # Qual o maior número da lista.
    lista_maior = lista[0]
    for numero in lista:
        if numero > lista_maior:
            lista_maior = numero
    return lista_maior

def menor_numero(lista):
    # Qual o menor número da lista.
    lista_menor = lista[0]
    for numero in lista:
        if numero < lista_menor:
            lista_menor = numero
    return lista_menor


def numeros_pares(lista):
    # Quais números são pares.
    lista_pares = []
    for pares in lista:
        if pares % 2 == 0:
            lista_pares.append(pares)
        else:
            pass
    return lista_pares


def numeros_impares(lista):
    # Quais números são ímpares.
    lista_impares = []
    for impares in lista:
        if impares % 2 == 1:
            lista_impares.append(impares)
        else:
            pass
    return lista_impares


def numeros_positivo(lista):
    # Quais números são positivos
    positivos_lista = []
    for positivos in lista:
        if positivos >= 0:
            positivos_lista.append(positivos)
        else:
            pass
    return positivos_lista


def numeros_negativos(lista):
    # Quais números são negativos.
    negativos_lista = []
    for negativos in lista:
        if negativos < 0:
            negativos_lista.append(negativos)
        else:
            pass
    return negativos_lista

def soma_numeros(lista):
    # A soma de todos os números.
    soma = 0
    for numero in lista:
        soma = numero + soma
    return soma

lista_1 = [10, 0, -3, 42, 5, -6, 8, 91]
lista_2 = [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
lista_3 = [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]

def test():
    assert maior_numero(lista_1) == 91
    assert maior_numero(lista_2) == 95
    assert maior_numero(lista_3) == 92

    assert menor_numero(lista_1) == -6
    assert menor_numero(lista_2) == 2
    assert menor_numero(lista_3) == 5

    assert numeros_pares(lista_1) == [10, 0, 42, -6, 8]
    assert numeros_pares(lista_2) == [20, 2, 74, 22]
    assert numeros_pares(lista_3) == [92, 50, 28]

    assert numeros_impares(lista_1) == [-3, 5, 91]
    assert numeros_impares(lista_2) == [27, 19, 85, 3, 95, 11]
    assert numeros_impares(lista_3) == [45, 23, 17, 89, 57, 15, 5]

    assert numeros_positivo(lista_1) == [10, 0, 42, 5, 8, 91]
    assert numeros_positivo(lista_2) == [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
    assert numeros_positivo(lista_3) == [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]

    assert numeros_negativos(lista_1) == [-3, -6]
    assert numeros_negativos(lista_2) == []
    assert numeros_negativos(lista_3) == []

    assert soma_numeros(lista_1) == 147
    assert soma_numeros(lista_2) == 358
    assert soma_numeros(lista_3) == 421

print(soma_numeros(lista_1) == 147)
