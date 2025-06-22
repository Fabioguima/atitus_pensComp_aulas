# https://leetcode.com/problems/find-words-containing-character/


def findWordsContaining(words, letter):
    alvo = letter
    indices = []
    for letra in words:
        if alvo in letra:
          indice_letra = words.index(letra)
          indices.append(indice_letra)
    return indices

def test_findWordsContaining():
    # Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
    assert findWordsContaining(words=["leet", "code"], letter="e") == [0, 1]

    # Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
    assert findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], letter="a") == [0, 2]

    # Explanation: "z" does not occur in any of the words. Hence, we return an empty array.
    assert findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], letter="z") == []

print(findWordsContaining(words=["leet", "code"], letter="e") == [0, 1])
print(findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], letter="a") == [0, 2])
print(findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], letter="z") == [])
