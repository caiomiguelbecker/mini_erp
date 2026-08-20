

import tkinter as tk
from tkinter import messagebox

from app.core.idioma import Idioma



class Perfil_Fornecedor_View:
    def __init__(
        self,
        root,
        controller,
        perfil,
        fornecedores_disponiveis
    ):
        self.root = root
        self.controller = controller
        self.perfil = perfil
        self._fornecedores = fornecedores_disponiveis
        self.configurar_janela()
        self.criar_componentes()
        self.preencher_lista()

    def configurar_janela(self):
        self.root.title(
            f"{Idioma.t('perfil_fornecedor.titulo_prefixo')} {self.perfil.nome}"
        )
        self.root.geometry("400x450")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = f"{Idioma.t('perfil_fornecedor.titulo_prefixo')} {self.perfil.nome}",
            font = ("Arial", 12, "bold"),
            wraplength = 380
        )
        self.lbl_titulo.pack(
            padx = 10,
            pady = 10
        )
        self.lbl_instrucao = tk.Label(
            self.root,
            text = Idioma.t("perfil_fornecedor.instrucao")
        )
        self.lbl_instrucao.pack(
            padx = 10,
            anchor = "w"
        )
        self.lst_fornecedores = tk.Listbox(
            self.root,
            selectmode = tk.MULTIPLE,
            height = 15
        )
        self.lst_fornecedores.pack(
            padx = 10,
            pady = 10,
            fill = "both",
            expand = True
        )
        self.frm_botoes = tk.Frame(
            self.root
        )
        self.frm_botoes.pack(
            pady = 10
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text = Idioma.t("comum.salvar"),
            width = 15,
            command = self.salvar
        )
        self.btn_salvar.grid(
            row = 0,
            column = 0,
            padx = 5
        )
        self.btn_cancelar = tk.Button(
            self.frm_botoes,
            text = Idioma.t("comum.cancelar"),
            width = 15,
            command = self.fechar
        )
        self.btn_cancelar.grid(
            row = 0,
            column = 1,
            padx = 5
        )

    def preencher_lista(self):

        ids_associados = []
        for fornecedor in self.perfil.fornecedores:
            ids_associados.append(fornecedor.id)

        for indice, fornecedor in enumerate(self._fornecedores):
            self.lst_fornecedores.insert(tk.END, fornecedor.nome_fantasia)
            if fornecedor.id in ids_associados:
                self.lst_fornecedores.selection_set(indice)

    def salvar(self):

        indices_selecionados = self.lst_fornecedores.curselection()

        fornecedores_selecionados = []
        for indice in indices_selecionados:
            fornecedores_selecionados.append(self._fornecedores[indice])

        self.controller.salvar_fornecedores(
            self,
            self.perfil,
            fornecedores_selecionados
        )

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

    def fechar(self):
        self.root.destroy()