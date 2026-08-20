from app.models.cliente import Cliente
from app.core.data_utils import Data_Utils
from app.core.idioma import Idioma

class Cliente_Controller:

    def __init__(
        self,
        dao,
        cidade_dao,
        estado_dao,
        view
    ):
        self.dao = dao
        self.cidade_dao = cidade_dao
        self.estado_dao = estado_dao
        self.view = view
        self.cliente_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def carregar_estados(self):
        estados = self.estado_dao.get_all()
        self.view.carregar_estados(estados)

    def carregar_cidades_do_estado_selecionado(self, event):
        id_estado = self.view.get_estado_selecionado_id()
        if id_estado is None:
            self.view.carregar_cidades([])
            return
        cidades = self.cidade_dao.get_by_estado(id_estado)
        self.view.carregar_cidades(cidades)

    def save(self):
        try:
            nome, data_nascimento, limite_credito, cidade = self.view.ler_dados_cliente()
            cliente = Cliente(
                None,
                nome,
                Data_Utils.string_para_data(data_nascimento),
                limite_credito,
                cidade
            )
            self.dao.save(cliente)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("cliente.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        clientes = self.dao.get_all()
        self.view.exibir_clientes(clientes)

    def selecionar_cliente(self, event):
        try:
            id_cliente = self.view.get_id_selecionado()
            self.cliente_selecionado = self.dao.get_by_id(
                id_cliente
            )
            cidades = self.cidade_dao.get_by_estado(
                self.cliente_selecionado.cidade.estado.id
            )
            self.view.preencher_campos(
                self.cliente_selecionado,
                cidades
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.cliente_selecionado is None:
                self.view.exibir_mensagem(Idioma.t("cliente.selecione_da_lista"), False)
                return
            nome, data_nascimento, limite_credito, cidade = self.view.ler_dados_cliente()
            self.cliente_selecionado.atualizar_dados(
                nome,
                Data_Utils.string_para_data(data_nascimento),
                limite_credito,
                cidade
            )
            self.dao.update(self.cliente_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("cliente.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.cliente_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("cliente.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.cliente_selecionado.id)
            if sucesso:
                self.cliente_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("cliente.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("cliente.nao_encontrado"), False)
        except Exception as e:
            self.view.exibir_mensagem(Idioma.t("cliente.erro_ao_excluir"), False)