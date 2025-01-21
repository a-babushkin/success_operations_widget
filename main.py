from src.widget import mask_account_card

cards_and_accounts = (
    'Maestro 1596837868705199',
    'Счет 64686473678894779589',
    'MasterCard 7158300734726758',
    'Счет 35383033474447895560',
    'Visa Classic 6831982476737658',
    'Visa Platinum 8990922113665229',
    'Visa Gold 5999414228426353',
    'Счет 73654108430135874305'
)

if __name__ == "__main__":
    for item in cards_and_accounts:
        print(item.split()[0], end=' ')
        print(mask_account_card(item))
