class Carro:
    def __init__(self, placa_carro, modelo, marca):
        self.id = None
        self.placa_carro = placa_carro
        self.modelo = modelo
        self.marca = marca

        def __str__(self):
            return self.id