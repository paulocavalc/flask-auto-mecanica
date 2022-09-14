class OrdemServico:
    def __init__(self, codigo, entrada, saida, codigo_funcionario, placa_carro, cpf_cnpj_cliente):
        self.id = None
        self.codigo = codigo
        self.entrada = entrada
        self.saida = saida
        self.codigo_funcionario = codigo_funcionario
        self.placa_carro = placa_carro
        self.cpf_cpnj_cliente = cpf_cnpj_cliente

        def __str__(self):
            return self.id