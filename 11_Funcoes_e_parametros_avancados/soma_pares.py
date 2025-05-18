#Crie um método que recebe uma lista L e um valor X. 
# Retorne um bool indicando se é possível chegar em X ao somar dois valores quaisquer que pertencem a L. 

def soma_pares(numeros: list, alvo: int) -> bool:
    for lista in numeros:
        j = lista
        for i in numeros:
            if i + j == alvo:
                return True
            else:
                pass
    return False


def test():
    assert soma_pares([1, 2], 4)
    assert not soma_pares([8], 1)
    assert not soma_pares([8], 10)
    assert soma_pares([3, 4, 6], 9)
    assert soma_pares([3, 4, 6], 7)

#print(soma_pares([1, 2], 4))
#print(soma_pares([8], 1))
#print(soma_pares([8], 10))     ------------> ASSERTS
#print(soma_pares([3, 4, 6], 9))
#print(soma_pares([3, 4, 6], 7))