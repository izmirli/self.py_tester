"""

"""
import unittest
from unittest.mock import patch
from io import StringIO
import sys

import self as sp


class SelfPyTestCase(unittest.TestCase):

    # def test_ex_4_2_2(self):
    #     self.assertIn('ex_4_2_2', dir(sp), 'Function to found')
    #     cases = (('sun', 'NOT'), ('bob', 'OK'), ('Borrow or rob', 'OK'))
    #     for case in cases:
    #         self.assertEqual(sp.ex_4_2_2(case[0]), case[1])

    def test_ex_5_3_4(self):
        self.assertIn('last_early', dir(sp), 'Function to found')
        cases = (
            ("happy birthday", True),
            ("best of luck", False),
            ("Wow", True),
            ("X", False),
        )
        for case in cases:
            self.assertEqual(sp.last_early(case[0]), case[1])

    def test_ex_5_3_5(self):
        self.assertIn('distance', dir(sp), 'Function to found')
        cases = (
            ([1, 2, 10], True),
            ([4, 5, 3], False),
            ([1, 2, 3], False),
        )
        for case in cases:
            self.assertEqual(sp.distance(*case[0]), case[1])

    def test_ex_5_3_6(self):
        self.assertIn('filter_teens', dir(sp), 'Function to found')
        cases = (
            ([], 0, 'no args, default ages'),
            ([20], 20, 'one grownup, missing 2 args - default teen ages'),
            ([1, 2, 3], 6, 'all my children < 13'),
            ([2, 13, 1], 3, '2 kids, one teen'),
            ([2, 1, 15], 18, '2 kids, one special teen'),
        )
        for case in cases:
            self.assertEqual(sp.filter_teens(*case[0]), case[1], case[2])

    def test_ex_5_3_7(self):
        self.assertIn('chocolate_maker', dir(sp), 'Function to found')
        cases = (
            ([3, 1, 8], True),
            ([3, 1, 9], False),
            ([3, 2, 9], False),
            ([3, 2, 10], True),
            ([0, 2, 10], True),
            ([10, 0, 10], True),
        )
        for case in cases:
            self.assertEqual(sp.chocolate_maker(*case[0]), case[1])

    def test_ex_5_5_1(self):
        self.assertIn('is_valid_input', dir(sp), 'Function to found')
        cases = (
            ('a', True, 'a is valid'),
            ('A', True, 'A is valid'),
            ('$', False, '$ is invalid'),
            ('ab', False, '"ab" is invalid'),
            ('app$', False, '"app$" is invalid'),
            ('', False, '"" (empty string) is invalid'),
            ('א', False, 'א is invalid'),
        )
        for case in cases:
            self.assertEqual(sp.is_valid_input(case[0]), case[1], case[2])

    def test_ex_6_1_2(self):
        self.assertIn('shift_left', dir(sp), 'Function to found')
        cases = (
            ([0, 1, 2], [1, 2, 0]),
            (['monkey', 2.0, 1], [2.0, 1, 'monkey']),
        )
        for case in cases:
            self.assertEqual(sp.shift_left(case[0]), case[1])

    def test_ex_6_2_3(self):
        self.assertIn('format_list', dir(sp), 'Function to found')
        cases = (
            (["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"],
             'hydrogen, lithium, boron and magnesium'),
            (["hydrogen", "helium"], 'hydrogen and helium'),
        )
        for case in cases:
            self.assertEqual(sp.format_list(case[0]), case[1])

    def test_ex_6_2_4(self):
        self.assertIn('extend_list_x', dir(sp), 'Function to found')
        cases = (
            ([[4, 5, 6], [1, 2, 3]], [1, 2, 3, 4, 5, 6]),
        )
        for case in cases:
            self.assertEqual(sp.extend_list_x(*case[0]), case[1])

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
