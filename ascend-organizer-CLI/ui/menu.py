import questionary

from ui.tree_view import mostrar_estrutura

from rich.console import Console
from rich.panel import Panel

from core.organizer import organizar_arquivos

console = Console()


def iniciar_menu():

    while True:

        console.clear()

        painel = Panel.fit(
            "[bold cyan]ASCEND ORGANIZER[/]",
            border_style="blue"
        )

        console.print(painel)

        opcao = questionary.select(
            "Escolha uma opção:",
            choices=[
                "📂 Organizar Downloads",
                "📜 Ver Logs",
                "❌ Sair"
            ]
        ).ask()

        # =========================
        # ORGANIZAR
        # =========================

        if opcao == "📂 Organizar Downloads":

            console.clear()

            console.print(
                "\n[bold green]Organizando arquivos...[/]\n"
            )

            organizar_arquivos()

            console.print(
                "\n[bold cyan]Estrutura final:[/]\n"
            )

            mostrar_estrutura()

            input("\nPressione ENTER para continuar...")

        # =========================
        # LOGS
        # =========================

        elif opcao == "📜 Ver Logs":

            console.clear()

            try:

                with open(
                    "logs/organizer.log",
                    "r",
                    encoding="utf-8"
                ) as arquivo:

                    logs = arquivo.read()

                    console.print(logs)

            except FileNotFoundError:

                console.print(
                    "[bold red]Nenhum log encontrado.[/]"
                )

            input("\nPressione ENTER para continuar...")

        # =========================
        # SAIR
        # =========================

        elif opcao == "❌ Sair":

            console.print(
                "\n[bold red]Saindo do sistema...[/]"
            )

            break