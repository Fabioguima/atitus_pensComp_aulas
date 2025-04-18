"""Calculadora de classe social. Crie um método que recebe uma lista com a remuneração mensal (em reais) de cada membro
da família e o valor do salário mínimo atual. Retorne a classe social correspondente à remuneração per capta. Considere:

1. Classe A: mais de 15 salários mínimos;
2. Classe B: de 5 a 15 salários mínimos;
3. Classe C: de 3 a 5 salários mínimos;
4. Classe D: de 1 a 3 salários mínimos;
5. Classe E: até 1 salário mínimo."""

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
    elif per_capita > (1 * salario_minimo):
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

print(calcula_classe_social([1000], 1000) == "E")
