from app.models.perfil import Perfil
from app.core.idioma import Idioma


class Perfil_Controller:
    def __init__(self, dao, fornecedor_dao, perfil_fornecedor_dao, view):
        self.dao = dao
        self.fornecedor_dao = fornecedor_dao
        self.perfil_fornecedor_dao = perfil_fornecedor_dao
        self.view = view
        self.perfil_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome, descricao = self.view.ler_dados_perfil()
            perfil = Perfil(
                None,
                nome,
                descricao
            )
            self.dao.save(perfil)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("perfil.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        perfis = self.dao.get_all()
        self.view.exibir_perfis(perfis)

    def selecionar_perfil(self, event):
        try:
            id_perfil = self.view.get_id_selecionado()
            self.perfil_selecionado = self.dao.get_by_id(
                id_perfil
            )
            self.view.preencher_campos(
                self.perfil_selecionado
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.perfil_selecionado is None:
                self.view.exibir_mensagem(Idioma.t("perfil.selecione_da_lista"), False)
                return
            nome, descricao = self.view.ler_dados_perfil()
            self.perfil_selecionado.atualizar_dados(nome, descricao)
            self.dao.update(self.perfil_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("perfil.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.perfil_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("perfil.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.perfil_selecionado.id)
            if sucesso:
                self.perfil_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("perfil.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("perfil.nao_encontrado"), False)
        except Exception as e:
            self.view.exibir_mensagem(Idioma.t("perfil.erro_ao_excluir"), False)

    def abrir_fornecedores(self):
        if self.perfil_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("perfil.selecione_da_lista"), False)
            return
        fornecedores_disponiveis = self.fornecedor_dao.get_all()
        if not fornecedores_disponiveis:
            self.view.exibir_mensagem(Idioma.t("perfil.sem_fornecedores"), False)
            return
        self.perfil_selecionado.fornecedores = self.perfil_fornecedor_dao.get_fornecedores_por_perfil(
            self.perfil_selecionado
        )
        self.view.abrir_fornecedores(
            self.perfil_selecionado,
            fornecedores_disponiveis
        )

    def salvar_fornecedores(self, view_fornecedores, perfil, fornecedores_selecionados):
        try:
            self.perfil_fornecedor_dao.substituir_fornecedores_do_perfil(
                perfil,
                fornecedores_selecionados
            )
            perfil.fornecedores = self.perfil_fornecedor_dao.get_fornecedores_por_perfil(
                perfil
            )
            view_fornecedores.exibir_mensagem(Idioma.t("perfil.fornecedores_atualizados_sucesso"))
            view_fornecedores.fechar()
        except Exception as e:
            view_fornecedores.exibir_mensagem(Idioma.t("perfil.erro_salvar_fornecedores"), False)