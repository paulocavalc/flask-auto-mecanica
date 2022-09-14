class Funcionario:
    def __init__(self, codigo, nome, especialidade, cpf, rg, telefone, data_adimissao, salario, foto):
        self.id = None
        self.codigo = codigo
        self.nome = nome
        self.especialidade = especialidade
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.data_adimissao = data_adimissao
        self.salario = salario
        self.foto = foto

        def __str__(self):
            return self.id