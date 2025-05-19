#Meses sao representados como: 1=Jan, 2=Feb, 3=Mar..

'''
MESES_31_DIAS = [1, 3, 5, 7, 8, 10, 12]
MESES_30_DIAS = [4, 6, 9, 11]

def eh_bissexto(ano: int) -> bool:
    if ano % 4 == 0:
       return True
    else:
         return False


def total_dias_no_mes(mes: int, ano: int) -> int:
    if eh_bissexto(ano):
        if mes == 2:
            return 29
    if mes in MESES_31_DIAS:
        return 31
    if mes in MESES_30_DIAS:
        return 30

def test():
    assert total_dias_no_mes(1, 2024) == 31
    assert total_dias_no_mes(2, 2024) == 29
    assert total_dias_no_mes(3, 2024) == 31
    assert total_dias_no_mes(11, 2024) == 30

#print(total_dias_no_mes(1, 2024) == 31)
#print(total_dias_no_mes(2, 2024) == 29)  ----> TESTES TRUE
#print(total_dias_no_mes(3, 2024) == 31)
#print(total_dias_no_mes(11, 2024) == 30)

def formata_data(data: list) -> str:
    if data[0] > 0 and data[0] < 32:
        if data[1] > 0 and data[1] < 13:
            if data[2] > 0:
                return f'{data[0]}/{data[1]}/{data[2]}'


def test():
    assert formata_data([1, 2, 2024]) == "1/2/2024"
    assert formata_data([1, 12, 2024]) == "1/12/2024"

#print(formata_data([1, 2, 2024]) == "1/2/2024")
#print(formata_data([1, 12, 2024]) == "1/12/2024")  ----> TESTES TRUE


def calcula_diferenca(data1: list, data2: list) -> int:
    def dias_inicio(data):
        if formata_data(data):
            dia, mes, ano = data


        total_dias = 0


        for ano1 in range(1, ano + 1): # ------------------------------> ANO
            if eh_bissexto(ano1):
                total_dias += 366 
            else: 
                total_dias += 365
 
        for mes1 in range(1, mes + 1):  # ----------------------------------> MES
            if total_dias_no_mes(mes1, ano):
                total_dias = total_dias + total_dias_no_mes(mes1, ano)
        
        total_dias += dia #-----------------------------------------> DIAS

        return total_dias

    dias_data1 = dias_inicio(data1)  
    dias_data2 = dias_inicio(data2)    # -------------> CHAMA UM ANO POR VEZ PARA RETORNAR A QUANTIDADE DE DIAS

    #print(dias_data1)
    #print(dias_data2)

    diferença = dias_data2 - dias_data1

    #print(diferença)

    return diferença


    
def test():
    # Diferenca em dias entre 2/7/2004 e 27/5/2024 é de 7268 dias
    assert calcula_diferenca([2, 7, 2004], [27, 5, 2024]) == 7268
    # Diferenca entre 27/5/2024 e 2/7/2089 é de 23779 dias
    assert calcula_diferenca([27, 5, 2024], [2, 7, 2004 + 85]) == 23779
    # Diferenca entre 2/7/2004 e 2/7/2089 é de 31047 dias
    assert calcula_diferenca([2, 7, 2004], [2, 7, 2004 + 85]) == 31047
    # A data 27/5/2024 representa 23.409669211195926% entre 2/7/2004 e 2/7/2089


    # Diferenca em dias entre 24/7/1991 e 24/10/2024 é de 12146 dias
    assert calcula_diferenca([24, 7, 1991], [24, 10, 2024]) == 12146
    # Diferenca entre 24/10/2024 e 24/7/2076 é de 18900 dias
    assert calcula_diferenca([24, 10, 2024], [24, 7, 1991 + 85]) == 18900
    # Diferenca entre 24/7/1991 e 24/7/2076 é de 31046 dias
    assert calcula_diferenca([24, 7, 1991], [24, 7, 1991 + 85]) == 31046
    # A data 24/10/2024 representa 39.12259228241963% entre 24/7/1991 e 24/7/2076

print(calcula_diferenca([2, 7, 2004], [27, 5, 2024]) == 7268)
#print(calcula_diferenca([27, 5, 2024], [2, 7, 2004 + 85]) == 23779)
#print(calcula_diferenca([2, 7, 2004], [2, 7, 2004 + 85]) == 31047)

#print(calcula_diferenca([24, 7, 1991], [24, 10, 2024]) == 12146)
#print(calcula_diferenca([24, 10, 2024], [24, 7, 1991 + 85]) == 18900)
#print(calcula_diferenca([24, 7, 1991], [24, 7, 1991 + 85]) == 31046)

'''

##########################################################################


# EXERCICIO PEDIDO EM AULA COM INPUT

'''
print('Digite a data no formato DD/MM/AAAA')
print()

data_nascimento = input('Digite sua data de nascimento: ')
data_atual = input('Agora a data atual: ')
data_expectativa = input('Por último sua espectativa de vida: ')

MESES_31_DIAS = [1, 3, 5, 7, 8, 10, 12]
MESES_30_DIAS = [4, 6, 9, 11]

def eh_bissexto(ano: int) -> bool:
    if ano % 4 == 0:
       return True
    else:
         return False


def total_dias_no_mes(mes: int, ano: int) -> int:
    if eh_bissexto(ano):
        if mes == 2:
            return 29
    if mes in MESES_31_DIAS:
        return 31
    if mes in MESES_30_DIAS:
        return 30


def formata_data(data: str) -> list:
    data_formatada = data.split('/')
    data_int = []
    for i in data_formatada:
        inteiro_convertido = int(i)
        data_int.append(inteiro_convertido)

    return data_int
    

def calcula_diferenca(data1: list, data2: list, data3: list) -> int:
    def dias_inicio(data):
        data_int = formata_data(data)
        dia, mes, ano = data_int


        total_dias = 0  #---------> PONTO CHAVE DO CODIGO


        for ano1 in range(1, ano + 1): # ------------------------------> ANO
            if eh_bissexto(ano1):
                total_dias += 366 
            else: 
                total_dias += 365
 
        for mes1 in range(1, mes + 1):  # ----------------------------------> MES
            if total_dias_no_mes(mes1, ano):
                total_dias = total_dias + total_dias_no_mes(mes1, ano)
        
        total_dias += dia #-----------------------------------------> DIAS

        return total_dias

    data_nascimento = dias_inicio(data1)  
    data_atual = dias_inicio(data2)              # -------------> CHAMA UM ANO POR VEZ PARA RETORNAR A QUANTIDADE DE DIAS
    data_expectativa = dias_inicio(data3)



    diferenca_inicial_atual = data_atual - data_nascimento
    diferenca_atual_final = data_expectativa - data_atual
    diferenca_inicial_final = data_expectativa - data_nascimento

    percentual_vivido = (diferenca_inicial_atual / diferenca_inicial_final) * 100

    print(f'Diferença entre a INICIAL e ATUAL: {diferenca_inicial_atual} DIAS')
    print(f'Diferença entre a ATUAL e FINAL: {diferenca_atual_final} DIAS')
    print(f'Diferença entre a INICIAL e FINAL: {diferenca_inicial_final} DIAS')
    print()
    print(f'Seu percentual vivido foi de {percentual_vivido}%')
    print()


calcula_diferenca(data_nascimento, data_atual, data_expectativa)
'''