"""

"""
import unittest
from unittest.mock import patch
from io import StringIO
import sys

import self as sp


class SelfPyTestCase(unittest.TestCase):

    def test_ex_4_2_2(self):
        self.assertIn('ex_4_2_2', dir(sp), 'Function to found')
        cases = (('sun', 'NOT'), ('bob', 'OK'), ('Borrow or rob', 'OK'))
        for case in cases:
            self.assertEqual(sp.ex_4_2_2(case[0]), case[1])

    def test_ex_6_3_1(self):
        self.assertIn('are_lists_equal', dir(sp), 'Function to found')
        list1 = [0.6, 1, 2, 3]
        list2 = [3, 2, 0.6, 1]
        list3 = [9, 0, 5, 10.5]
        self.assertEqual(sp.are_lists_equal(list1, list2), True)
        self.assertEqual(sp.are_lists_equal(list1, list3), False)

    def test_ex_6_3_2(self):
        self.assertIn('longest', dir(sp), 'Function to found')
        cases = (
            (["111", "234", "2000", "goru", "birthday", "09"], "birthday"),
            (["nanu", "nanu", "mork", "and", "Williams", "mindy", "Robin"], "Williams"),
        )
        for case in cases:
            self.assertEqual(sp.longest(case[0]), case[1])

    def test_ex_6_4_1(self):
        self.assertIn('check_valid_input', dir(sp), 'Function to found')
        cases = (
            ('C', ['a', 'b', 'c'], False, 'in old letters, but uppercase.'),
            ('ep', ['a', 'b', 'c'], False, '2 letters'),
            ('$', ['a', 'b', 'c'], False, 'not alpha'),
            ('s', ['a', 'b', 'c'], True, 'valid'),
            ('a', [], True, 'empty old letters'),
        )
        for case in cases:
            self.assertEqual(sp.check_valid_input(case[0], case[1]), case[2], case[3])

    def test_ex_6_4_2(self):
        self.assertIn('try_update_letter_guessed', dir(sp), 'Function to found')
        old_letters = ['a', 'p', 'c', 'f']
        cases = (
            ('A', old_letters, 'X\na -> c -> f -> p\n', False, 'in old letters, but uppercase.'),
            ('s', old_letters, '', True, 'OK guess "s"'),
            ('$', old_letters, 'X\na -> c -> f -> p -> s\n', False, 'not alpha'),
            ('d', old_letters, '', True, 'OK guess "d"'),
            # ('a', [], True, 'empty old letters'),
        )
        for case in cases:
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                rv = sp.try_update_letter_guessed(case[0], case[1])
                op = fake_stdout.getvalue()
                # print(f'rv: {rv}; op: {op}', file=sys.stderr)
                self.assertTrue(op == case[2] and rv == case[3], case[4])

    def test_ex_7_1_4(self):
        self.assertIn('squared_numbers', dir(sp), 'Function to found')
        cases = (
            (4, 8, [16, 25, 36, 49, 64]),
            (-3, 3, [9, 4, 1, 0, 1, 4, 9]),
        )
        for case in cases:
            self.assertEqual(sp.squared_numbers(case[0], case[1]), case[2])

    def test_ex_7_2_1(self):
        self.assertIn('is_greater', dir(sp), 'Function to found')
        base_list = [1, 30, 25, 60, 27, 28]
        cases = (
            (base_list, 28, [30, 60], 'return 2 out of 6'),
            (base_list, 0, [1, 30, 25, 60, 27, 28], 'return all 6'),
            (base_list, 60, [], 'return empty'),
        )
        for case in cases:
            self.assertEqual(sorted(sp.is_greater(case[0], case[1])), sorted(case[2]))

    def test_ex_7_2_2(self):
        self.assertIn('numbers_letters_count', dir(sp), 'Function to found')
        cases = (
            ('Python 3.6.3', [3, 9], 'example test'),
            ('363', [3, 0], 'no letters'),
            ('Python...', [0, 9], 'no digits'),
        )
        for case in cases:
            self.assertEqual(sp.numbers_letters_count(case[0]), case[1], case[2])


if __name__ == '__main__':
    unittest.main()
