# ui/components.py

import customtkinter as ctk


def criar_botao(master, texto, comando):
    """
    Cria um botão padrão do sistema
    """

    botao = ctk.CTkButton(
        master=master,
        text=texto,
        command=comando,
        width=200,
        height=45,
        corner_radius=12,
        font=("Segoe UI", 14, "bold")
    )

    return botao


def criar_titulo(master, texto):
    """
    Cria um título padrão
    """

    titulo = ctk.CTkLabel(
        master=master,
        text=texto,
        font=("Segoe UI", 28, "bold")
    )

    return titulo


def criar_card(master):
    """
    Cria um card/container
    """

    card = ctk.CTkFrame(
        master=master,
        corner_radius=15
    )

    return card


def criar_texto(master, texto):
    """
    Cria texto padrão
    """

    label = ctk.CTkLabel(
        master=master,
        text=texto,
        font=("Segoe UI", 14)
    )

    return label