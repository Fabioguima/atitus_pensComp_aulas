def get_response(coin_a: str, coin_b: str) -> dict:
    import http.client
    import json

    conn = http.client.HTTPSConnection("api.coinbase.com")
    conn.request("GET", f"/v2/prices/{coin_a}-{coin_b}/buy")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def get_exchange_rate(coin_a: str, coin_b: str) -> float:
    response = get_response(coin_a, coin_b)
    valor = response['data']["amount"]
    moeda_a = response['data']["base"]
    moeda_b = response['data']["currency"]
    get_new_value(moeda_a, moeda_b, valor)


def get_new_value(coin_a: str, coin_b: str, value: float) -> float:
    print(f'Uma {coin_a}, equivalem a ${value} da {coin_b}')


cambio_a, cambio_b = input('Forneça duas moedas que seja verificar taxa de cambio\nA primeira corresponde a quantatidae em valor na mesma quantidade da segunda: ').split()
get_exchange_rate(cambio_a, cambio_b)