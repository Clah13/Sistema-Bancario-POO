# Etapa 1:

class ContaBancaria:
    """Representa uma conta bancária com saldo e histórico de transações."""

    # Método Construtor que define os atributos dos objetos a serem criados (instanciados)
    def __init__(self, numero_conta, saldo_inicial = 0.0, extrato_inicial = None):

        self.saldo = saldo_inicial
        self._numero_conta = numero_conta
        self.extrato = extrato_inicial if extrato_inicial is not None else []

# Exemplo de como a classe é utilizada

# Criando uma conta bancária

minha_conta = ContaBancaria(numero_conta = "12345-X", saldo_inicial = 1000.0)
print(f"Conta criada: {minha_conta._numero_conta}, Saldo inicial: R$ {minha_conta.saldo:.2f}")

# Criando outra conta para demonstrar a independência

conta_joao = ContaBancaria(numero_conta = "67890-Y")
print(f"Conta de João: {conta_joao._numero_conta}, Saldo inicial: R${conta_joao.saldo:.2f}")

# O extrato é uma lista vazia no início
print(f"Extrato da minha conta: {minha_conta.extrato}")