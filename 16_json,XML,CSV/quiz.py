import http.client
import json
import random

def get_questions(amount: int = 10, difficulty: str = 'easy') -> dict:

    conn = http.client.HTTPSConnection("opentdb.com")
    conn.request("GET", f"/api.php?amount={amount}&difficulty={difficulty}&type=multiple")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def parse_text(html_string: str) -> str:
    import html

    # Convert HTML entity to regular single quote
    return html.unescape(html_string)

def escolhe_pergunta():
    perguntas_easy = get_questions()
    # Salva o arquivo em json
    with open('json,xml,csv/perguntas_easy.json', 'w', encoding='utf-8') as arquivo:
        json.dump(perguntas_easy, arquivo, ensure_ascii=False, indent=4)


    #Abre o arquivo
    with open('json,xml,csv/perguntas_easy.json', 'r', encoding='utf-8') as arquivo:
        perguntas = json.load(arquivo) 

    pergunta_escolhida = random.choice(perguntas["results"])

    pergunta = pergunta_escolhida["question"]
    resposta_certa = pergunta_escolhida["correct_answer"]
    resposta_errada = pergunta_escolhida["incorrect_answers"]

    # Remove a pergunta
    (perguntas["results"]).remove(pergunta_escolhida)
    
    # Salva a lista atualizada
    with open('json,xml,csv/perguntas_easy.txt', 'w', encoding='utf-8') as arquivo: 
        json.dump(perguntas, arquivo, ensure_ascii=False, indent=4)

    return pergunta, resposta_certa, resposta_errada



def start_quiz():
    lista = list(range(0, 11))
    pontos_user = 0

    for i in lista:
        pergunta, resposta_certa, resposta_errada = escolhe_pergunta()

        for per_user in pergunta:

            # EMBARALHAR OPÇÕES DE RESPOSTA
            opcoes = resposta_errada + [resposta_certa]
            random.shuffle(opcoes)

            # MOSTRA PERGUNTA
            print(pergunta)
            # MOSTRA RESPOSTA E AS ENUMERA
            for enumeracao, opcao in enumerate(opcoes, 1):
                print(f"{enumeracao}. {opcao}")


            resposta_usuario = input('Informe sua resposta: ')
            # VERIFICA SE A RESPOSTA DADA EM NUMEROS ESTÁ CORRETA
            try:
                resposta_numero = int(resposta_usuario)
                # VERIFICA SE A RESPOSTA DO USUÁRIO ESTA ENTRE O INTERVALO DE RESPOSTA 
                if 1 <= resposta_numero <= len(opcoes):

                    # SUBTAI -1 DO INDICE PARA PEGAR A POSIÇÃO CORRETA NA LISTA DE OPÇÕES
                    resposta_escolhida = opcoes[resposta_numero - 1]
                    if resposta_escolhida == resposta_certa:
                        print("Parabéns! Você acertou.")
                        pontos_user += 1
                        print('')
                        print(f'Sua Pontuação: {pontos_user}')
                        break
                    else:
                        print('')
                        print(f"Que pena! Você errou. A resposta correta era: {resposta_certa}")
                        print('')
                        return (print(f'Sua Pontuação foi de: {pontos_user}'))
                else:
                    print('')
                    print(f"Tente Novamente. Respostas válidas (1, 2, 3, 4)") # RESPOSTA VÁLIDA LETRAS
                    print('')
                    continue
            except:
                print('')
                print(f"Tente Novamente. Respostas válidas (1, 2, 3, 4)") # RESPOSTA VÁLIDA LETRAS
                print('')
                continue


    


start_quiz()
