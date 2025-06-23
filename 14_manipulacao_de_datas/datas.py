from datetime import date, datetime, timedelta


# Crie método que recebe uma string (mm-dd-aaaa) e retorna uma data
def str_to_date(date_str):
    repartir_data = date_str.split('-')
    day = int(repartir_data[0])
    month = int(repartir_data[1])
    year = int(repartir_data[2])
    if day < 0 or day > 31:
        return None
    if month < 0 or month > 12:
        return None
    if year < 0 or year > 2999:
        return None
    return date(day=day, month=month, year=year)


def test_str_to_date():
    assert str_to_date('10-01-2025') == date(day=10, month=1, year=2025)
    assert str_to_date('10-99-2025') is None

print(str_to_date('10-01-2025') == date(day=10, month=1, year=2025))
print(str_to_date('10-99-2025') is None)


# O nome do dia da semana (“sábado”, “domingo”, …)
def nome_dia_semana(data):
    dia_da_semana = data.weekday()
    if dia_da_semana == 0:
        return 'segunda-feira'
    if dia_da_semana == 1:
        return 'terça-feira'
    if dia_da_semana == 2:
        return 'quarta-feira'
    if dia_da_semana == 3:
        return 'quinta-feira'
    if dia_da_semana == 4:
        return 'sexta-feira'
    if dia_da_semana == 5:
        return 'sábado'
    if dia_da_semana == 6:
        return 'domingo'

    return None

def test_nome_dia_semana():
    assert nome_dia_semana(date(year=2025, month=1, day=1)) == 'quarta-feira'
    assert nome_dia_semana(date(year=2025, month=1, day=2)) == 'quinta-feira'

print(nome_dia_semana(date(year=2025, month=1, day=1)) == 'quarta-feira')
print(nome_dia_semana(date(year=2025, month=1, day=2)) == 'quinta-feira')


# Quantos dias faltam para o final de semana
def dias_para_finde(data):
    ate_finde = data.weekday()
    sub = 5 - ate_finde  # 5 representa sabado que é o primeiro dia do final de semana, caso for SAB ou DOM retorna 0
    if sub < 0:
        return 0
    return sub

def test_dias_para_finde():
    assert dias_para_finde(date(year=2025, month=1, day=1)) == 3
    assert dias_para_finde(date(year=2025, month=1, day=2)) == 2

print(dias_para_finde(date(year=2025, month=1, day=1)) == 3)
print(dias_para_finde(date(year=2025, month=1, day=2)) == 2)

'''
# Quantos dias existem entre a data e hoje
def delta_dias(data_a, data_b):
    diferença = data_b - data_a
    #print(diferença.days)
    return diferença.days

def test_delta_dias():
    assert delta_dias(date(year=2025, month=1, day=1), date(year=2026, month=1, day=2)) == 365
    assert delta_dias(date(year=2026, month=1, day=1), date(year=2025, month=1, day=2)) == -365
    assert delta_dias(date(year=2025, month=1, day=1), date(year=2025, month=1, day=2)) == 0

print(delta_dias(date(year=2025, month=1, day=1), date(year=2026, month=1, day=2)) == 365)
print(delta_dias(date(year=2026, month=1, day=1), date(year=2025, month=1, day=2)) == -365)
print(delta_dias(date(year=2025, month=1, day=1), date(year=2025, month=1, day=2)) == 0)
'''

# O mesmo dia no próximo mês (ou o anterior próximo)
def proximo_mes(data_a):
    dia = data_a.day
    mes = data_a.month
    ano = data_a.year

    if mes == 12:
        mes = 1
        ano += 1
    else:
        mes += 1

    if mes == 12:
        proximo_mes_data = date(ano + 1, 1, 1)
    else:
        proximo_mes_data = date(ano, mes + 1, 1)

    ultimo_dia_mes = (proximo_mes_data - timedelta(days=1)).day

    if dia < ultimo_dia_mes:
        dia_final = dia
    else:
        dia_final = ultimo_dia_mes

    return date(ano, mes, dia_final)

def test_proximo_mes():
    assert proximo_mes(date(year=2025, month=1, day=1)) == date(year=2025, month=2, day=1)
    assert proximo_mes(date(year=2025, month=1, day=29)) == date(year=2025, month=2, day=28)
    assert proximo_mes(date(year=2024, month=1, day=29)) == date(year=2024, month=2, day=29)
    assert proximo_mes(date(year=2025, month=1, day=30)) == date(year=2025, month=2, day=28)

print(proximo_mes(date(year=2025, month=1, day=1)) == date(year=2025, month=2, day=1))
print(proximo_mes(date(year=2025, month=1, day=29)) == date(year=2025, month=2, day=28))
print(proximo_mes(date(year=2024, month=1, day=29)) == date(year=2024, month=2, day=29))
print(proximo_mes(date(year=2025, month=1, day=30)) == date(year=2025, month=2, day=28))


# 1 se esta data está no futuro, -1 se no passado ou 0 se for hoje.
def data_futuro(data: date) -> str:
    data_atual = date.today()
    if data > data_atual:
        return '1'
    elif data < data_atual:
        return '-1'
    else:
        return '0'

def test_data_futuro():
    assert data_futuro(date(day=1, month=1, year=2099)) == 1
    assert data_futuro(date(day=1, month=1, year=1999)) == -1
    assert data_futuro(date.today()) == 0

print(data_futuro(date(day=1, month=1, year=2099)))
print(data_futuro(date(day=1, month=1, year=1999)))
print(data_futuro(date.today()))