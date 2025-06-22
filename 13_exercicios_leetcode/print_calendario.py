'''
def imprimir_calendario_mes(dia_inicial: int, total_dias: int):
    dias_semana = "Do.Se.Te.Qu.Qu.Se.Sá"
    calendario = [dias_semana]
    dias = list(range(1, total_dias + 1))
    espacos_iniciais = ['...' for _ in range(dia_inicial)]
    dias_com_espacos = espacos_iniciais + dias
    for i in range(0, len(dias_com_espacos), 7):
        semana = dias_com_espacos[i:i+7]
        linha = ""
        for dia in semana:
            if dia == '...':
                linha += '...'
            else:
                if dia < 10:
                    linha += f".{dia}"
                else:
                    linha += f"{dia}"

        while len(semana) < 7:
            linha += '...'
            semana.append('...')
        calendario.append(linha)
    return calendario

def test_imprimir_calendario_mes():
    assert imprimir_calendario_mes(0, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá",
        ".1..2..3..4..5..6..7",
        ".8..9.10.11.12.13.14",
        "15.16.17.18.19.20.21",
        "22.23.24.25.26.27.28",
        "29.30.31",
    ]

    assert imprimir_calendario_mes(1, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá"
        "....1..2..3..4..5..6"
        ".7..8..9.10.11.12.13"
        "14.15.16.17.18.19.20"
        "21.22.23.24.25.26.27"
        "28.29.30.31"
    ]

    assert imprimir_calendario_mes(2, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá"
        ".......1..2..3..4..5"
        ".6..7..8..9.10.11.12"
        "13.14.15.16.17.18.19"
        "20.21.22.23.24.25.26"
        "27.28.29.30.31"
    ]

print(imprimir_calendario_mes(0, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá",
        ".1..2..3..4..5..6..7",
        ".8..9.10.11.12.13.14",
        "15.16.17.18.19.20.21",
        "22.23.24.25.26.27.28",
        "29.30.31",
    ])

print(imprimir_calendario_mes(1, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá"
        "....1..2..3..4..5..6"
        ".7..8..9.10.11.12.13"
        "14.15.16.17.18.19.20"
        "21.22.23.24.25.26.27"
        "28.29.30.31"
    ])
print(imprimir_calendario_mes(2, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá"
        ".......1..2..3..4..5"
        ".6..7..8..9.10.11.12"
        "13.14.15.16.17.18.19"
        "20.21.22.23.24.25.26"
        "27.28.29.30.31"
    ])
'''