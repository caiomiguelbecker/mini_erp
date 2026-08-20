

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from app.core.idioma import Idioma



class Login_View:

    # Ordem dos idiomas exibidos no combobox da tela de login.
    # O índice escolhido no combobox é usado para descobrir o código
    # do idioma (pt/en) que deve ser passado para Idioma.definir().
    CODIGOS_IDIOMA = ["pt", "en"]
    NOMES_IDIOMA = ["Português", "English"]

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("login.janela_titulo"))
        self.root.geometry("400x290")
        self.root.resizable(False, False)

    def criar_componentes(self):

        self.frm_idioma = tk.Frame(
            self.root
        )
        self.frm_idioma.pack(
            pady = (10, 0),
            fill = "x",
            padx = 10
        )
        self.lbl_idioma = tk.Label(
            self.frm_idioma,
            text = f"{Idioma.t('login.idioma')}:"
        )
        self.lbl_idioma.pack(
            side = "left"
        )
        self.cmb_idioma = ttk.Combobox(
            self.frm_idioma,
            width = 12,
            state = "readonly",
            values = self.NOMES_IDIOMA
        )
        self.cmb_idioma.current(
            self.CODIGOS_IDIOMA.index(Idioma.ATUAL)
        )
        self.cmb_idioma.pack(
            side = "right"
        )

        self.lbl_titulo = tk.Label(
            self.root,
            text = Idioma.t("login.sistema_titulo"),
            font = ("Arial", 14, "bold"),
        )
        self.lbl_titulo.pack(
            pady = 15
        )
        self.frm_dados = tk.Frame(
            self.root
        )
        self.frm_dados.pack(
            pady = 5
        )
        self.lbl_email = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('login.email')}:"
        )
        self.lbl_email.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "e"
        )
        self.txt_email = tk.Entry(
            self.frm_dados,
            width = 30
        )
        self.txt_email.grid(
            row = 0,
            column = 1,
            padx = 5,
            pady = 5
        )
        self.lbl_senha = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('login.senha')}:"
        )
        self.lbl_senha.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "e"
        )
        self.txt_senha = tk.Entry(
            self.frm_dados,
            width = 30,
            show = "*"
        )
        self.txt_senha.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5
        )
        self.btn_entrar = tk.Button(
            self.root,
            text = Idioma.t("login.entrar"),
            width = 15
        )
        self.btn_entrar.pack(
            pady = 20
        )
        self.txt_email.focus()

    def configurar_eventos(self):
        self.btn_entrar.config(
            command = self.controller.autenticar
        )
        self.txt_email.bind(
            "<Return>",
            self.ao_pressionar_enter
        )
        self.txt_senha.bind(
            "<Return>",
            self.ao_pressionar_enter
        )
        self.cmb_idioma.bind(
            "<<ComboboxSelected>>",
            self.ao_selecionar_idioma
        )

    def ao_pressionar_enter(self, event):
        self.controller.autenticar()

    def ao_selecionar_idioma(self, event):
        indice = self.cmb_idioma.current()
        if indice < 0:
            return
        codigo = self.CODIGOS_IDIOMA[indice]
        Idioma.definir(codigo)
        self.atualizar_textos()

    def atualizar_textos(self):
        self.root.title(Idioma.t("login.janela_titulo"))
        self.lbl_idioma.config(text = f"{Idioma.t('login.idioma')}:")
        self.lbl_titulo.config(text = Idioma.t("login.sistema_titulo"))
        self.lbl_email.config(text = f"{Idioma.t('login.email')}:")
        self.lbl_senha.config(text = f"{Idioma.t('login.senha')}:")
        self.btn_entrar.config(text = Idioma.t("login.entrar"))

    def ler_dados_login(self):
        email = self.txt_email.get()
        senha = self.txt_senha.get()
        return email, senha

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(
                "Mini ERP",
                mensagem,
                parent=self.root
            )
        else:
            messagebox.showerror(
                "Mini ERP",
                mensagem,
                parent=self.root
            )