# Desafio

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
                print(
                    f"Transferência de R$ {valor_transferencia:.2f} para conta {conta_destino._numero_conta} realizada com sucesso.")
                print(f"Seu novo saldo é: R$ {self.saldo:.2f}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                # Chamar o método depositar da conta_destino
                conta_destino.depositar(
                    valor_transferencia)  # Chama o método depositar() da conta destino para adicionar o valor.

            else:
                print("Saldo insuficiente para realizar a transferência.")

        except ValueError:
            print("Valor inválido para transferência. Por favor, digite um número.")


def salvar_tudo(contas, filename="banco_centralizado.json"):
    """Salva os dados de todas as contas existentes em um único arquivo JSON"""

    dados = {}
    for numero, conta in contas.items():
        dados[numero] = {
            "numero_conta": conta._numero_conta,
            "saldo": conta.saldo,
            "extrato": conta.extrato
        }
    with open(filename, "w") as f:
        json.dump(dados, f, indent=4)


def carregar_tudo(filename="banco_centralizado.json"):
    """Carrega os dados de múltiplas contas de um arquivo JSON"""
    contas = {}
    try:
        with open(filename, "r") as f:
            dados = json.load(f)
            for numero, info in dados.items():
                contas[numero] = ContaBancaria(
                    numero_conta=info["numero_conta"],
                    saldo_inicial=info["saldo"],
                    extrato_inicial=info["extrato"]
                )
    except FileNotFoundError:
        print("Arquivo de contas não encontrado. Iniciando com 0 contas.")
    return contas

def criar_nova_conta(contas):
    """Cria uma nova conta e adiciona ao dicionário de contas"""

    numero = input("Digite o número da nova conta: ")

    if numero in contas:
        print("Essa conta já existe.")

    else:
        contas[numero] = ContaBancaria(numero)
        print(f"Conta {numero} criada com sucesso!")


# Função para selecionar uma conta existente
def selecionar_conta(contas):
    """Permite ao usuário selecionar uma conta existente"""

    numero = input("Digite o número da conta que deseja acessar: ")

    if numero in contas:
        return contas[numero]

    else:
        print("Conta não encontrada.")
        return None


# Execução principal do sistema com suporte a múltiplas contas
if __name__ == "__main__":

    # Carrega todas as contas já salvas anteriormente
    contas = carregar_tudo()

    while True:
        print("\n--- Menu Principal ---")
        print("1 - Criar nova conta")
        print("2 - Acessar conta existente")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_nova_conta(contas)

        elif escolha == "2":
            conta = selecionar_conta(contas)
            if conta:
                while True:
                    print(f"\n--- Acessando conta {conta._numero_conta} ---")
                    print("1 - Consultar saldo")
                    print("2 - Depositar")
                    print("3 - Sacar")
                    print("4 - Extrato")
                    print("5 - Transferir para outra conta")
                    print("6 - Voltar ao menu principal")
                    op = input("Escolha: ")

                    if op == "1":
                        conta.consultar_saldo()
                    elif op == "2":
                        valor = input("Valor do depósito: ")
                        conta.depositar(valor)
                    elif op == "3":
                        valor = input("Valor do saque: ")
                        conta.sacar(valor)
                    elif op == "4":
                        conta.exibir_extrato()
                    elif op == "5":
                        destino = input("Número da conta destino: ")
                        if destino in contas:
                            valor = input("Valor da transferência: ")
                            conta.transferir(contas[destino], valor)
                        else:
                            print("Conta destino não encontrada.")
                    elif op == "6":
                        break
                    else:
                        print("Opção inválida.")

        elif escolha == "3":
            salvar_tudo(contas)  # Salva os dados de todas as contas antes de sair
            print("Obrigado por utilizar nosso banco virtual!")
            break

        else:
            print("Opção inválida.")