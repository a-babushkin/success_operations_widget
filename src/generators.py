"""Набор функций, реализующих генераторы для обработки данных"""

def filter_by_currency(transaction_list: list[dict], currency: str) -> iter:
    filtered_transactions = list(
        filter(lambda x: x['operationAmount']['currency']['code'] == currency, transaction_list))
    for item_trans in filtered_transactions:
        yield item_trans


def transaction_descriptions(transaction_list: list[dict]) -> iter:
    filtered_description = list(map(lambda x: x['description'], transaction_list))
    for item_trans in filtered_description:
        yield item_trans

def card_number_generator(start: int = 1, finish: int = 9999999999999999) -> iter:
    if start < finish:
        for item_trans in range(start, finish + 1):
            item_card_number = "0" * (16 - len(str(item_trans))) + str(item_trans)
            yield item_card_number[:4] + ' ' + item_card_number[4:9] + ' ' + item_card_number[8:13] + ' ' + item_card_number[12:]
    else:
        yield "Неверный диапазон!"

if __name__ == '__main__':
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]

    usd_transactions = filter_by_currency(transactions, "RUB")
    for _ in range(2):
        print(next(usd_transactions))

    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))

    for card_number in card_number_generator(467446741, 467446755):
        print(card_number)
