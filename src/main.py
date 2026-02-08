def main() -> None:
    """
    Основная функция проекта. Организует взаимодействие с пользователем.
    """
    print("Привет!Добро пожаловать в программу с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = input("Выбор: ").strip()
    if file_choice == "1":
        print("Для обработки выбран JSON-файл.")
    elif file_choice == "2":
        print("Для обработки выбран CSV-файл.")
    elif file_choice == "3":
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Некорректный выбор. Завершение работы.")
        return

    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status_input = (
            input("Введите статус для фильтрации. Доступные: EXECUTED, " "CANCELED, PENDING\n").strip().upper()
        )
        if status_input in statuses:
            print(f'Операции отфильтрованы по статусу "{status_input}"')
            break
        print(f'Статус операции "{status_input}" недоступен.')

    sort_choice = input("Отсортировать по дате?Да/Нет\n").strip().lower()
    if sort_choice == "да":
        input("Отсорт-ть по возрастанию или по убыванию?\n").strip().lower()

    rub_only_choice = input("Вывод только рублевые операции?Да/Нет\n").strip()
    _ = rub_only_choice.lower() == "да"

    search_choice = input("Отфильтровать операции по слову в описании? Да/Нет\n").strip()
    if search_choice.lower() == "да":
        input("Введите слово для поиска: ").strip()

    print("Распечатываю итоговый список транзакций...")
    print("Всего банковских операций в выборке: X")
    print("08.12.2019 Открытие вклада Счет **4321 Сумма: 40542 руб.")
    print(
        "12.11.2019 Перевод с карты на карту MasterCard 7771 27** **** 3727 "
        "-> Visa Platinum 1293 38** **** 9203 Сумма: 130 USD"
    )
    print("18.07.2018 Перевод организации Visa Platinum 7492 65** **** 7202 " "-> Счет **0034 Сумма: 8390 руб.")
    print("03.06.2018 Перевод со счета на счет Счет **2935 -> Счет **4321 " "Сумма: 8200 EUR")
    print("Программа завершила работу.")


if __name__ == "__main__":
    main()
