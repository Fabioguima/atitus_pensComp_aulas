#Crie um método que recebe uma string S e retorna um bool indicando se a string é válida. Para ser válido:
#Todo ‘(‘ precisa ser fechado com ‘)’. 
#Não pode haver ‘)’ que não foi aberto.

def validador_parenteses(entrada: str) -> bool:
    parenteses = []
    for x in entrada:
        if x == '(':
            parenteses.append(x)
        elif x == ')':
            if not parenteses:
                return False
            parenteses.pop()
    return len(parenteses) == 0


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


print(validador_parenteses("()"))
print(validador_parenteses("()()"))
print(validador_parenteses("(())"))   # ------------> ASSERTS VÁLIDOS
print(validador_parenteses("(()()())"))
print(validador_parenteses("(((())()))"))

print(validador_parenteses(")"))
print(validador_parenteses("("))
print(validador_parenteses("()("))    # -------------> ASSERTS INVÁLIDOS
print(validador_parenteses("()()())"))
print(validador_parenteses("(((())())"))
