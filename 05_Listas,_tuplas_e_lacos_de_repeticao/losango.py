def desenha_losango(altura):
    if altura % 2 == 0 or altura <3:
        print(f'O numero {altura} não é impar ou é menor que o valor solicitdo')
    
    else:
        resultado = 0
        contador = 2
        velha = "#"
        while contador <= altura:
            resultado = resultado + contador
            contador = contador + 1
            jogo = velha * contador
            print(jogo)
        #return resultado

altura = int(input("Digite um valor ímpar maior ou igual a 3 para altura do losango: "))
desenha_losango(altura)

#Falta finalizar
