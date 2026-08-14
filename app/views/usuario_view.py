from app.models.usuario import Usuario
from app.core.data_utils import Data_Utils
from app.core.idioma import Idioma

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



class Usuario_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._estados = []
        self._cidades = []
        self._perfis = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("usuario.janela_titulo"))
        self.root.geometry("900x600")
        self.root.resizable(False, False)


    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = Idioma.t("usuario.titulo"),
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
            text = Idioma.t("usuario.dados_frame")
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
            text = f"{Idioma.t('usuario.nome')}:"
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
        self.lbl_email = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('usuario.email')}:"
        )
        self.lbl_email.grid(
            row = 1,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_email = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_email.grid(
            row = 1,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_data_nascimento = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('usuario.nascimento')} (DD/MM/AAAA):"
        )
        self.lbl_data_nascimento.grid(
            row = 2,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_data_nascimento = tk.Entry(
            self.frm_dados,
            width = 20
        )
        self.txt_data_nascimento.grid(
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
            text = f"{Idioma.t('usuario.cidade')}:"
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
        self.lbl_perfis = tk.Label(
            self.frm_dados,
            text = f"{Idioma.t('usuario.perfil')}:"
        )
        self.lbl_perfis.grid(
            row = 3,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.cmb_perfis = ttk.Combobox(
            self.frm_dados,
            width = 37,
            state = "readonly"
        )
        self.cmb_perfis.grid(
            row = 3,
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
        self.tbl_usuarios = ttk.Treeview(
            self.root,
            height = 10
        )
        self.tbl_usuarios.grid(
            row = 5,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )

    def configurar_treeview(self):
        self.tbl_usuarios["columns"] = (
            "id",
            "nome",
            "email",
            "nascimento",
            "idade",
            "cidade",
            "estado",
            "perfil"
        )
        self.tbl_usuarios.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_usuarios.column(
            "id",
            width = 10,
            anchor = "center"
        )
        self.tbl_usuarios.column(
            "nome",
            width = 40
        )
        self.tbl_usuarios.column(
            "email",
            width = 50
        )
        self.tbl_usuarios.column(
            "nascimento",
            width = 20,
            anchor = "center"
        )
        self.tbl_usuarios.column(
            "idade",
            width = 15,
            anchor = "center"
        )
        self.tbl_usuarios.column(
            "cidade",
            width = 30
        )
        self.tbl_usuarios.column(
            "estado",
            width = 15,
            anchor = "center"
        )
        self.tbl_usuarios.column(
            "perfil",
            width = 30
        )
        self.tbl_usuarios.heading(
            "id",
            text = Idioma.t("comum.id")
        )
        self.tbl_usuarios.heading(
            "nome",
            text = Idioma.t("usuario.nome")
        )
        self.tbl_usuarios.heading(
            "email",
            text = Idioma.t("usuario.email")
        )
        self.tbl_usuarios.heading(
            "nascimento",
            text = Idioma.t("usuario.nascimento")
        )
        self.tbl_usuarios.heading(
            "idade",
            text = Idioma.t("usuario.idade")
        )
        self.tbl_usuarios.heading(
            "cidade",
            text = Idioma.t("usuario.cidade")
        )
        self.tbl_usuarios.heading(
            "estado",
            text = Idioma.t("usuario.uf")
        )
        self.tbl_usuarios.heading(
            "perfil",
            text = Idioma.t("usuario.perfil")
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
        self.tbl_usuarios.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_usuario
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

    def carregar_perfis(self, perfis):
        self._perfis = perfis
        valores = []
        for perfil in perfis:
            valores.append(
                f"{perfil.id} - {perfil.nome}"
            )
        self.cmb_perfis["values"] = valores
        self.cmb_perfis.set("")

    def get_estado_selecionado_id(self):
        indice = self.cmb_estados.current()
        if indice < 0:
            return None
        return self._estados[indice].id

    def preencher_campos(self, usuario, cidades):

        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(usuario.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_nome.insert(
            0,
            usuario.nome
        )

        self.txt_email.insert(
            0,
            usuario.email
        )

        self.txt_data_nascimento.insert(
            0,
            Data_Utils.data_para_string(usuario.data_nascimento)
        )

        for indice, estado in enumerate(self._estados):
            if estado.id == usuario.cidade.estado.id:
                self.cmb_estados.current(indice)
                break

        self.carregar_cidades(cidades)

        for indice, cidade in enumerate(self._cidades):
            if cidade.id == usuario.cidade.id:
                self.cmb_cidades.current(indice)
                break

        for indice, perfil in enumerate(self._perfis):
            if perfil.id == usuario.perfil.id:
                self.cmb_perfis.current(indice)
                break

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.txt_data_nascimento.delete(0, tk.END)
        self.cmb_estados.set("")
        self.cmb_cidades.set("")
        self.cmb_cidades["values"] = []
        self._cidades = []
        self.cmb_perfis.set("")
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_usuarios.get_children():
            self.tbl_usuarios.delete(item)


    def get_id_selecionado(self):

        item = self.tbl_usuarios.selection()[0]

        return self.tbl_usuarios.item(item)["values"][0]

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            Idioma.t("comum.confirmacao"),
            Idioma.t("usuario.confirmar_exclusao"),
            parent=self.root
        )

    def ler_dados_usuario(self):
        nome = self.txt_nome.get()
        email = self.txt_email.get()
        data_nascimento = self.txt_data_nascimento.get()
        if not Data_Utils.validar_data(data_nascimento):
            raise ValueError("usuario.erro_data_invalida")
        indice_cidade = self.cmb_cidades.current()
        if indice_cidade < 0:
            raise ValueError("usuario.erro_cidade_nao_selecionado")
        cidade = self._cidades[indice_cidade]
        indice_perfil = self.cmb_perfis.current()
        if indice_perfil < 0:
            raise ValueError("usuario.erro_perfil_nao_selecionado")
        perfil = self._perfis[indice_perfil]
        return nome, email, data_nascimento, cidade, perfil

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
    def exibir_usuarios(self, usuarios):

        self.limpar_treeview()

        for usuario in usuarios:

            self.tbl_usuarios.insert(
                "",
                tk.END,
                values=(
                    usuario.id,
                    usuario.nome,
                    usuario.email,
                    Data_Utils.data_para_string(usuario.data_nascimento),
                    usuario.idade,
                    usuario.cidade.nome,
                    usuario.cidade.estado.sigla,
                    usuario.perfil.nome
                )
            )
    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_estados()
        self.controller.carregar_perfis()
        self.controller.get_all()