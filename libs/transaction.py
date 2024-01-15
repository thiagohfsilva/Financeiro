class Transaction:
    def __init__(self, p_value : int, p_periodic: bool,
                 p_note : str, p_done : bool, p_expiration_day : int, p_resp : str,
                 p_tepe : str) -> None :
        '''
        Classe destinada a descrever uma transação:

        @param p_value: Valor da transação.
        @param p_periodic: True caso se repita todos os meses.
        @param p_note: Campo de cometario para outras explicações.
        @param p_done: Caso a transacao ja tenha sido feita.
        @param p_expiration_day: Data de vencimento da transação.
        @param p_resp: Responsável por realizar a transação.
        '''
        self.value = p_value
        self.periodic = p_periodic
        self.note = p_note
        self.type = p_type
        self.done = p_done
        self.expiration_day = p_expiration_day
        self.resp = p_resp


class Month:
    def __init__(self,  p_mes, p_ano, p_transaction_list=[]):
        '''
        Classe destinada a descrever um mes:

        @param p_transaction_list: Lista de transações de um lista.
        @param p_mes: Valor do mes.
        @param p_ano: Ano no qual se encontra o mês.
        '''
        self.transaction_list = p_transaction_list
        self.mes = p_mes
        self.ano = p_ano

    def add_transaction(self, p_transaction: Transaction):

        '''
        Adiciona uma transação no mes.

        @param p_transaction transação.
        '''
        self.transaction_list += [p_transaction]
