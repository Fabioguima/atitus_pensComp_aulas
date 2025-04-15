"""nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
nota_3 = int(input("Digite a terceira nota: "))
nota_4 = int(input("Digite a quarta nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 7:
    print(f"Sua nota foi {media}. Aluno aprovado!")
else:
    print(f"Sua nota foi {media}.Aluno reprovado!")

def test():
    assert status_aluno([10, 10, 10, 10])
    assert status_aluno([10, None, 10, 10])

    assert not status_aluno([10, 5, None, 5])
    assert not status_aluno([5, 5, 5, 5])
    assert not status_aluno([0, 0, 0, 0])
