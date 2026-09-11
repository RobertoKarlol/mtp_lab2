"""Задания по структурному программированию, вариант 5."""


def primes_up_to(limit=100):
    """Вернуть простые числа от 2 до limit включительно."""
    primes = []
    for number in range(2, limit + 1):
        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                break
            divisor += 1
        else:
            primes.append(number)
    return primes


def count_vowels(text):
    """Подсчитать русские и английские гласные без учёта регистра."""
    vowels = "аеёиоуыэюяaeiou"
    count = 0
    for letter in text.lower():
        if letter in vowels:
            count += 1
    return count


def multiplication_table():
    """Вернуть таблицу умножения чисел от 1 до 10."""
    table = []
    for first in range(1, 11):
        row = []
        for second in range(1, 11):
            row.append(first * second)
        table.append(row)
    return table


def binary_search(numbers, target):
    """Найти индекс target в отсортированном списке или вернуть -1."""
    left = 0
    right = len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
