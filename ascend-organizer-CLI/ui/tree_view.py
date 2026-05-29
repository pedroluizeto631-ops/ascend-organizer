from pathlib import Path

from rich.console import Console
from rich.tree import Tree


console = Console()


DOWNLOADS_DIR = Path.home() / "Downloads"


def mostrar_estrutura():

    arvore = Tree("📂 Downloads")

    for pasta in DOWNLOADS_DIR.iterdir():

        if pasta.is_dir():

            pasta_node = arvore.add(
                f"📁 {pasta.name}"
            )

            for arquivo in pasta.iterdir():

                if arquivo.is_file():

                    pasta_node.add(
                        f"📄 {arquivo.name}"
                    )

    console.print(arvore)