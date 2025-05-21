#Meses sao representados como: 1=Jan, 2=Feb, 3=Mar..


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

