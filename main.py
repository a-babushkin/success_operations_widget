from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

cards_and_accounts = (
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
)
transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
if __name__ == "__main__":
    print("Фильтрация со указанным параметром state:")
    print(filter_by_state(transactions, "CANCELED"))
    print("Фильтрация с параметром по умолчанию:")
    print(filter_by_state(transactions))

    print("Сортировка по убыванию:")
    print(sort_by_date(transactions))
    print("Сортировка по возрастанию:")
    print(sort_by_date(transactions, False))

    print("Вывод маскированных номеров карт и счетов и их типов:")
    for item in cards_and_accounts:
        print(mask_account_card(item))

    print('Вывод даты в формате "ДД.ММ.ГГГГ":')
    print(get_date("2024-03-11T02:26:18.671407"))
