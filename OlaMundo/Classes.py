class ContaBancaria:
    def __init__(self, tipo, conta, agencia):
        self.tipo = tipo
        self.conta = conta
        self.agencia = agencia

    def ExibirDadosConta(self):
        print(f"Informações da Conta criada: Tipo: {self.tipo} - Conta: {self.conta} - Agência: {self.agencia}")

if __name__ == '__main__':
    conta1 = ContaBancaria("corrente", 10534, '0001')
    print(f"Conta 1 criada: Tipo: {conta1.tipo} - Conta: {conta1.conta} - Agência: {conta1.agencia}")
    conta1.ExibirDadosConta()

    conta2 = ContaBancaria("poupança", 56420, '4451')
    print(f"Conta 2 criada: Tipo: {conta2.tipo} - Conta: {conta2.conta} - Agência: {conta2.agencia}")
    conta2.ExibirDadosConta()
