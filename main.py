from tasks import (
    binary_search,
    count_vowels,
    multiplication_table,
    primes_up_to,
)


def print_table():
    print("   |" + "".join(f"{number:4}" for number in range(1, 11)))
    print("---+" + "-" * 40)
    for number, row in enumerate(multiplication_table(), start=1):
        print(f"{number:2} |" + "".join(f"{value:4}" for value in row))


def run_search():
    try:
        numbers = [int(value) for value in input(
            "Введите целые числа по возрастанию через пробел: "
        ).split()]
        target = int(input("Искомое число: "))
    except ValueError:
        print("Ошибка: нужно вводить целые числа.")
        return

    for index in range(1, len(numbers)):
        if numbers[index] < numbers[index - 1]:
            print("Ошибка: список должен быть отсортирован по возрастанию.")
            return

    index = binary_search(numbers, target)
    if index == -1:
        print("Число не найдено.")
    else:
        print(f"Индекс: {index} (нумерация с нуля).")


def main():
    while True:
        print("\n1. Простые числа до 100")
        print("2. Подсчёт гласных")
        print("3. Таблица умножения")
        print("4. Бинарный поиск")
        print("0. Выход")
        try:
            choice = input("Выберите задание: ").strip()
            if choice == "0":
                return
            if choice == "1":
                print(*primes_up_to())
            elif choice == "2":
                print("Количество гласных:", count_vowels(input("Строка: ")))
            elif choice == "3":
                print_table()
            elif choice == "4":
                run_search()
            else:
                print("Нет такого пункта меню.")
        except (EOFError, KeyboardInterrupt):
            print("\nВыход.")
            return


if __name__ == "__main__":
    main()
