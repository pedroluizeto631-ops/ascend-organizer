# core/organizer.py

from pathlib import Path
import shutil

from core.categories import obter_categorias
from core.logger import registrar_log


# Caminho da pasta Downloads
DOWNLOADS_DIR = Path.home() / "Downloads"


def organizar_arquivos():
    """
    Organiza os arquivos da pasta Downloads
    """

    categorias = obter_categorias()

    # Percorre todos os itens da pasta
    for arquivo in DOWNLOADS_DIR.iterdir():

        # Verifica se é um arquivo
        if arquivo.is_file():

            # Pega a extensão do arquivo
            extensao = arquivo.suffix.lower()

            # Verifica se existe nas categorias
            if extensao in categorias:

                # Nome da pasta destino
                nome_pasta = categorias[extensao]

                # Caminho completo da pasta
                pasta_destino = DOWNLOADS_DIR / nome_pasta

                # Cria a pasta caso não exista
                pasta_destino.mkdir(exist_ok=True)

                # Caminho final do arquivo
                destino = pasta_destino / arquivo.name

                try:

                    # Move o arquivo
                    shutil.move(str(arquivo), str(destino))

                    mensagem = f"{arquivo.name} movido para {nome_pasta}"

                    registrar_log(mensagem)

                except Exception as erro:

                    registrar_log(
                        f"ERRO ao mover {arquivo.name}: {erro}"
                    )