class Fornecedor:
    def __init__(self, id, razao_social, nome_fantasia, cnpj, sla_atendimento, categorias=None):
        self._id = id
        self._razao_social = razao_social
        self._nome_fantasia = nome_fantasia
        self._cnpj = cnpj
        self._sla_atendimento = sla_atendimento
        self._categorias = categorias if categorias is not None else []

    def validar_sla(self, sla):
        if sla < 0:
            raise ValueError("fornecedor.sla_erro_negativo")

    # Encapsulamento do ID
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    # Encapsulamento da Razão Social
    @property
    def razao_social(self):
        return self._razao_social
    
    @razao_social.setter
    def razao_social(self, nova_razao):
        self._razao_social = nova_razao

    # Encapsulamento do Nome Fantasia
    @property
    def nome_fantasia(self):
        return self._nome_fantasia
    
    @nome_fantasia.setter
    def nome_fantasia(self, novo_nome):
        self._nome_fantasia = novo_nome

    # Encapsulamento do CNPJ
    @property
    def cnpj(self):
        return self._cnpj
    
    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj

    # Encapsulamento do SLA de Atendimento
    @property
    def sla_atendimento(self):
        return self._sla_atendimento
    
    @sla_atendimento.setter
    def sla_atendimento(self, novo_sla):
        self._sla_atendimento = novo_sla

    # Encapsulamento das Categorias
    @property
    def categorias(self):
        return self._categorias

    @categorias.setter
    def categorias(self, novas_categorias):
        self._categorias = novas_categorias

    def atualizar_dados(self, nova_razao_social, novo_nome_fantasia, novo_cnpj, novo_sla):
        self.validar_sla(novo_sla)
        self._razao_social = nova_razao_social
        self._nome_fantasia = novo_nome_fantasia
        self._cnpj = novo_cnpj
        self._sla_atendimento = novo_sla
