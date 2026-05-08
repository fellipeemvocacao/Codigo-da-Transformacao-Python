import json
import os
from manutencao.backup import realizar_backup
from interface.formatacao import exibir_titulo

def carregar_configuracoes():
    if not os.path.exists("configuracoes.json"):
        config = {
            "pasta_origem": "meus_documentos",
            "pasta_destino": "servidor_backup"
        }
        with open("configuracoes.json", "w") as f:
            json.dump(config, f, indent=4)
        return config
    
    with open("configuracoes.json", "r") as f:
        return json.load(f)

def executar_sistema():
    exibir_titulo("Iniciando Backup Automático")
    
    config = carregar_configuracoes()
    origem = config['pasta_origem']
    destino = config['pasta_destino']

    if not os.path.exists(origem):
        os.makedirs(origem)
        with open(f"{origem}/arquivo_importante.txt", "w") as f:
            f.write("Dados sensíveis de teste.")

    print(f"📁 Origem: {origem}")
    print(f"🚀 Destino: {destino}")
    
    sucesso, mensagem = realizar_backup(origem, destino)

    if sucesso:
        print(f"\n✅ Backup concluído com sucesso!")
        print(f"📍 Localizado em: {mensagem}")
    else:
        print(f"\n❌ Falha no backup: {mensagem}")

if __name__ == "__main__":
    executar_sistema()