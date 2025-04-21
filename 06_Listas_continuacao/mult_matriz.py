def multiply_matrix_by_scalar(matrix, scalar):
    resultado = []

    for dentro_lista in matrix:
        nova_lista = []
        for dentro_lista2 in dentro_lista:
            nova_lista.append(scalar * dentro_lista2) # Adiciona o resultado dentro da variavel NOVA_LISTA

        resultado.append(nova_lista)    # Adiciona o resultado de NOVA_LISTA dentro da variavel RESULTADO     
            
    return resultado

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result_01 = [[3, 6, 9], [12, 15, 18], [21, 24, 27]]

def test():
    assert multiply_matrix_by_scalar(matrix_1, 3) == result_01

matrix_02 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
result_02 = [[8, 12, 16], [20, 24, 28], [32, 36, 40]]

def test():
    assert multiply_matrix_by_scalar(matrix_02, 4) == result_02

print(multiply_matrix_by_scalar(matrix_02, 4) == result_02)
