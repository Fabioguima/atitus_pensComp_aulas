def validador_parenteses(entrada: str) -> bool:
    pass


# Valores válidos
assert validador_parenteses("()")
assert validador_parenteses("()()")
assert validador_parenteses("(())")
assert validador_parenteses("(()()())")
assert validador_parenteses("(((())()))")

# Valores inválidos
assert validador_parenteses(")")
assert validador_parenteses("(")
assert validador_parenteses("()(")
assert validador_parenteses("()()())")
assert validador_parenteses("(((())())")#Crie um método que recebe uma string S e retorna um bool indicando se a string é válida. Para ser válido:
#Todo ‘(‘ precisa ser fechado com ‘)’. 
#Não pode haver ‘)’ que não foi aberto.

def validador_parenteses(entrada: str) -> bool:
    parenteses_a = ''
    parenteses_b = ''

    for x in entrada:
        if x == '(':
            parenteses_a += x
        else:
            parenteses_b += x

    if len(parenteses_a) == len(parenteses_b):
        return True
    else:
        return False


def test():# Valores válidos
    assert validador_parenteses("()")
    assert validador_parenteses("()()")
    assert validador_parenteses("(())")
    assert validador_parenteses("(()()())")
    assert validador_parenteses("(((())()))")

def test():# Valores inválidos
    assert validador_parenteses(")")
    assert validador_parenteses("(")
    assert validador_parenteses("()(")
    assert validador_parenteses("()()())")
    assert validador_parenteses("(((())())")

'''
print(validador_parenteses("()"))
print(validador_parenteses("()()"))
print(validador_parenteses("(())"))    ------------> ASSERTS VÁLIDOS
print(validador_parenteses("(()()())"))
print(validador_parenteses("(((())()))"))

print(validador_parenteses(")"))
print(validador_parenteses("("))
print(validador_parenteses("()("))     -------------> ASSERTS INVÁLIDOS
print(validador_parenteses("()()())"))
print(validador_parenteses("(((())())"))
'''
