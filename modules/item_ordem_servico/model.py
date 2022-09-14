class ItemOrdemServico:
    def __init__(self, codigo, codigo_item_servico, codigo_funcionario, codigo_ordem_servico):
        self.id = None
        self.codigo = codigo
        self.codigo_item_servico = codigo_item_servico
        self.codigo_funcionario = codigo_funcionario
        self.codigo_ordem_servico = codigo_ordem_servico

        def __str__(self):
            return self.id