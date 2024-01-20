# Sistema de Gestão Financeira Pessoal

Este repositório contém um sistema simples de gestão financeira pessoal em Python. Ele permite a criação de transações financeiras mensais, como despesas e receitas, organizadas em meses de um ano financeiro.

## Estrutura do Código

O código é dividido em três principais classes:

### Transaction

- **Atributos:**
  - `id`: Identificador único da transação.
  - `value`: Valor da transação.
  - `periodic`: Indica se a transação se repete todos os meses.
  - `note`: Campo para comentários ou explicações adicionais.
  - `type`: Tipo da transação (e.g., Despesa, Receita).
  - `done`: Indica se a transação já foi realizada.
  - `expiration_day`: Dia de vencimento da transação.
  - `resp`: Responsável por realizar a transação.

### Month

- **Atributos:**
  - `transaction_list`: Lista de transações do mês.
  - `mes`: Valor do mês.
  - `ano`: Ano do mês.

- **Métodos Principais:**
  - `add_transaction(transaction)`: Adiciona uma transação ao mês.
  - `delete_transaction(transaction_to_delete)`: Exclui uma transação específica do mês.
  - `get_balance()`: Calcula o saldo do mês somando os valores das transações concluídas.
  - `display_transactions_table()`: Exibe as transações do mês em forma de tabela.

### FinancialYear

- **Atributos:**
  - `json_file_path`: Caminho para o arquivo JSON que contém os dados.
  - `month_list`: Lista de objetos Month.

- **Métodos Principais:**
  - `load_data_from_json(json_file_path)`: Carrega os dados do arquivo JSON.
  - `save_data_to_json()`: Salva os dados da lista de meses em um arquivo JSON.

## Como Usar

1. Instale as dependências necessárias utilizando o seguinte comando:
~~~~
pip install tabulate
~~~~

2. Execute o código principal fornecendo o caminho para o arquivo JSON de dados.

Exemplo:
~~~~
financial_year_instance = FinancialYear('data.json')
~~~~

3. Interaja com o sistema criando, visualizando e manipulando transações e meses.
Exemplo:
~~~~
# Exibir tabela de transações para cada mês
for month in financial_year_instance.month_list:
    month.display_transactions_table()

# Adicionar uma nova transação ao primeiro mês
new_transaction = Transaction(id=5, value=75.0, periodic=False, note="Compra online", done=False, expiration_day=20, resp="Ana", type="Despesa")
financial_year_instance.month_list[0].add_transaction(new_transaction)

# Salvar as alterações no arquivo JSON
financial_year_instance.save_data_to_json()
~~~~

Lembre-se de substituir 'data.json' pelo caminho do seu próprio arquivo JSON, se necessário.

Este sistema oferece uma estrutura básica para gerenciar transações financeiras pessoais em um formato mensal. Sinta-se à vontade para adaptar e expandir conforme necessário.
