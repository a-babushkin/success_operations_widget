import os

import pandas as pd

from src.dialogs import choose_state, additional_questions
from src.utils import read_json_file


def json_data_processing(file_name: str) -> None:
    data_from_json = read_json_file(os.path.join(file_name, 'data', 'operations.json'))
    state = choose_state()
    filter_state = [transaction for transaction in data_from_json if transaction.get('state') == state]
    options = additional_questions()

    # filter_state = df.loc[df.state == choose_state()]
    #
    if options['rub_transactions']:
        filter_rub = [transaction for transaction in filter_state if transaction.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']# filter_rub = filter_state.loc[filter_state['operationAmount']['currency']['code'] == 'RUB']
    # print(options)
        print(len(filter_state), len(filter_rub))


def csv_data_processing(file_name: str) -> None:
    df = pd.read_csv(os.path.join(file_name, 'data', 'transactions.csv'))
    print(df)


def excel_data_processing(file_name: str) -> None:
    df = pd.read_excel(os.path.join(file_name, 'data', 'transactions_excel.xlsx'))
    print(df)
