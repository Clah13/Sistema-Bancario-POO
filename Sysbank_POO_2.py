import datetime # Necessário para registrar a data e hora das transações

# Etapa 2:

class ContaBancaria:
    """Representa uma conta bancária com saldo e histórico de transações."""

    #Método construtor
    def __init__(self, numero_conta, saldo_inicial= 0.0, extrato_inicial = None):

        self.saldo = saldo_inicial
        self._numero_conta = numero_conta
        self.extrato = extrato_inicial if extrato_inicial is not None else []

    def consultar_saldo(self):
        """Exibe o saldo atual da conta."""

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Seu saldo atual é: R$ {self.saldo:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def depositar(self, valor):
        """Realiza uma operação de depósito na conta"""

        try:
            valor_deposito = float(valor)
            if valor_deposito <= 0:
                print("Valor de depósito inválido. Digite um número positivo.")
                return
            self.saldo += valor_deposito # Atualiza o saldo (somando o valor do depósito)

            # Registra a transação no extrato
            agora = datetime.datetime.now()
            self.extrato.append({
                    "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                    "tipo":"Depósito",
                    "valor": valor_deposito
                                })
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
            print(f"Seu novo saldo é: R$ {self.saldo:.2f}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        except ValueError:
            print("Valor inválido para depósito. Por favor, digite um número.")

    def sacar(self, valor):
        """Realiza uma operação de saque na conta, verificando o saldo."""
        try:
            valor_saque = float(valor)
            if valor_saque <= 0:

                print("Valor de saque inválido. Digite um número positivo.")
                return

            if valor_saque <= self.saldo: #Verifica se o saldo é suficiente
                self.saldo -= valor_saque #Atualiza o saldo

                #Registra a transação no extrato
                agora = datetime.datetime.now()
                self.extrato.append({
                    "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                    "tipo":"Saque",
                    "valor": valor_saque
                })

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
                print(f"Seu novo saldo é: R$ {self.saldo:.2f}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            else:
                print("Saldo insuficiente.")

        except ValueError:
            print("Valor inválido para saque. Por favor, digite um número.")

# Exemplo de uso da classe (para testar os métodos):

if __name__ == "__main__":

    # Criando uma conta bancária de exemplo
    minha_conta = ContaBancaria(numero_conta = "98765-4", saldo_inicial = 500.0)
    print(f"Conta {minha_conta._numero_conta} criada com saldo: R$ {minha_conta.saldo:.2f}")

    print("\n --- Testando operações ---")

    minha_conta.consultar_saldo() #Exibe o saldo atual da conta.

    minha_conta.depositar(200) # Permite ao usuário depositar um valor na conta.
    minha_conta.consultar_saldo()  # Exibe o saldo atual da conta.

    minha_conta.sacar(150) # Permite ao usuário sacar um valor da conta, verificando se há saldo suficiente.
    minha_conta.consultar_saldo() #Exibe o saldo atual da conta.

    minha_conta.depositar("abc") # Teste de entrada inválida para depósito.
    minha_conta.sacar("xyz") # Teste de entrada inválida para saque.