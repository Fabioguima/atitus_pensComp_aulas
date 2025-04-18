nota_1 = 10  #int(input("Digite a primeira nota: "))
nota_2 = 10  #int(input("Digite a segunda nota: "))
nota_3 = 10  #int(input("Digite a terceira nota: "))
nota_4 = 10  #int(input("Digite a quarta nota: "))

status_aluno = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if status_aluno >= 7:
    print(f"Sua nota foi {status_aluno}. Aluno aprovado!")
else:
    print(f"Sua nota foi {status_aluno}.Aluno reprovado!")

def test():
    assert status_aluno([10, 10, 10, 10])
    assert status_aluno([10, None, 10, 10])

    assert not status_aluno([10, 5, None, 5])
    assert not status_aluno([5, 5, 5, 5])
    assert not status_aluno([0, 0, 0, 0])
