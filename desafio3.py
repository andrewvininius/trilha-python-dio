import datetime

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, endereco, cpf, data_nascimento):
        super().__init__(nome, endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, agencia, cliente):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0.0
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.adicionar_transacao(f"Depósito: {valor}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque: {valor}")
            return True
        return False

    def obter_saldo(self):
        return self.saldo

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = 3  # Número de saques permitidos por dia

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            super().sacar(valor)
            return True
        return False

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, descricao):
        data_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transacoes.append(f"{data_atual} - {descricao}")

class Transacao:
    def registrar(self, conta: 'Conta'):
        raise NotImplementedError("Esta é uma interface!")

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta: 'Conta'):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta: 'Conta'):
        conta.sacar(self.valor)

# Exemplo de uso:
cliente = PessoaFisica("João Silva", "Rua das Flores, 123", "12345678901", "1980-05-15")
conta = ContaCorrente(101, "001", cliente, 500)
conta.depositar(1000)
print(conta.obter_saldo())  # Saída: 1000.0

saque = Saque(200)
saque.registrar(conta)
print(conta.obter_saldo())  # Saída: 800.0

# Exibindo histórico:
for transacao in conta.historico.transacoes:
    print(transacao)
