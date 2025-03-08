
def choose_state() -> str:
    """Осуществляет выбор статуса операции"""
    while True:
        user_input = input('''
Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    ''')
        try:
            selected_status = user_input.upper()
            if selected_status in ['EXECUTED', 'CANCELED', 'PENDING']:
                print(f"Операции отфильтрованы по статусу {selected_status}.")
                return selected_status
            else:
                print(f"Статус операции {selected_status} недоступен.")
        except ValueError:
            print("Ошибка: Пожалуйста, попробуйте снова.")


def additional_questions() -> dict:
    answers = {}
    while True:
        input_value = input('Отсортировать операции по дате? Да / Нет').lower()
        if input_value in ["да", "д"]:
            answers['sort_by_date'] = True
            break
        elif input_value in ["нет", "н"]:
            answers['sort_by_date'] = False
            break
        else:
            print("Можно выбрать только Да или Нет")

    while True:
        input_value = input('Отсортировать по возрастанию или по убыванию?').lower()
        if input_value in ["по возрастанию", "в"]:
            answers['sort_asc'] = True
            break
        elif input_value in ["по убыванию", "у"]:
            answers['sort_asc'] = False
            break
        else:
            print("Можно выбрать только по возрастанию или по убыванию")

    while True:
        input_value = input('Выводить  только  рублевые транзакции? Да / Нет').lower()
        if input_value  in ["да", "д"]:
            answers['rub_transactions'] = True
            break
        elif input_value  in ["нет", "н"]:
            answers['rub_transactions'] = False
            break
        else:
            print("Можно выбрать только Да или Нет")

    while True:
        input_value = input('Отфильтровать список транзакций по определенному слову в описании? Да / Нет').lower()
        if input_value  in ["да", "д"]:
            answers['filter_by_word'] = input('Введите слово')
            break
        elif input_value  in ["нет", "н"]:
            answers['filter_by_word'] = ''
            break
        else:
            print("Можно выбрать только Да или Нет")
    return answers