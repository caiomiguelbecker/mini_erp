

import tkinter as tk
from tkinter import messagebox

from app.core.idioma import Idioma



class Fornecedor_Categoria_View:
    def __init__(
        self,
        root,
        controller,
        fornecedor,
        categorias_disponiveis
    ):
        self.root = root
        self.controller = controller
        self.fornecedor = fornecedor
        self._categorias = categorias_disponiveis
        self.configurar_janela()
        self.criar_componentes()
        self.preencher_lista()

    def configurar_janela(self):
        self.root.title(
            f"{Idioma.t('fornecedor_categoria.titulo_prefixo')} {self.fornecedor.nome_fantasia}"
        )
        self.root.geometry("400x450")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = f"{Idioma.t('fornecedor_categoria.titulo_prefixo')} {self.fornecedor.nome_fantasia}",
            font = ("Arial", 12, "bold"),
            wraplength = 380
        )
        self.lbl_titulo.pack(
            padx = 10,
            pady = 10
        )
        self.lbl_instrucao = tk.Label(
            self.root,
            text = Idioma.t("fornecedor_categoria.instrucao")
        )
        self.lbl_instrucao.pack(
            padx = 10,
            anchor = "w"
        )
        self.lst_categorias = tk.Listbox(
            self.root,
            selectmode = tk.MULTIPLE,
            height = 15
        )
        self.lst_categorias.pack(
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
        for categoria in self.fornecedor.categorias:
            ids_associados.append(categoria.id)

        for indice, categoria in enumerate(self._categorias):
            self.lst_categorias.insert(tk.END, categoria.nome)
            if categoria.id in ids_associados:
                self.lst_categorias.selection_set(indice)

    def salvar(self):

        indices_selecionados = self.lst_categorias.curselection()

        categorias_selecionadas = []
        for indice in indices_selecionados:
            categorias_selecionadas.append(self._categorias[indice])

        self.controller.salvar_categorias(
            self,
            self.fornecedor,
            categorias_selecionadas
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