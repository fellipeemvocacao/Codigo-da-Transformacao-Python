from faker import Faker
import json

fake = Faker('pt_BR')

def gerar_clientes_ficticios(quantidade):
    lista_clientes = {}
    
    print(f"🚀 Gerando {quantidade} clientes aleatórios...")
    
    for i in range(quantidade):
        id_cliente = str(200 + i)
        
        lista_clientes[id_cliente] = {
            "nome": fake.name(),
            "email": fake.email(),
            "cidade": fake.city(),
            "data_cadastro": fake.date_between(start_date='-2y', end_date='today').strftime('%d/%m/%Y')
        }
    
    return lista_clientes

novos_dados = gerar_clientes_ficticios(5)
with open("clientes_teste.json", "w", encoding="utf-8") as f:
    json.dump(novos_dados, f, indent=4, ensure_ascii=False)

print("✅ Arquivo 'clientes_teste.json' gerado com sucesso!")