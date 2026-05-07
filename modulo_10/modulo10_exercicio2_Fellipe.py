import requests
from datetime import datetime

def exibir_previsao(cidade, api_key):
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
        data = response.json()
        info = {
            "Cidade": data.get("name"),
            "País": data.get("sys", {}).get("country"),
            "Temperatura Atual": f"{data['main']['temp']}°C",
            "Sensação Térmica": f"{data['main']['feels_like']}°C",
            "Mínima/Máxima": f"{data['main']['temp_min']}°C / {data['main']['temp_max']}°C",
            "Condição": data['weather'][0]['description'].capitalize(),
            "Umidade": f"{data['main']['humidity']}%",
            "Vento": f"{data['wind']['speed']} m/s",
            "Nascer do Sol": datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
            "Pôr do Sol": datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
        }
        print("-" * 40)
        print(f"RELATÓRIO METEOROLÓGICO: {info['Cidade']}, {info['País']}")
        print("-" * 40)
        for chave, valor in info.items():
            if chave not in ["Cidade", "País"]:
                print(f"{chave:<20}: {valor}")
        print("-" * 40)

    except requests.exceptions.HTTPError:
        print("Erro: Cidade não encontrada ou chave de API inválida.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

CHAVE_API = "SUA_API_KEY_AQUI"
CIDADE = "Rio de Janeiro"

exibir_previsao(CIDADE, CHAVE_API)