from pathlib import Path
from datetime import datetime


LOGS_DIR = Path("logs")

LOG_FILE = LOGS_DIR / "organizer.log"


def criar_pasta_logs():

    LOGS_DIR.mkdir(exist_ok=True)


def registrar_log(mensagem):

    criar_pasta_logs()

    horario = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    linha = f"[{horario}] {mensagem}\n"

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(linha)

    print(linha.strip())