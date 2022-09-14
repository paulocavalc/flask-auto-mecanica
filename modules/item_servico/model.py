class ItemServico:
    def __init__(self, codigo, descricao, valor_item, codigo_servico):
        self.id = None
        self.codigo = codigo
        self.descricao = descricao
        self.valor_item = valor_item
        self.codigo_servico = codigo_servico

        def __str__(self):
            return self.id