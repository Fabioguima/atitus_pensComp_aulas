#altura = int(input("Digite um valor ímpar para a altura do losango: "))

def losango(altura):
    if altura % 2 == 0:
        altura = altura + 1
        print("O valor digitado era par, usaremos", altura, "no lugar")

    meio = altura // 2  
    for linha_atual in range(altura): 
        if linha_atual <= meio:
            num_espacos = meio - linha_atual
            num_star = linha_atual * 2 + 1
        else:  
            num_espacos = linha_atual - meio
            num_star = altura - (linha_atual - meio) * 2
        print("." * num_espacos + "#" * num_star)

def test():
    losango(3)


#print(losango(3))