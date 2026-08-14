class Estado:

    def __init__(self, id, nome, sigla):
        self._id = id
        self._nome = nome
        self._sigla = sigla

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
    def sigla(self):
        return self._sigla.upper()

    @sigla.setter
    def sigla(self, nova_sigla):
        self._sigla = nova_sigla

    def atualizar_dados(self, novo_nome, nova_sigla):

        if len(nova_sigla) != 2:
            raise ValueError("estado.erro_sigla_tamanho")

        self._nome = novo_nome
        self._sigla = nova_sigla.upper()
        