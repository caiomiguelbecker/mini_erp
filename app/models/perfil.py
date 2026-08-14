class Perfil:

    def __init__(self, id, nome, descricao, fornecedores=None):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._fornecedores = fornecedores if fornecedores is not None else []

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
            raise ValueError("perfil.erro_nome_vazio")
        self._nome = novo_nome

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if not nova_descricao or not nova_descricao.strip():
            raise ValueError("perfil.erro_descricao_vazio")
        self._descricao = nova_descricao

    @property
    def fornecedores(self):
        return self._fornecedores

    @fornecedores.setter
    def fornecedores(self, novos_fornecedores):
        self._fornecedores = novos_fornecedores

    def atualizar_dados(self, novo_nome, nova_descricao):
        self._nome = novo_nome
        self._descricao = nova_descricao
