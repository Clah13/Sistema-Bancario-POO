# Roteiro de Práticas 06 - Sistema Bancário com POO

O roteiro tem como objetivo principal criar um programa que simule as operações realizadas em um sistema bancário, mas desta vez com foco na Programação Orientada a Objetos. O código encontrado no Repositório 'Sistema Bancário' é reutilizado aqui a fim de otimizar o tempo de desenvolvimento.

Suas atividades são incrementais, em que o primeiro código representa um MVP e os códigos subsequentes representam atualizações das entregas anteriores. Este roteiro também utiliza métodos de publicação descritos no roteiro anterior (Repositórios e Versionamento.)

Os códigos seguem um roteiro fixo criado pelo professor.
## Etapas de desenvolvimento

### Roteiro 04

Etapa 1: Definir a Classe Principal que representará uma conta bancária. [*Sysbank_POO_1*]

  >Implementa a Classe ContaBancaria e o método construtor \_\_init\_\_. Define regras de proteção dos atributos (ex: \_numero_conta). Implementa testes para exemplo de uso. 

Etapa 2: Mover as operações bancárias para dentro da classe como métodos.

  > Os principais métodos do menu - consultar saldo, depositar e sacar - são refatorados para dentro da classe ContaBancaria, com testes ou exemplos de uso.

Etapa 3: Adicionar as funcionalidades de extrato detalhado e transferência entre contas.

  > Refatoração dos métodos para exibir o extrato e transferir para outra conta, com adaptações necessárias para a Classe ContaBancaria.

Etapa 4: Salvar e carregar os dados das contas bancárias usando JSON.

> Implementa a função salvar_dados e carregar_dados para manter o histórico das operações na conta e também consultá-lo quando necessário.

Etapa 5: Criar o loop principal do programa que interage com o usuário e utiliza a classe ContaBancaria.

> Implementa o Menu utilizado para navegar no programa, conectando com os métodos e salvamento implementados nos passos anteriores. Permite a transferência entre conta, com um banco secundário (banco_secundario.json) para manter os registros.

Etapa 6: Desafio

> Implementa um protótipo para gerenciamento de múltiplas contas. Os dados são salvos em um único JSON (banco_centralizado). O Menu foi dividido em duas seções: criação de conta e ao entrar, ações bancárias.

Arquivos Extras: Banco de Dados [*banco_dados.json*], [*banco_secundario.json*], [*banco_centralizado.json*]
> Cópia do arquivo gerado durante testes.
