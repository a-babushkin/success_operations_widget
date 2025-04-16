import pandas as pd


def get_transaction_from_csv_file(path_to_file: str) -> list[dict]:
    """Get path to CSV file and return list of dictionary transactions"""
    try:
        transactions = pd.read_csv(path_to_file, sep=";")
        return transactions.to_dict("records")
    except FileNotFoundError:
        return [{}]


def get_transaction_from_excel_file(path_to_file: str) -> list[dict]:
    """Get path to Excell file and return list of dictionary transactions"""
    try:
        transactions = pd.read_excel(path_to_file)
        return transactions.to_dict("records")
    except FileNotFoundError:
        return [{}]
