#   MINHA SOLUÇÃO

#   COMENTADO PELO FATO DE NÃO TER DEF TEST

'''''
LEN_CEP = 8

def user_consulta():
    cep = input('Digite o CEP que deseja validar: ')
    if cep != '0':
        validador_cep(cep)
    else:
        print('Consulta CEP finalizado')

def validador_cep(cep):
    if len(cep) != LEN_CEP:
        print('Digite um CEP válido')
        return user_consulta
    for char in cep:
        if not char.isdigit():
            print('Digite um CEP válido')
            return user_consulta
    return confere_endereco(cep)


def confere_endereco(cep):
    if ja_consultado(cep):
        print(f"O CEP {cep} já foi consultado anteriormente.")
        user_consulta()
    else:
        print()
        print(f'Busca site externo. LOST MONEY ︶︹︺')
        obtem_dados_endereco(cep) #uf: localidade:
        print()
        print(enderecos)
        print()
        user_consulta()

def ja_consultado(cep):
    for uf in enderecos.keys():
        for localidade in enderecos[uf].keys():
            if cep in enderecos[uf][localidade]:
                return True


enderecos = {

}

def obtem_dados_endereco(cep):
    import http.client
    import json

    url = f"/ws/{cep}/json/"
    conn = http.client.HTTPSConnection("viacep.com.br")
    conn.request("GET", url)
    response = json.loads(conn.getresponse().read().decode())
    conn.close()

        # Exemplo de resposta
    # {    #   'uf': 'RS',
                    #'localidade': 'Porto Alegre',
                            #'[cep': '91110-000',]
    # }

    uf = response['uf']
    localidade = response['localidade']
    cep1 = response['cep']

    if uf not in enderecos:
        enderecos[uf] = {}
    if localidade not in enderecos[uf]:
        enderecos[uf][localidade] = []
    if cep1 not in enderecos[uf][localidade]:
        enderecos[uf][localidade].append(cep1)
    return response


user_consulta()
'''



#   SOLUÇÃO PROFESSOR



import http.client
import json

LEN_CEP = 8


def get_cep_data_from_api(val):
    url = f"/ws/{val}/json/"
    conn = http.client.HTTPSConnection("viacep.com.br")
    conn.request("GET", url)
    response = json.loads(conn.getresponse().read().decode())
    conn.close()
    return response


def is_cep_valid(val):
    if len(val) != LEN_CEP:
        return False
    for char in val:
        if not char.isdigit():
            return False
    return True


def consuta_ceps_conhecidos(ceps_conhecidos, cep):
    for uf in ceps_conhecidos.keys():
        for localidade in ceps_conhecidos[uf].keys():
            if cep in ceps_conhecidos[uf][localidade]:
                return True
    return False


def main():
    contador_consultas = 0
    enderecos = {}

    while True:
        print("Você consultou um total de:", contador_consultas, "vezes")
        print("Dados em memória: ", enderecos)
        print()

        cep = input("Digite o seu cep:")
        if not is_cep_valid(cep):
            print("CEP inválido")
            continue

        if consuta_ceps_conhecidos(enderecos, cep):
            print("Já conhecemos este cep")
            continue

        contador_consultas += 1
        response = get_cep_data_from_api(cep)

        uf = response["uf"]
        localidade = response["localidade"]

        if uf in enderecos:
            if localidade in enderecos[uf]:
                enderecos[uf][localidade].append(cep)
            else:
                enderecos[uf][localidade] = [cep, ]
        else:
            enderecos[uf] = {localidade: [cep, ]}


main()

