from pathlib import Path
import json

CONFIG_PATH = Path("Config/config.json")

def carregar_config():
    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as arquivo:
            config = json.load(arquivo)
            return config
        
    except FileNotFoundError:
        print(f"Arquivo de configuração não encontrado")
        return { }
    
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo de configuração")
    return { }

def obter_categorias():
    config = carregar_config()

    return config.get("pastas",{})
