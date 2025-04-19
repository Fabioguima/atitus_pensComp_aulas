def status_aluno(notas):
    #Verificar se todas as notas são válidas
    #for nota in notas:
      #  if nota is None:
         #   return False
    
    #Calcula a média das notas
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    
    if media >= 7:
        return True  # Aprovado!
    else:
        return False  # Reprovado!

def test():
    assert status_aluno([10, 10, 10, 10])
    assert status_aluno([10, None, 10, 10]) 

    assert not status_aluno([10, 5, None, 5])
    assert not status_aluno([5, 5, 5, 5])
    assert not status_aluno([0, 0, 0, 0])

print(status_aluno([10, 10, 10, 10]))
