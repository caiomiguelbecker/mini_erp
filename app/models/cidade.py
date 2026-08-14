from app.models.estado import Estado


class Cidade:

    def __init__(self, id, nome, estado: Estado):
        self._id = id
        self.nome = nome
        self._estado = estado

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
        if not novo_nome or not novo_nome.strip():
            raise ValueError("cidade.erro_nome_vazio")
        self._nome = novo_nome

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, novo_estado):
        self._estado = novo_estado

    def atualizar_dados(
        self,
        novo_nome,
        novo_estado
    ):

        self.nome = novo_nome
        self._estado = novo_estado