class NotaFiscalServico:
    def __init__(self, codigo, cnpj_empresa, cpf_cnpj_cliente, codigo_ordem_servico, total, forma_pagamento):
        self.id = None
        self.codigo = codigo
        self.cnpj_empresa = cnpj_empresa
        self.cpf_cpnj_cliente = cpf_cnpj_cliente
        self.codigo_ordem_servico = codigo_ordem_servico
        self.total = total
        self.forma_pagamento = forma_pagamento

        def __str__(self):
            return self.id