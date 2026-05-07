import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

def buscar_previsao_robusta(cidade, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': cidade, 'appid': api_key, 'units': 'metric', 'lang': 'pt_br'}

    try:
        response = requests.get(url, params=params, timeout=10)
        
        response.raise_for_status()
        try:
            dados = response.json()
        except ValueError:
            print("Erro: A resposta da API não é um JSON válido.")
            return

        temp = dados['main']['temp']
        desc = dados['weather'][0]['description']
        print(f"Clima em {dados['name']}: {temp}°C, {desc.capitalize()}.")
    
    except HTTPError as http_err:
        if response.status_code == 404:
            print("Erro: Cidade não encontrada. Verifique a ortografia.")
        elif response.status_code == 401:
            print("Erro: Chave de API inválida.")
        else:
            print(f"Erro HTTP ocorrido: {http_err}")

    except ConnectionError:
        print("Erro de Conexão: Verifique sua internet ou DNS.")

    except Timeout:
        print("Erro de Timeout: A API demorou demais para responder. Tente novamente.")

    except RequestException as req_err:
        print(f"Erro na requisição: {req_err}")

    except KeyError as key_err:
        print(f"Erro de Parsing: O campo {key_err} não foi encontrado nos dados da API.")
MINHA_CHAVE = "SUA_API_KEY_AQUI"
buscar_previsao_robusta("Curitiba", MINHA_CHAVE)