

import tkinter as tk
from tkinter import messagebox



class Login_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("Login")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = "Sistema Corporativo ERP",
            font = ("Arial", 14, "bold"),
        )
        self.lbl_titulo.pack(
            pady = 20
        )
        self.frm_dados = tk.Frame(
            self.root
        )
        self.frm_dados.pack(
            pady = 5
        )
        self.lbl_email = tk.Label(
            self.frm_dados,
            text = "E-mail:"
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
            text = "Senha:"
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
            text = "Entrar",
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

    def ao_pressionar_enter(self, event):
        self.controller.autenticar()

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
