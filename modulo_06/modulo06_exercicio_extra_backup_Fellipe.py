import shutil
import os
from datetime import datetime

def realizar_backup(origem, destino):
    if not os.path.exists(origem):
        return False, f"Erro: A pasta de origem '{origem}' não existe."

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pasta_final = os.path.join(destino, f"backup_{timestamp}")

    try:
        shutil.copytree(origem, pasta_final)
        return True, pasta_final
    except Exception as e:
        return False, str(e)