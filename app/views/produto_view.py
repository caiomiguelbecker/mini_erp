

from app.models.produto import Produto
from app.core.idioma import Idioma

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



class Produto_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._fornecedores = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("produto.janela_titulo"))
        self.root.geometry("800x600")
        self.root.resizable(False, False)


    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = Idioma.t("produto.titulo"),
            font = ("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 4,
            padx = 5,
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = Idioma.t("produto.dados_frame")
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan=4,
            padx = 10,
            pady = 5,
            sticky = "ew"
        )
        self.frm_dados.grid_columnconfigure(0, weight=0)
        self.frm_dados.grid_columnconfigure(1, weight=1)
        self.frm_dados.grid_columnconfigure(2, weight=0)
        self.frm_dados.grid_columnconfigure(3, weight=1)
        self.lbl_id = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('comum.id')}:"
        )
        self.lbl_id.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width = 10,
            state = "readonly"
        )
        self.txt_id.grid(
            row = 0,
            column= 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('comum.nome')}:"
        )
        self.lbl_nome.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_nome.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_fornecedores = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('produto.fornecedor')}:"
        )
        self.lbl_fornecedores.grid(
            row = 1,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.cmb_fornecedores = ttk.Combobox(
            self.frm_dados,
            width = 37,
            state = "readonly"
        )
        self.cmb_fornecedores.grid(
            row = 1,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_estoque = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('produto.estoque')}:"
        )
        self.lbl_estoque.grid(
            row = 2,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_estoque = tk.Entry(
            self.frm_dados,
            width = 20
        )
        self.txt_estoque.grid(
            row = 2,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_preco = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('produto.preco')}:"
        )
        self.lbl_preco.grid(
            row = 2,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_preco = tk.Entry(
            self.frm_dados,
            width = 20
        )
        self.txt_preco.grid(
            row = 2,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border = 2,
            relief = "groove"
        )
        self.frm_botoes.grid(
            row = 4,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 4,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text = Idioma.t("comum.novo"),
            width = 15
        )
        self.btn_novo.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text = Idioma.t("comum.salvar"),
            width = 15
        )
        self.btn_salvar.grid(
            row = 0,
            column = 1,
            padx = 5,
            pady = 5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text = Idioma.t("comum.alterar"),
            width = 15
        )
        self.btn_alterar.grid(
            row = 0,
            column = 2,
            padx = 5,
            pady = 5
        )
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text = Idioma.t("comum.excluir"),
            width = 15
        )
        self.btn_excluir.grid(
            row = 0,
            column = 3,
            padx = 5,
            pady = 5
        )
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text = Idioma.t("comum.fechar"),
            width = 15
        )
        self.btn_fechar.grid(
            row = 0,
            column = 4,
            padx = 5,
            pady = 5
        )
        self.tbl_produtos = ttk.Treeview(
            self.root,
            height = 10
        )
        self.tbl_produtos.grid(
            row = 3,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )

    def configurar_treeview(self):
        self.tbl_produtos["columns"] = (
            "id",
            "nome",
            "estoque",
            "preco",
            "valor_estoque",
            "fornecedor"
        )
        self.tbl_produtos.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_produtos.column(
            "id",
            width = 10,
            anchor = "center"
        )
        self.tbl_produtos.column(
            "nome",
            width = 40
        )
        self.tbl_produtos.column(
            "estoque",
            width = 20
        )
        self.tbl_produtos.column(
            "preco",
            width = 20
        )
        self.tbl_produtos.column(
            "valor_estoque",
            width = 30
        )
        self.tbl_produtos.column(
            "fornecedor",
            width = 40
        )
        self.tbl_produtos.heading(
            "id",
            text = Idioma.t("comum.id")
        )
        self.tbl_produtos.heading(
            "nome",
            text = Idioma.t("comum.nome")
        )
        self.tbl_produtos.heading(
            "estoque",
            text = Idioma.t("produto.estoque")
        )
        self.tbl_produtos.heading(
            "preco",
            text = Idioma.t("produto.preco")
        )
        self.tbl_produtos.heading(
            "valor_estoque",
            text = Idioma.t("produto.valor_estoque")
        )
        self.tbl_produtos.heading(
            "fornecedor",
            text = Idioma.t("produto.fornecedor")
        )
    def configurar_eventos(self):
        self.btn_novo.config(
            command = self.controller.new
        )
        self.btn_salvar.config(
            command = self.controller.save
        )
        self.btn_alterar.config(
            command = self.controller.update
        )
        self.btn_excluir.config(
            command = self.controller.delete
        )
        self.btn_fechar.config(
            command = self.fechar
        )
        self.tbl_produtos.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_produto

        )
    def carregar_fornecedores(self, fornecedores):
        self._fornecedores = fornecedores
        valores = []
        for fornecedor in fornecedores:
            valores.append(
                f"{fornecedor.id} - {fornecedor.nome_fantasia}"
            )
        self.cmb_fornecedores["values"] = valores
        self.cmb_fornecedores.set("")

    def preencher_campos(self, produto):

        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(produto.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_nome.insert(
            0,
            produto.nome
        )

        self.txt_estoque.insert(
            0,
            str(produto.estoque)
        )

        self.txt_preco.insert(
            0,
            str(produto.preco)
        )

        for indice, fornecedor in enumerate(self._fornecedores):
            if fornecedor.id == produto.fornecedor.id:
                self.cmb_fornecedores.current(indice)
                break

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome.delete(0, tk.END)
        self.txt_estoque.delete(0, tk.END)
        self.txt_preco.delete(0, tk.END)
        self.cmb_fornecedores.set("")
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_produtos.get_children():
            self.tbl_produtos.delete(item)


    def get_id_selecionado(self):

        item = self.tbl_produtos.selection()[0]

        return self.tbl_produtos.item(item)["values"][0]

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            Idioma.t("comum.confirmacao"),
            Idioma.t("produto.confirmar_exclusao"),
            parent=self.root
        )

    def ler_dados_produto(self):
        nome = self.txt_nome.get()
        estoque = int(self.txt_estoque.get())
        preco = float(self.txt_preco.get())
        indice = self.cmb_fornecedores.current()
        if indice < 0:
            raise ValueError("produto.erro_fornecedor_nao_selecionado")
        fornecedor = self._fornecedores[indice]
        return nome, estoque, preco, fornecedor

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
    def exibir_produtos(self, produtos):

        self.limpar_treeview()

        for produto in produtos:

            self.tbl_produtos.insert(
                "",
                tk.END,
                values=(
                    produto.id,
                    produto.nome,
                    produto.estoque,
                    f"{produto.preco:.2f}",
                    f"{produto.valor_estoque:.2f}",
                    produto.fornecedor.nome_fantasia
                )
            )
    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_fornecedores()
        self.controller.get_all()