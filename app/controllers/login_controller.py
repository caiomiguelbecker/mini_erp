from app.core.senha_utils import Senha_Utils
from app.core.idioma import Idioma


class Login_Controller:
    def __init__(self, usuario_dao, view, ao_autenticar):
        self.usuario_dao = usuario_dao
        self.view = view
        self.ao_autenticar = ao_autenticar

    def autenticar(self):
        email, senha = self.view.ler_dados_login()

        if not email or not senha:
            self.view.exibir_mensagem(Idioma.t("login.campos_obrigatorios"), False)
            return

        usuario = self.usuario_dao.get_by_email(email)

        if usuario is None or not Senha_Utils.verificar_senha(senha, usuario.senha):
            self.view.exibir_mensagem(Idioma.t("login.credenciais_invalidas"), False)
            return

        self.ao_autenticar(usuario)