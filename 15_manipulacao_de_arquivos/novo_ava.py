import os

def limpa_nome_pasta(nome: str) -> str:
    nome_formatado = ''
    nome_minusculo = nome.lower()
    subs_espaco = nome_minusculo.replace(' ', '_').replace('ê', 'e').replace('ç', 'c').replace('ã', 'a')
    nome_formatado += subs_espaco
    return nome_formatado

def test_limpa_nome_pasta():
    assert limpa_nome_pasta('Ciência da Computação') == 'ciencia_da_computacao'
    assert limpa_nome_pasta('Administração') == 'administracao'

print(limpa_nome_pasta('Ciência da Computação') == 'ciencia_da_computacao')
print(limpa_nome_pasta('Administração') == 'administracao')

'''
def cria_pasta_curso(nome_curso: str) -> None:
    pasta = limpa_nome_pasta(nome_curso)
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        print(f"A pasta '{pasta}' foi criada com sucesso.")
    else:
        print(f"A pasta '{pasta}' já existe.")

def converte_alunos_em_lista(alunos_com_virgula: str) -> list:
    with open('ciencia_da_computacao/alunos.txt', 'w') as arquivo:
        conteudo = arquivo.write('\n'.join(alunos_com_virgula))
        return conteudo


def cria_alunos(alunos: list, nome_curso: str) -> None:
    curso = cria_pasta_curso(nome_curso)
    lista_alunos = converte_alunos_em_lista(alunos)



cria_alunos(['Fábio', 'Pedro', 'Lucas', 'Matheus'], 'Ciência da Computação')

'''
