

import customtkinter as ctk

from ui.components import (
    criar_botao,
    criar_titulo,
    criar_texto,
    criar_card
)

from core.organizer import organizar_arquivos


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        
        self.title("Auto Organizer")

        self.geometry("900x500")

        self.resizable(False, False)

    
        ctk.set_appearance_mode("dark")

        ctk.set_default_color_theme("blue")

        
        self.criar_interface()

    def criar_interface(self):

        

        sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        
        titulo = criar_titulo(
            sidebar,
            "Auto Organizer"
        )

        titulo.pack(
            pady=(40, 20)
        )

        
        descricao = criar_texto(
            sidebar,
            "Organize seus arquivos automaticamente"
        )

        descricao.pack(
            padx=20,
            pady=(0, 30)
        )

        
        botao_organizar = criar_botao(
            sidebar,
            "Organizar Arquivos",
            organizar_arquivos
        )

        botao_organizar.pack(
            pady=10
        )

        

        main_area = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        main_area.pack(
            side="right",
            expand=True,
            fill="both"
        )

        
        card = criar_card(main_area)

        card.pack(
            padx=40,
            pady=40,
            fill="both",
            expand=True
        )

        
        texto_card = criar_titulo(
            card,
            "Sistema pronto 🚀"
        )

        texto_card.pack(
            pady=(40, 20)
        )

        descricao_card = criar_texto(
            card,
            "Clique no botão para organizar os arquivos da pasta Downloads."
        )

        descricao_card.pack(
            padx=20
        )