# Sistema Bancário Simples

Este repositório contém um script Python que simula um sistema bancário básico. O programa permite que os usuários realizem operações como saque, depósito e consulta de extrato. O código foi desenvolvido como parte de um exercício para praticar conceitos básicos de programação em Python, como estruturas de controle, loops e manipulação de variáveis.

## Funcionalidades

O sistema bancário oferece as seguintes funcionalidades:

1. **Saque**: Permite ao usuário sacar dinheiro da conta, respeitando um limite de R$ 500 por saque e um limite máximo de 3 saques diários.
2. **Depósito**: Permite ao usuário depositar dinheiro na conta.
3. **Extrato**: Exibe o saldo atual da conta.
4. **Sair**: Encerra o programa.

## Como Executar

Para executar o sistema bancário, siga os passos abaixo:

1. Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/).
2. Clone este repositório ou copie o código para um arquivo Python (`sistema_bancario.py`).
3. Execute o script no terminal ou prompt de comando:

   ```bash
   python sistema_bancario.py
   ```

4. Siga as instruções exibidas no menu para realizar as operações desejadas.

## Estrutura do Código

O código é composto por um loop `while` que exibe um menu de opções para o usuário. Dependendo da escolha do usuário, o programa executa uma das seguintes operações:

- **Saque**: Verifica se o usuário ainda tem saques disponíveis e se o saldo é suficiente para o valor solicitado.
- **Depósito**: Adiciona o valor depositado ao saldo da conta.
- **Extrato**: Exibe o saldo atual da conta.
- **Sair**: Encerra o loop e finaliza o programa.

### Variáveis Principais

- `saldo`: Armazena o saldo atual da conta.
- `limite`: Define o limite máximo de saque por operação (R$ 500).
- `extrato`: Armazena o histórico de transações (não implementado no código atual).
- `numero_de_saque`: Conta quantos saques foram realizados no dia.
- `LIMITE_DE_SAQUE`: Define o número máximo de saques permitidos por dia (3).

## Melhorias Futuras

O código atual é uma versão simples e pode ser melhorado com as seguintes funcionalidades:

1. **Histórico de Transações**: Armazenar e exibir um histórico detalhado de todas as transações (saques e depósitos).
2. **Validação de Entrada**: Garantir que o usuário insira valores válidos (números positivos) para saques e depósitos.
3. **Interface Gráfica**: Implementar uma interface gráfica para melhorar a experiência do usuário.
4. **Persistência de Dados**: Salvar o saldo e o histórico de transações em um arquivo para que os dados não sejam perdidos ao fechar o programa.

