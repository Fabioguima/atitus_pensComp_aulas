def sao_anagramas(palavra1: str, palavra2: str) -> bool:
    for p1 in palavra1:
        if p1 in palavra2:
            pass
        else:
            return False
    return True

def test_sao_anagramas():
    assert sao_anagramas("amor", "roma")
    assert sao_anagramas("iracema", "america")
    assert sao_anagramas("estudo", "duetos")

    assert not sao_anagramas("banana", "anana")
    assert not sao_anagramas("banana", "")
    assert not sao_anagramas("banana", "abc")

#print(sao_anagramas("amor", "roma"))
#print(sao_anagramas("iracema", "america"))
#print(sao_anagramas("banana", "anana"))
#print(sao_anagramas("banana", ""))
print(sao_anagramas("banana", "abc"))
