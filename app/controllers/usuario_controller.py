from app.models.usuario import Usuario
from app.core.data_utils import Data_Utils
from app.core.senha_utils import Senha_Utils


class Usuario_Controller:

    def __init__(self, dao, cidade_dao, estado_dao, perfil_dao, view):
        self.dao = dao
        self.cidade_dao = cidade_dao
        self.estado_dao = estado_dao
        self.perfil_dao = perfil_dao
        self.view = view
        self.usuario_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def carregar_estados(self):
        estados = self.estado_dao.get_all()
        self.view.carregar_estados(estados)

    def carregar_perfis(self):
        perfis = self.perfil_dao.get_all()
        self.view.carregar_perfis(perfis)

    def carregar_cidades_do_estado_selecionado(self, event):
        id_estado = self.view.get_estado_selecionado_id()
        if id_estado is None:
            self.view.carregar_cidades([])
            return
        cidades = self.cidade_dao.get_by_estado(id_estado)
        self.view.carregar_cidades(cidades)

    def save(self):
        try:
            nome, email, data_nascimento, cidade, perfil, senha = self.view.ler_dados_usuario()
            if not senha:
                raise ValueError("Informe uma senha para o novo usuário.")
            usuario = Usuario(
                None,
                nome,
                email,
                Data_Utils.string_para_data(data_nascimento),
                cidade,
                perfil,
                Senha_Utils.gerar_hash(senha)
            )
            self.dao.save(usuario)
            self.get_all()
            self.view.exibir_mensagem("Usuário cadastrado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def get_all(self):
        usuarios = self.dao.get_all()
        self.view.exibir_usuarios(usuarios)

    def selecionar_usuario(self, event):
        try:
            id_usuario = self.view.get_id_selecionado()
            self.usuario_selecionado = self.dao.get_by_id(
                id_usuario
            )
            cidades = self.cidade_dao.get_by_estado(
                self.usuario_selecionado.cidade.estado.id
            )
            self.view.preencher_campos(
                self.usuario_selecionado,
                cidades
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.usuario_selecionado is None:
                self.view.exibir_mensagem("Selecione um usuário na lista.", False)
                return
            nome, email, data_nascimento, cidade, perfil, senha = self.view.ler_dados_usuario()
            self.usuario_selecionado.atualizar_dados(
                nome,
                email,
                Data_Utils.string_para_data(data_nascimento),
                cidade,
                perfil
            )
            if senha:
                self.usuario_selecionado.senha = Senha_Utils.gerar_hash(senha)
            self.dao.update(self.usuario_selecionado)
            self.get_all()
            self.view.exibir_mensagem("Usuário atualizado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.usuario_selecionado is None:
            self.view.exibir_mensagem("Selecione um usuário na lista.", False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.usuario_selecionado.id)
            if sucesso:
                self.usuario_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Usuário excluído com sucesso!")
            else:
                self.view.exibir_mensagem("Usuário não encontrado.", False)
        except Exception as e:
            self.view.exibir_mensagem("Problemas ao excluir usuário", False)
