def real_para_dolar(valor, tx_conversao):
    #Calculo da cotação real --> Dolar
    return print(f'{valor / tx_conversao} usd')

def test():
    assert real_para_dolar(500, 5.20) == 96.23
    assert real_para_dolar(500, 1) == 500
    assert real_para_dolar(500, 6) == 83.33333333333333

print(real_para_dolar(500, 6))