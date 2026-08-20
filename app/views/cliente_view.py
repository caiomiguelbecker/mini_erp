

from app.models.cliente import Cliente
from app.core.data_utils import Data_Utils
from app.core.idioma import Idioma

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



class Cliente_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._estados = []
        self._cidades = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("cliente.janela_titulo"))
        self.root.geometry("900x600")
        self.root.resizable(False, False)


    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = Idioma.t("cliente.titulo"),
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
            text = Idioma.t("cliente.dados_frame")
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
        self.lbl_data_nascimento = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('cliente.nascimento')} (DD/MM/AAAA):"
        )
        self.lbl_data_nascimento.grid(
            row = 1,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_data_nascimento = tk.Entry(
            self.frm_dados,
            width = 20
        )
        self.txt_data_nascimento.grid(
            row = 1,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_limite_credito = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('cliente.limite_credito')}:"
        )
        self.lbl_limite_credito.grid(
            row = 2,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_limite_credito = tk.Entry(
            self.frm_dados,
            width = 20
        )
        self.txt_limite_credito.grid(
            row = 2,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_estados = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('cidade.estado')}:"
        )
        self.lbl_estados.grid(
            row = 2,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.cmb_estados = ttk.Combobox(
            self.frm_dados,
            width = 37,
            state = "readonly"
        )
        self.cmb_estados.grid(
            row = 2,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_cidades = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('cliente.cidade')}:"
        )
        self.lbl_cidades.grid(
            row = 3,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.cmb_cidades = ttk.Combobox(
            self.frm_dados,
            width = 37,
            state = "readonly"
        )
        self.cmb_cidades.grid(
            row = 3,
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
        self.tbl_clientes = ttk.Treeview(
            self.root,
            height = 10
        )
        self.tbl_clientes.grid(
            row = 5,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )

    def configurar_treeview(self):
        self.tbl_clientes["columns"] = (
            "id",
            "nome",
            "nascimento",
            "idade",
            "limite",
            "cidade",
            "estado"
        )
        self.tbl_clientes.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_clientes.column(
            "id",
            width = 10,
            anchor = "center"
        )
        self.tbl_clientes.column(
            "nome",
            width = 40
        )
        self.tbl_clientes.column(
            "nascimento",
            width = 20,
            anchor = "center"
        )
        self.tbl_clientes.column(
            "idade",
            width = 15,
            anchor = "center"
        )
        self.tbl_clientes.column(
            "limite",
            width = 20,
            anchor = "e"
        )
        self.tbl_clientes.column(
            "cidade",
            width = 30
        )
        self.tbl_clientes.column(
            "estado",
            width = 15,
            anchor = "center"
        )
        self.tbl_clientes.heading(
            "id",
            text = Idioma.t("comum.id")
        )
        self.tbl_clientes.heading(
            "nome",
            text = Idioma.t("comum.nome")
        )
        self.tbl_clientes.heading(
            "nascimento",
            text = Idioma.t("cliente.nascimento")
        )
        self.tbl_clientes.heading(
            "idade",
            text = Idioma.t("cliente.idade")
        )
        self.tbl_clientes.heading(
            "limite",
            text = Idioma.t("cliente.limite_credito")
        )
        self.tbl_clientes.heading(
            "cidade",
            text = Idioma.t("cliente.cidade")
        )
        self.tbl_clientes.heading(
            "estado",
            text = Idioma.t("cliente.uf")
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
        self.tbl_clientes.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_cliente
        )
        self.cmb_estados.bind(
            "<<ComboboxSelected>>",
            self.controller.carregar_cidades_do_estado_selecionado
        )
    def carregar_estados(self, estados):
        self._estados = estados
        valores = []
        for estado in estados:
            valores.append(
                f"{estado.id} - {estado.nome}"
            )
        self.cmb_estados["values"] = valores
        self.cmb_estados.set("")

    def carregar_cidades(self, cidades):
        self._cidades = cidades
        valores = []
        for cidade in cidades:
            valores.append(
                f"{cidade.id} - {cidade.nome}"
            )
        self.cmb_cidades["values"] = valores
        self.cmb_cidades.set("")

    def get_estado_selecionado_id(self):
        indice = self.cmb_estados.current()
        if indice < 0:
            return None
        return self._estados[indice].id

    def preencher_campos(self, cliente, cidades):

        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(cliente.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_nome.insert(
            0,
            cliente.nome
        )

        self.txt_data_nascimento.insert(
            0,
            Data_Utils.data_para_string(cliente.data_nascimento)
        )

        self.txt_limite_credito.insert(
            0,
            str(cliente.limite_credito)
        )

        for indice, estado in enumerate(self._estados):
            if estado.id == cliente.cidade.estado.id:
                self.cmb_estados.current(indice)
                break

        self.carregar_cidades(cidades)

        for indice, cidade in enumerate(self._cidades):
            if cidade.id == cliente.cidade.id:
                self.cmb_cidades.current(indice)
                break

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome.delete(0, tk.END)
        self.txt_data_nascimento.delete(0, tk.END)
        self.txt_limite_credito.delete(0, tk.END)
        self.cmb_estados.set("")
        self.cmb_cidades.set("")
        self.cmb_cidades["values"] = []
        self._cidades = []
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_clientes.get_children():
            self.tbl_clientes.delete(item)


    def get_id_selecionado(self):

        item = self.tbl_clientes.selection()[0]

        return self.tbl_clientes.item(item)["values"][0]

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            Idioma.t("comum.confirmacao"),
            Idioma.t("cliente.confirmar_exclusao"),
            parent=self.root
        )

    def ler_dados_cliente(self):
        nome = self.txt_nome.get()
        data_nascimento = self.txt_data_nascimento.get()
        if not Data_Utils.validar_data(data_nascimento):
            raise ValueError("cliente.erro_data_invalida")
        limite_credito = float(self.txt_limite_credito.get())
        indice = self.cmb_cidades.current()
        if indice < 0:
            raise ValueError("cliente.erro_cidade_nao_selecionado")
        cidade = self._cidades[indice]
        return nome, data_nascimento, limite_credito, cidade

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
    def exibir_clientes(self, clientes):

        self.limpar_treeview()

        for cliente in clientes:

            self.tbl_clientes.insert(
                "",
                tk.END,
                values=(
                    cliente.id,
                    cliente.nome,
                    Data_Utils.data_para_string(cliente.data_nascimento),
                    cliente.idade,
                    f"{cliente.limite_credito:.2f}",
                    cliente.cidade.nome,
                    cliente.cidade.estado.sigla
                )
            )
    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_estados()
        self.controller.get_all()