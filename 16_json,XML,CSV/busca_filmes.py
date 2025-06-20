import http.client
import urllib.parse
import json

def get_movies(texto_busca: str) -> dict:
    texto_busca_codificado = urllib.parse.quote(texto_busca)
    conn = http.client.HTTPSConnection("search.imdbot.workers.dev")
    conn.request("GET", f"/?q={texto_busca_codificado}")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def search_movie(movie_name: dict) -> dict:
    nome_filme = get_movies(movie_name)

    if nome_filme['description'] == []:
        print(f'\nEste filme com nome {movie_name} não foi encontrado na base de dados\n')
    else:    
        descricao_filme = nome_filme['description'][0]
        titulo_filme = descricao_filme['#TITLE']
        ano_filme = descricao_filme['#YEAR']
        avaliacoes_filme = descricao_filme['#IMDB_URL']
        poster_filme = descricao_filme["#IMG_POSTER"]

        resultado_da_busca = (f"\nTitulo: {titulo_filme}\nAno de Lançamento: {ano_filme}\nAvaliações do Filme: {avaliacoes_filme}\nPoster: {poster_filme}\n")
        print(resultado_da_busca)


nome_filme = input('Informe qual filme você busca: ')
search_movie(nome_filme)
