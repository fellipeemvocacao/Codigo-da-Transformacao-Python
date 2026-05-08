import json

CAMINHO_JSON = "clientes.json"

def salvar_clientes(dicionario_clientes):
    try:
        with open(CAMINHO_JSON, 'w', encoding='utf-8') as f:
            json.dump(dicionario_clientes, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar: {e}")
        return False

def carregar_clientes():
    try:
        with open(CAMINHO_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Erro ao carregar: {e}")
        return {}