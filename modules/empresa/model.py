class Empresa:
    def __init__(self, cnpj, nome, inscricao_estadual, endereco, latitude, longitude):
        self.id = None
        self.cnpj = cnpj
        self.nome = nome
        self.inscricao_estadual = inscricao_estadual
        self.endereco = endereco
        self.latitude = latitude
        self.longitude = longitude

        def __str__(self):
            return self.id