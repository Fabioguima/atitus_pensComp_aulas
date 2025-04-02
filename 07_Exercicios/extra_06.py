def valor_pgto(valor, forma_pgto):
    dinheiro_pix = (valor - 15) / 100 * 100
    credito = (valor - 10) / 100 * 100
    parcelado_tres = valor + (valor * (10 / 100))

    if forma_pgto == 1:
        return dinheiro_pix
    if forma_pgto == 2:
        return credito
    if forma_pgto == 3:
        return valor
    if forma_pgto == 4:
        return parcelado_tres

def test():
    assert valor_pgto(100, 1) == 85
    assert valor_pgto(100, 2) == 90
    assert valor_pgto(100, 3) == 100
    assert valor_pgto(100, 4) == 110

print(valor_pgto(100, 4) == 110)
