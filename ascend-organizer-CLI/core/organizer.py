from pathlib import Path
import shutil

from core.categories import obter_categorias
from core.logger import registrar_log


DOWNLOADS_DIR = Path.home() / "Downloads"


def organizar_arquivos():

    categorias = obter_categorias()

    for arquivo in DOWNLOADS_DIR.iterdir():

        if arquivo.is_file():

            extensao = arquivo.suffix.lower()

            if extensao in categorias:

                nome_pasta = categorias[extensao]

                pasta_destino = DOWNLOADS_DIR / nome_pasta

                pasta_destino.mkdir(exist_ok=True)

                destino = pasta_destino / arquivo.name

                try:

                    shutil.move(
                        str(arquivo),
                        str(destino)
                    )

                    registrar_log(
                        f"{arquivo.name} movido para {nome_pasta}"
                    )

                except Exception as erro:

                    registrar_log(
                        f"ERRO: {erro}"
                    )