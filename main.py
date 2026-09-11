"""Консольный запуск лабораторной работы №2."""

import argparse

from tasks import (
    binary_search,
    count_vowels,
    multiplication_table,
    primes_up_to,
)


def print_table():
    """Вывести таблицу с заголовками строк и столбцов."""
    print("   |" + "".join(f"{number:4}" for number in range(1, 11)))
    print("---+" + "-" * 40)
    for number, row in enumerate(multiplication_table(), start=1):
        print(f"{number:2} |" + "".join(f"{value:4}" for value in row))


def run_search():
    """Прочитать отсортированный список и искомое целое число."""
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


def demo():
    """Показать результаты всех заданий без ввода с клавиатуры."""
    print("Простые числа до 100:")
    print(*primes_up_to())
    text = "Привет, Python!"
    print(f"Гласных в строке «{text}»: {count_vowels(text)}")
    print("Таблица умножения:")
    print_table()
    numbers = [1, 3, 5, 7, 9, 11]
    print(f"Бинарный поиск в списке {numbers}:")
    print(f"Число 7: индекс {binary_search(numbers, 7)}")
    print(f"Число 8: индекс {binary_search(numbers, 8)} (не найдено)")


def main():
    """Обработать параметры запуска и показать меню."""
    parser = argparse.ArgumentParser(description="МТП, лабораторная №2")
    parser.add_argument("--demo", action="store_true",
                        help="показать примеры без ввода с клавиатуры")
    args = parser.parse_args()
    if args.demo:
        demo()
        return

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
