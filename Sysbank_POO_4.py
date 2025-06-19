# Etapa 4:

import datetime  # Necessário para registrar a data e hora das transações
import json

class ContaBancaria:
    """Representa uma conta bancária com saldo e histórico de transações."""

    # Método construtor
    def __init__(self, numero_conta, saldo_inicial=0.0, extrato_inicial=None):

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
            self.saldo += valor_deposito  # Atualiza o saldo (somando o valor do depósito)

            # Registra a transação no extrato
            agora = datetime.datetime.now()
            self.extrato.append({
                "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                "tipo": "Depósito",
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

            if valor_saque <= self.saldo:  # Verifica se o saldo é suficiente
                self.saldo -= valor_saque  # Atualiza o saldo

                # Registra a transação no extrato
                agora = datetime.datetime.now()
                self.extrato.append({
                    "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                    "tipo": "Saque",
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

    def exibir_extrato(self):
        """Exibe o histórico detalhado de transações da conta."""

        if not self.extrato:  # Verifica se o extrato está vazio
            print("Não foram realizadas transações.")

        else:

            print("\n --- Extrato Bancário ---")
            for transacao in self.extrato:  # Iterar sobre a lista extrato e exiba cada transação formatada.
                data_hora = transacao["data_hora"]
                tipo = transacao["tipo"]
                valor = transacao["valor"]
                print(f"{data_hora} - {tipo}: R$ {valor:.2f}")

            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"Saldo atual: R$ {self.saldo:.2f}")  # Exibir o saldo atual da conta.
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def transferir(self, conta_destino, valor):
        """Realiza uma transferência de valor para outra conta bancária."""

        try:
            valor_transferencia = float(
                valor)  # O sistema deverá pedir o número da conta de destino e depois o valor a ser transferido.

            if valor_transferencia <= 0:
                print("Valor de transferência inválido. Digite um número positivo.")
                return

            if not isinstance(conta_destino, ContaBancaria):  # Verificar se existe a conta de destino
                print("Erro: A conta de destino não é válida de ContaBancaria.")
                return

            if valor_transferencia <= self.saldo:  # Verificar se há saldo suficiente na conta de origem
                self.saldo -= valor_transferencia  # O valor deve ser subtraído do saldo.

                # Registrar a transação na conta de origem
                agora = datetime.datetime.now()

                self.extrato.append({
                    "data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"),
                    "tipo": f"Transferencia para {conta_destino._numero_conta}",
                    "valor": valor_transferencia
                })

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Transferência de R$ {valor_transferencia:.2f} para conta {conta_destino._numero_conta} realizada com sucesso.")
                print(f"Seu novo saldo é: R$ {self.saldo:.2f}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                # Chamar o método depositar da conta_destino
                conta_destino.depositar(
                    valor_transferencia)  # Chama o método depositar() da conta destino para adicionar o valor.

            else:
                print("Saldo insuficiente para realizar a transferência.")

        except ValueError:
            print("Valor inválido para transferência. Por favor, digite um número.")

def salvar_dados(conta, filename="banco_dados.json"):
    """Salva o saldo e o extrato de uma conta em um arquivo JSON"""

    dados = {
        "numero_conta": conta._numero_conta,  # Incluir o número da conta para recriar o objeto
        "saldo": conta.saldo,
        "extrato": conta.extrato

    }
    with open(filename, "w") as f:  # Abre o arquivo "banco_dados.json" em modo de escrita ("w")

        # Salva o saldo e o extrato no arquivo usando json.dump()
        json.dump(dados, f, indent=4)  # O 'indent 4' é para formatar o JSON de forma legível

    print(f"Dados da cona '{conta._numero_conta}' salvos com sucesso!")

def carregar_dados(filename = "banco_dados.json"):
    """Carrega o saldo e o extrato de uma conta a partir de um arquivo JSON. """

    try: # Tentar abrir um arquivo chamado "banco_dados.json" em modo de leitura ("r").
        with open(filename, "r") as f:
            dados = json.load(f) # Se o arquivo existir, carregar o saldo e o extrato de lá.

            # Retorna uma nova instância de ContaBancaria com os dados carregados
            return ContaBancaria(
                dados["numero_conta"],
                dados["saldo"],
                dados["extrato"])

    except FileNotFoundError:

        print("Arquivo de dados não encontrado. Criando uma nova conta com número padrão '00000-0'.")
        return ContaBancaria("00000-0")


# Exemplo de uso da classe (para testar os métodos):

if __name__ == "__main__":
    # Criando uma conta bancária de exemplo
    minha_conta = ContaBancaria(numero_conta="12345-X", saldo_inicial=1000.0)
    conta_joao = ContaBancaria(numero_conta="67890-Y", saldo_inicial=200.0)

    print(f"Conta {minha_conta._numero_conta} criada com saldo: R$ {minha_conta.saldo:.2f}")
    print(f"Conta {conta_joao._numero_conta} criada com saldo: R$ {conta_joao.saldo:.2f}")

    print("\n --- Testando Extrato Inicial ---")
    minha_conta.exibir_extrato()

    print("\n --- Depósito na minha conta ---")
    minha_conta.depositar(500)

    print("\n --- Saque na minha conta ---")
    minha_conta.sacar(250)

    print("\n --- Transferência para João ---")
    minha_conta.transferir(conta_joao, 400)

    print("\n --- Saldos após a transferência ---")
    minha_conta.consultar_saldo()
    conta_joao.consultar_saldo()

    print("\n --- Meu extrato ---")
    minha_conta.exibir_extrato()

    print("\n --- Extrato do João ---")
    conta_joao.exibir_extrato()

    print("\n --- Tentativa de saque com valor inválido ---")
    minha_conta.sacar(-100)

    print("\n --- Tentativa de transferência com saldo insuficiente ---")
    minha_conta.transferir(conta_joao, 2000)

    print("\n --- Salvando dados da minha conta ---")
    salvar_dados(minha_conta)

    print("\n --- Carregando conta a partir do arquivo ---")
    conta_carregada = carregar_dados()
    conta_carregada.exibir_extrato()