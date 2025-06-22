'''
from datetime import date, timedelta

def parcelamento(valor, parcelas, dt_venda):
    resultado = []

    valor_parcela = valor // parcelas
    # Calcula o restante que sobra na divisão
    resto = valor % parcelas

    # Data do primeiro vencimento
    data_atual = dt_venda

    for i in range(parcelas):
        valor_parcela_atual = valor_parcela + (1 if i < resto else 0)
        resultado.append([valor_parcela_atual, data_atual])
        dia = data_atual.day
        mes = data_atual.month
        ano = data_atual.year
        if mes == 12:
            mes = 1
            ano += 1
        else:
            mes += 1
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            dia_final = 31
        elif mes == 2:
            # Verifica se é ano bissexto
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                dia_final = 29
            else:
                dia_final = 28
        else:
            dia_final = 30
        dia = min(dia, dia_final)
        data_atual = date(ano, mes, dia)

    return resultado

data_venda = date(2025, 1, 31)

def test_parcelamento():
    assert parcelamento(100, 1, data_venda) == [[100, data_venda]]
    assert parcelamento(100, 2, data_venda) == [
        [50, data_venda],
        [50, date(2025, 2, 28)]
    ]
    assert parcelamento(100, 3, data_venda) == [
        [33, data_venda],
        [33, date(2025, 2, 28)],
        [34, date(2025, 3, 31)]
    ]
    assert parcelamento(100, 3, data_venda) == [
        [25, data_venda],
        [25, date(2025, 2, 28)],
        [25, date(2025, 3, 31)],
        [25, date(2025, 4, 30)]
    ]
    assert parcelamento(100, 6, data_venda) == [
        [16, data_venda],
        [16, date(2025, 2, 28)],
        [17, date(2025, 3, 31)],
        [17, date(2025, 4, 30)],
        [17, date(2025, 5, 31)],
        [17, date(2025, 6, 30)]
    ]

print(parcelamento(100, 1, data_venda) == [[100, data_venda]])
print(parcelamento(100, 2, data_venda) == [
        [50, data_venda],
        [50, date(2025, 2, 28)]
    ])
print(parcelamento(100, 3, data_venda) == [
        [33, data_venda],
        [33, date(2025, 2, 28)],
        [34, date(2025, 3, 31)]
    ])
print(parcelamento(100, 3, data_venda) == [
        [25, data_venda],
        [25, date(2025, 2, 28)],
        [25, date(2025, 3, 31)],
        [25, date(2025, 4, 30)]
    ])
print(parcelamento(100, 6, data_venda) == [
        [16, data_venda],
        [16, date(2025, 2, 28)],
        [17, date(2025, 3, 31)],
        [17, date(2025, 4, 30)],
        [17, date(2025, 5, 31)],
        [17, date(2025, 6, 30)]
    ])

'''