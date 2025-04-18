def letra_em_texto(texto, letra):
    # Se esta letra existe dentro do texto (sem usar 'in')
   try:
       texto.index(letra)
       return (f"A letra --> {letra} <-- existe no texto.")
   except:
       return(f"A letra --> {letra} <-- não existe no texto.")

def conta_letra_em_texto(texto, letra):
    # Quantas vezes essa letra aparece no texto (sem usar '.count()')
    numero_vezes = 0
    letra1 = letra
    for letra in texto:
        if letra == letra1:
            numero_vezes = numero_vezes + 1
    return numero_vezes
        
def texto_sem_letra(texto, letra):
    # O texto novamente, removendo todas ocorrências desta letra (sem usar 'replace()')
        texto_modificado_sem_letra = ""
        sem_letra = letra
        for letra in texto:
            if sem_letra == letra:
                pass
            else:
                texto_modificado_sem_letra = (texto_modificado_sem_letra + letra)
        return texto_modificado_sem_letra
    


def texto_com_letra_upper(texto, letra):
    # O texto novamente, trocando essa letra por usa versão maiúscula  (sem usar 'replace()')
        texto_modificado = ""
        letra_upper = letra
        for letra in texto:
            if letra_upper == letra:
                texto_modificado = (texto_modificado + letra.upper())
            else:
                texto_modificado = (texto_modificado + letra)
        return texto_modificado

def test():
    assert letra_em_texto("Pensamento Computacional", "a")
    assert letra_em_texto("Pensamento Computacional", " ")
    assert not letra_em_texto("Pensamento Computacional", "A")
    assert not letra_em_texto("Pensamento Computacional", "c")

    assert conta_letra_em_texto("Pensamento Computacional", "a") == 3
    assert conta_letra_em_texto("Pensamento Computacional", "A") == 0
    assert conta_letra_em_texto("Pensamento Computacional", "e") == 2

    assert texto_sem_letra("Pensamento Computacional", "a") == "Pensmento Computcionl"
    assert texto_sem_letra("Pensamento Computacional", "z") == "Pensamento Computacional"
    assert texto_sem_letra("Pensamento Computacional", " ") == "PensamentoComputacional"

    assert (
        texto_com_letra_upper("Pensamento Computacional", "a") == "PensAmento ComputAcionAl"
    )
    assert (
        texto_com_letra_upper("Pensamento Computacional", "z") == "Pensamento Computacional"
    )
    assert (
        texto_com_letra_upper("Pensamento Computacional", " ") == "Pensamento Computacional"
    )

print(letra_em_texto("Pensamento Computacional", "a"))