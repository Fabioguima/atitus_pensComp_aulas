# https://leetcode.com/problems/jewels-and-stones/description/


def stones_jewels(stones, jewels):
    contador = 0
    for letra in stones:
            if letra in jewels:
                contador += 1
    return contador

def test_stones_jewels():
    assert stones_jewels(jewels="aA", stones="aAAbbbb") == 3
    assert stones_jewels(jewels="z", stones="ZZ") == 0

print(stones_jewels(jewels="aA", stones="aAAbbbb") == 3)
print(stones_jewels(jewels="z", stones="ZZ") == 0)

