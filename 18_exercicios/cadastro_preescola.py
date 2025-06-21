IDADE_PARA_MAIORIDADE = 18


def verifica_maioridade(idade: int) -> bool:
    if idade < IDADE_PARA_MAIORIDADE:
        return False
    else:
        return True


def verifica_email(email: str) -> bool:
    if email.find("@") < 1:
        return False
    if email.count('@') > 1:
        return False
    if not email.endswith('.com'):
        return False
    if email.count('.com') > 1:
        return False
    else:
        return True
    
def solicita_nome() -> str | None:
    pass


def test_verifica_maioridade():
    # Testes para verifica_maioridade
    assert not verifica_maioridade(-1)
    assert not verifica_maioridade(0)
    assert not verifica_maioridade(1)
    assert not verifica_maioridade(17)
    assert verifica_maioridade(18)
    assert verifica_maioridade(20)
    assert verifica_maioridade(100)

def test_verifica_email():
    # Testes para verifica_email
    # E-mail False
    assert not verifica_email('')
    assert not verifica_email('@')
    assert not verifica_email('@@')
    assert not verifica_email('abc@@abc.com')
    assert not verifica_email('abc@abc.edu')
    assert not verifica_email('a_b_c@a_b_c.com.com')
    assert not verifica_email('a_b_c@a_b_c.com.com.com')
    # E-mail True
    assert verifica_email('ABC@a_b_c.com')
    assert verifica_email('ABC@ABC.com')
    assert verifica_email('AbC@1BC.com')
    assert verifica_email('abc@abc.com')
    assert verifica_email('a23@123.com')
    assert verifica_email('a_b_c@a_b_c.com')






'''
print(verifica_email(''))
print(verifica_email('@'))
print(verifica_email('@@'))
print(verifica_email('abc@@abc.com'))
print(verifica_email('abc@abc.edu'))
print(verifica_email('a_b_c@a_b_c.com.com'))
print(verifica_email('a_b_c@a_b_c.com.com.com'))

print(verifica_email('ABC@a_b_c.com'))
print(verifica_email('ABC@ABC.com'))
print(verifica_email('AbC@1BC.com'))
print(verifica_email('abc@abc.com'))
print(verifica_email('a23@123.com'))
print(verifica_email('a_b_c@a_b_c.com'))
'''