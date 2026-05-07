import requests

def buscar_previsao(cidade, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': cidade,
        'appid': api_key,
        'units': 'metric', 
        'lang': 'pt_br'     
    }

    try:
        response = requests.get(url, params=params)
        
        response.raise_for_status()
        
        dados = response.json()

        temp = dados['main']['temp']
        clima = dados['weather'][0]['description']
        umidade = dados['main']['humidity']
        cidade_nome = dados['name']

        print(f"--- Previsão para {cidade_nome} ---")
        print(f"Temperatura: {temp}°C")
        print(f"Condição: {clima.capitalize()}")
        print(f"Umidade: {umidade}%")

    except requests.exceptions.HTTPError as err:
        print(f"Erro na requisição: {err}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

MINHA_CHAVE = "SUA_API_KEY_AQUI"
CIDADE_DESEJADA = "São Paulo"

buscar_previsao(CIDADE_DESEJADA, MINHA_CHAVE)