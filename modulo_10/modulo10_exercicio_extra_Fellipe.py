import requests

def buscar_filme(nome_filme, api_key):
    base_url = "https://api.themoviedb.org/3"
    search_url = f"{base_url}/search/movie"
    genre_url = f"{base_url}/genre/movie/list"
    
    params = {
        'api_key': api_key,
        'query': nome_filme,
        'language': 'pt-BR'
    }

    try:
        genre_resp = requests.get(genre_url, params={'api_key': api_key, 'language': 'pt-BR'})
        genre_resp.raise_for_status()
        generos_lista = {g['id']: g['name'] for g in genre_resp.json()['genres']}

        response = requests.get(search_url, params=params, timeout=10)
        response.raise_for_status()
        
        resultados = response.json().get('results', [])

        if not resultados:
            print(f"Nenhum filme encontrado com o nome: '{nome_filme}'")
            return

        filme = resultados[0]
        
        titulo = filme.get('title')
        sinopse = filme.get('overview') or "Sinopse não disponível."
        data_lancamento = filme.get('release_date', 'N/A')
        
        ids_generos = filme.get('genre_ids', [])
        generos_nomes = [generos_lista.get(id, "Desconhecido") for id in ids_generos]

        print("\n" + "="*50)
        print(f"RESULTADO DA BUSCA")
        print("="*50)
        print(f"Título       : {titulo}")
        print(f"Lançamento   : {data_lancamento}")
        print(f"Gênero(s)    : {', '.join(generos_nomes)}")
        print("-" * 50)
        print(f"Sinopse:\n{sinopse}")
        print("="*50 + "\n")

    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Erro: Falha na conexão. Verifique sua internet.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

SUA_CHAVE = "INSIRA_SUA_API_KEY_AQUI"
filme_input = input("Digite o nome do filme: ")

buscar_filme(filme_input, SUA_CHAVE)