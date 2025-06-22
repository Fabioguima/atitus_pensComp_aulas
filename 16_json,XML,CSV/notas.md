    Para acessar dados dentro de [] lista
    Ex:
    "description": [
    {
      "#TITLE": "Matrix",
      "#YEAR": 1999,

    }]
    Usar:
         descricao_filme = nome_filme['description'][0]
        titulo_filme = descricao_filme['#TITLE']
        ano_filme = descricao_filme['#YEAR']
    Para entrar dentro da lista


x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x

    Para acessar dentro de {} dicionario
    Ex:
    {
  "data": {
    "amount": "103316.775",
    "base": "BTC",
    "currency": "USD"
  }
}
    Usar:
        valor = response['data']["amount"]
        moeda_a = response['data']["base"]
        moeda_b = response['data']["currency"]
    Para entrar dentro do dicionario.