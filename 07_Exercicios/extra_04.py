def calcula_classe_social(salarios, salario_minimo):
    if not salarios:
        return None
    
    total_salarios = 0
    for numero in salarios:
        total_salarios = numero + total_salarios
    

    num_membros = len(salarios)
    per_capita = total_salarios / num_membros

    if per_capita > (15 * salario_minimo):
        return "A"
    elif per_capita >= (5 * salario_minimo):
        return "B"
    elif per_capita >= (3 * salario_minimo):
        return "C"
    elif per_capita >= (1 * salario_minimo):
        return "D"
    else:
        return "E"

def test():
    assert calcula_classe_social([], 1000) is None
    assert calcula_classe_social([1000], 1000) == "E"
    assert calcula_classe_social([500], 1000) == "E"
    assert calcula_classe_social([500], 1000) == "E"
    assert calcula_classe_social([1000, 0], 900) == "E"
    assert calcula_classe_social([1000], 900) == "D"
    assert calcula_classe_social([10000, 15000], 1000) == "B"
    assert calcula_classe_social([20000, 25000], 1000) == "A"
    assert calcula_classe_social([20000, 0, 0, 0, 0], 1000) == "C"

print(calcula_classe_social([20000, 25000], 1000) == "A")
