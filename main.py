import os

from src.data_processing import json_data_processing, csv_data_processing, excel_data_processing

def run_start_menu() -> None:
    """Запускает начальное меню для выбора типа файла данных"""
    while True:
        user_input = input('''
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    ''')
        try:
            selected_menu = int(user_input)
            file_name = (os.path.dirname(__file__))
            match selected_menu:
                case 1:
                    print("Для обработки выбран JSON-файл.")
                    json_data_processing(file_name)
                    return
                case 2:
                    print("Для обработки выбран CSV-файл.")
                    csv_data_processing(file_name)
                    return
                case 3:
                    print("Для обработки выбран XLSX-файл.")
                    excel_data_processing(file_name)
                    return
                case _:
                    print("Неверный выбор! Попробуйте еще раз.")
        except ValueError:
            print("Ошибка: введено не число. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    run_start_menu()


    # file_name = run_tart_menu()
    # file_name = additional_questions()

