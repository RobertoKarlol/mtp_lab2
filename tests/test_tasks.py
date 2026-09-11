"""Проверки алгоритмов и консольного ввода."""

import subprocess
import sys
import unittest
from pathlib import Path

from tasks import (
    binary_search,
    count_vowels,
    multiplication_table,
    primes_up_to,
)


class TaskTests(unittest.TestCase):
    def test_primes_to_100(self):
        self.assertEqual(primes_up_to(), [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
        ])

    def test_prime_boundaries(self):
        for limit in (-5, 0, 1):
            with self.subTest(limit=limit):
                self.assertEqual(primes_up_to(limit), [])
        self.assertEqual(primes_up_to(2), [2])
        self.assertEqual(primes_up_to(3), [2, 3])
        self.assertNotIn(49, primes_up_to(49))

    def test_russian_vowels(self):
        self.assertEqual(count_vowels("АЕЁИОУЫЭЮЯаеёиоуыэюя"), 20)
        self.assertEqual(count_vowels("Съешь ещё этих мягких булок"), 9)

    def test_english_and_mixed_vowels(self):
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(count_vowels("Привет, Python!"), 3)

    def test_no_vowels(self):
        for text in ("", "123 !?", "бвгджзй", "rhythm"):
            with self.subTest(text=text):
                self.assertEqual(count_vowels(text), 0)

    def test_table(self):
        table = multiplication_table()
        self.assertEqual(len(table), 10)
        self.assertTrue(all(len(row) == 10 for row in table))
        self.assertEqual(table[0], list(range(1, 11)))
        self.assertEqual(table[6], [7, 14, 21, 28, 35, 42, 49, 56, 63, 70])
        self.assertEqual(table[-1], list(range(10, 101, 10)))

    def test_search_found(self):
        numbers = [-10, -3, 0, 2, 8, 15]
        for index, target in enumerate(numbers):
            with self.subTest(target=target):
                self.assertEqual(binary_search(numbers, target), index)

    def test_search_missing(self):
        for target in (-11, -1, 7, 16):
            with self.subTest(target=target):
                self.assertEqual(binary_search([-10, 0, 8, 15], target), -1)

    def test_search_empty_and_single(self):
        self.assertEqual(binary_search([], 5), -1)
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([5], 4), -1)

    def test_search_duplicates(self):
        numbers = [1, 2, 2, 2, 3]
        index = binary_search(numbers, 2)
        self.assertIn(index, (1, 2, 3))
        self.assertEqual(numbers[index], 2)


class ConsoleTests(unittest.TestCase):
    def run_program(self, user_input="", *args):
        root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [sys.executable, str(root / "main.py"), *args],
            input=user_input, capture_output=True, text=True,
            encoding="utf-8", timeout=5,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return result.stdout

    def test_demo(self):
        output = self.run_program("", "--demo")
        self.assertIn("89 97", output)
        self.assertIn("Гласных в строке «Привет, Python!»: 3", output)
        self.assertIn("Число 7: индекс 3", output)
        self.assertIn("Число 8: индекс -1", output)

    def test_menu_tasks(self):
        output = self.run_program("1\n2\nЁж\n3\n4\n1 3 5 7\n7\n0\n")
        self.assertIn("89 97", output)
        self.assertIn("Количество гласных: 1", output)
        self.assertIn("100", output)
        self.assertIn("Индекс: 3", output)

    def test_invalid_menu_and_input(self):
        output = self.run_program("9\n4\n1 x 3\n4\n1 3\nx\n0\n")
        self.assertIn("Нет такого пункта меню.", output)
        self.assertEqual(output.count("нужно вводить целые числа"), 2)

    def test_unsorted_list(self):
        output = self.run_program("4\n3 1 2\n1\n0\n")
        self.assertIn("список должен быть отсортирован", output)

    def test_empty_list(self):
        output = self.run_program("4\n\n1\n0\n")
        self.assertIn("Число не найдено.", output)

    def test_end_of_input(self):
        self.assertIn("Выход.", self.run_program())


if __name__ == "__main__":
    unittest.main()
