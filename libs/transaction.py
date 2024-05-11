import json

from tabulate import tabulate


class Transaction:
    def __init__(
        self,
        p_id: int,
        p_value: int,
        p_periodic: bool,
        p_note: str,
        p_done: bool,
        p_expiration_day: int,
        p_resp: str,
        p_type: str,
    ) -> None:
        """
        Classe destinada a descrever uma transação:

        @param p_id: Identificador único da transação.
        @param p_value: Valor da transação.
        @param p_periodic: True caso se repita todos os meses.
        @param p_note: Campo de cometario para outras explicações.
        @param p_type: Campo destinado ao tipo de transacao.
        @param p_done: Caso a transacao ja tenha sido feita.
        @param p_expiration_day: Data de vencimento da transação.
        @param p_resp: Responsável por realizar a transação.
        """
        self.id = p_id
        self.value = p_value
        self.periodic = p_periodic
        self.note = p_note
        self.type = p_type
        self.done = p_done
        self.expiration_day = p_expiration_day
        self.resp = p_resp


class Month:
    def __init__(self, p_mes, p_ano, p_transaction_list=[]):
        """
        Classe destinada a descrever um mes:

        @param p_transaction_list: Lista de transações de um lista.
        @param p_mes: Valor do mes.
        @param p_ano: Ano no qual se encontra o mês.
        """
        self.transaction_list = p_transaction_list
        self.mes = p_mes
        self.ano = p_ano

    def add_transaction(self, p_transaction: Transaction):

        """
        Adiciona uma transação no mes.

        @param p_transaction transação.
        """
        self.transaction_list += [p_transaction]

    def delete_transaction(self, transaction_to_delete: Transaction):
        """
        Exclui uma transação específica do mês.

        @param transaction_to_delete: Transação a ser excluída do mês.
        """
        # Verifica se a transação está na lista antes de tentar removê-la
        if transaction_to_delete in self.transaction_list:
            self.transaction_list.remove(transaction_to_delete)
        else:
            print('A transação não foi encontrada no mês.')

    def get_balance(self):
        # Calcular o saldo do mês somando os valores das transações concluídas
        return sum(
            transaction.value
            for transaction in self.transaction_list
            if transaction.done
        )

    def display_transactions_table(self):
        """
        Exibe as transações do mês em forma de tabela.
        """
        headers = [
            'ID',
            'Valor',
            'Periódica',
            'Nota',
            'Tipo',
            'Concluída',
            'Dia de Vencimento',
            'Responsável',
        ]
        table_data = []

        for transaction in self.transaction_list:
            table_data.append(
                [
                    transaction.id,
                    transaction.value,
                    'Sim' if transaction.periodic else 'Não',
                    transaction.note,
                    transaction.type,
                    'Sim' if transaction.done else 'Não',
                    transaction.expiration_day,
                    transaction.resp,
                ]
            )

        # Exibe a tabela usando a biblioteca tabulate
        print(tabulate(table_data, headers=headers, tablefmt='grid'))


class FinancialYear:
    def __init__(self, json_file_path):
        """
        Classe que contém uma lista de objetos Month, inicializada a partir de um arquivo JSON.

        @param json_file_path: Caminho para o arquivo JSON que contém os dados.
        """
        self.json_file_path = json_file_path
        self.month_list = self.load_data_from_json(json_file_path)

    def load_data_from_json(self, json_file_path):
        """
        Carrega os dados do arquivo JSON e retorna uma lista de objetos Month.

        @param json_file_path: Caminho para o arquivo JSON que contém os dados.
        @return: Lista de objetos Month.
        """
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
                # Verifica se a chave 'months' está presente no JSON
                if 'months' in data:
                    month_list = []
                    for month_data in data['months']:
                        # Cria objetos Month a partir dos dados do JSON
                        transaction_list = []
                        for transaction_data in month_data.get(
                            'transaction_list', []
                        ):
                            transaction_list += [
                                Transaction(
                                    transaction_data['id'],
                                    transaction_data['value'],
                                    transaction_data['periodic'],
                                    transaction_data['note'],
                                    transaction_data['done'],
                                    transaction_data['expiration_day'],
                                    transaction_data['resp'],
                                    transaction_data['type'],
                                )
                            ]
                        month = Month(
                            p_mes=month_data['mes'],
                            p_ano=month_data['ano'],
                            p_transaction_list=transaction_list,
                        )
                        month_list.append(month)
                    return month_list
                else:
                    raise ValueError("Chave 'months' não encontrada no JSON.")
        except FileNotFoundError:
            raise FileNotFoundError(
                f'O arquivo JSON em {json_file_path} não foi encontrado.'
            )
        except json.JSONDecodeError:
            raise ValueError(
                f'Erro ao decodificar o JSON no arquivo {json_file_path}.'
            )

    def save_data_to_json(self):
        """
        Salva os dados da lista de meses em um arquivo JSON.
        """
        data = {'months': []}

        for month in self.month_list:
            month_data = {
                'mes': month.mes,
                'ano': month.ano,
                'transaction_list': [],
            }

            for transaction in month.transaction_list:
                transaction_data = {
                    'id': transaction.id,
                    'value': transaction.value,
                    'periodic': transaction.periodic,
                    'note': transaction.note,
                    'type': transaction.type,
                    'done': transaction.done,
                    'expiration_day': transaction.expiration_day,
                    'resp': transaction.resp,
                }
                month_data['transaction_list'].append(transaction_data)

            data['months'].append(month_data)

        try:
            with open(self.json_file_path, 'w') as file:
                json.dump(data, file, indent=2)
                print(
                    f'Dados salvos com sucesso no arquivo JSON: {self.json_file_path}'
                )
        except IOError:
            print(
                f'Erro ao salvar os dados no arquivo JSON: {self.json_file_path}'
            )


# Exemplo de uso da classe FinancialYear
financial_year_instance = FinancialYear('data.json')
for i in range(len(financial_year_instance.month_list)):
    financial_year_instance.month_list[i].display_transactions_table()
financial_year_instance.save_data_to_json()
