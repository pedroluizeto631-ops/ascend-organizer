from pathlib import Path
import json


CONFIG_PATH = Path("config/config.json")


def carregar_config():

    try:

        with open(
            CONFIG_PATH,
            "r",
            encoding="utf-8"
        ) as arquivo:

            config = json.load(arquivo)

            return config

    except FileNotFoundError:

        print("config.json não encontrado.")

        return {}

    except json.JSONDecodeError:

        print("Erro no JSON.")

        return {}


def obter_categorias():

    config = carregar_config()

    return config.get("pastas", {})