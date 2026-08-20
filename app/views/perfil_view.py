

from app.models.perfil import Perfil
from app.views.perfil_fornecedor_view import Perfil_Fornecedor_View
from app.core.idioma import Idioma

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



class Perfil_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("perfil.janela_titulo"))
        self.root.geometry("800x600")
        self.root.resizable(False, False)


    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = Idioma.t("perfil.titulo"),
            font = ("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            padx = 5,
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = Idioma.t("perfil.dados_frame")
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan=2,
            padx = 10,
            pady = 5,
            sticky = "ew"
        )
        self.frm_dados.grid_columnconfigure(0, weight=0)
        self.frm_dados.grid_columnconfigure(1, weight=1)
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
        self.lbl_descricao = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('perfil.descricao')}:"
        )
        self.lbl_descricao.grid(
            row = 2,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_descricao = tk.Text(
            self.frm_dados,
            width = 60,
            height = 3,
            wrap = "word",
            font = "TkTextFont"
        )
        self.txt_descricao.grid(
            row = 2,
            column = 1,
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
            row = 3,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 2,
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
        self.btn_fornecedores = tk.Button(
            self.frm_botoes,
            text = Idioma.t("perfil.fornecedores"),
            width = 15
        )
        self.btn_fornecedores.grid(
            row = 0,
            column = 4,
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
            column = 5,
            padx = 5,
            pady = 5
        )
        self.tbl_perfis = ttk.Treeview(
            self.root,
            height = 12
        )
        self.tbl_perfis.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )

    def configurar_treeview(self):
        self.tbl_perfis["columns"] = (
            "id",
            "nome",
            "descricao"
        )
        self.tbl_perfis.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_perfis.column(
            "id",
            width = 10,
            anchor = "center"
        )
        self.tbl_perfis.column(
            "nome",
            width = 40
        )
        self.tbl_perfis.column(
            "descricao",
            width = 60
        )
        self.tbl_perfis.heading(
            "id",
            text = Idioma.t("comum.id")
        )
        self.tbl_perfis.heading(
            "nome",
            text = Idioma.t("comum.nome")
        )
        self.tbl_perfis.heading(
            "descricao",
            text = Idioma.t("perfil.descricao")
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
        self.btn_fornecedores.config(
            command = self.controller.abrir_fornecedores
        )
        self.btn_fechar.config(
            command = self.fechar
        )
        self.tbl_perfis.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_perfil

        )
    def preencher_campos(self, perfil):

        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(perfil.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_nome.insert(
            0,
            perfil.nome
        )

        self.txt_descricao.insert(
            "1.0",
            perfil.descricao
        )

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome.delete(0, tk.END)
        self.txt_descricao.delete("1.0", tk.END)
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_perfis.get_children():
            self.tbl_perfis.delete(item)


    def get_id_selecionado(self):

        item = self.tbl_perfis.selection()[0]

        return self.tbl_perfis.item(item)["values"][0]

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            Idioma.t("comum.confirmacao"),
            Idioma.t("perfil.confirmar_exclusao"),
            parent=self.root
        )

    def ler_dados_perfil(self):
        nome = self.txt_nome.get()
        descricao = self.txt_descricao.get("1.0", tk.END).strip()
        return nome, descricao

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
    def exibir_perfis(self, perfis):

        self.limpar_treeview()

        for perfil in perfis:

            self.tbl_perfis.insert(
                "",
                tk.END,
                values=(
                    perfil.id,
                    perfil.nome,
                    perfil.descricao
                )
            )

    def abrir_fornecedores(self, perfil, fornecedores_disponiveis):
        janela_fornecedores = tk.Toplevel(self.root)
        Perfil_Fornecedor_View(
            janela_fornecedores,
            self.controller,
            perfil,
            fornecedores_disponiveis
        )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()