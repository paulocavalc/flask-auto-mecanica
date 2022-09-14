class Servico:
    def __init__(self, codigo, descricao, valor_servico):
        self.id = None
        self.codigo = codigo
        self.descricao = descricao
        self.valor_servico = valor_servico

        def __str__(self):
            return self.id