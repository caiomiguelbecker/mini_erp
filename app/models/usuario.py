from app.models.cidade import Cidade
from app.models.perfil import Perfil
from app.core.data_utils import Data_Utils


class Usuario:

    def __init__(
        self,
        id,
        nome,
        email,
        data_nascimento,
        cidade: Cidade,
        perfil: Perfil,
        senha
    ):
        self._id = id
        self._nome = nome
        self._email = email
        self._data_nascimento = data_nascimento
        self._cidade = cidade
        self._perfil = perfil
        self._senha = senha

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def nome(self):
        return self._nome.upper()

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        self._data_nascimento = nova_data

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, nova_cidade):
        self._cidade = nova_cidade

    @property
    def perfil(self):
        return self._perfil

    @perfil.setter
    def perfil(self, novo_perfil):
        self._perfil = novo_perfil

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    @property
    def idade(self):
        return Data_Utils.calcular_idade(self._data_nascimento)

    def atualizar_dados(
        self,
        novo_nome,
        novo_email,
        nova_data_nascimento,
        nova_cidade,
        novo_perfil
    ):
        self._nome = novo_nome
        self._email = novo_email
        self._data_nascimento = nova_data_nascimento
        self._cidade = nova_cidade
        self._perfil = novo_perfil