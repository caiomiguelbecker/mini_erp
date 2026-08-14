from app.models.fornecedor import Fornecedor
class Produto:
    def __init__(self, id, nome, estoque, preco, fornecedor:Fornecedor):
        self._id = id
        self._nome = nome  
        self._estoque = estoque
        self._preco = preco
        self._fornecedor = fornecedor

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
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, novo_estoque):
        self._estoque = novo_estoque

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco

    @property
    def valor_estoque(self):
        return self._preco * self._estoque
    
    @property
    def fornecedor(self):
        return self._fornecedor
    
    @fornecedor.setter
    def fornecedor(self, novo_fornecedor):
        self._fornecedor = novo_fornecedor
    

    def atualizar_dados(self, novo_nome, novo_estoque, novo_preco, novo_fornecedor):
        if novo_preco < 0:
            raise ValueError("produto.erro_preco")
        if novo_estoque < 0:
            raise ValueError("produto.erro_estoque")
        self._nome = novo_nome
        self._estoque = novo_estoque
        self._preco = novo_preco
        self._fornecedor = novo_fornecedor
            

