class Cliente:
    def __init__(self, cpf_cnpj, nome, endereco, rg, telefone, placa_carro, tipo, latitude, longitude):
        self.id = None
        self.cpf_cnpj = cpf_cnpj
        self.nome = nome
        self.endereco = endereco
        self.rg = rg
        self.telefone = telefone
        self.placa_carro = placa_carro
        self.tipo = tipo
        self.latitude = latitude
        self.longitude = longitude

        def __str__(self):
            return self.id