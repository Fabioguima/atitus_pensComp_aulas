def soma_str(param):
    soma = 0
    for n in param:
        try:
            inteiro = int(n)
            soma += inteiro
        except:
            continue
    return soma

def test():
    assert soma_str("") == 0
    assert soma_str("a") == 0
    assert soma_str("4") == 4
    assert soma_str("5ab6") == 11  # 5+6
    assert soma_str("3 -4 z5") == 12  # 3+4+5, ignore o sinal
    assert soma_str("11a2z3") == 7  # 1+1+2+3

print(soma_str("") == 0)
print(soma_str("a") == 0)
print(soma_str("4") == 4)
print(soma_str("5ab6") == 11)
print(soma_str("3 -4 z5") == 12)
print(soma_str("11a2z3") == 7)
