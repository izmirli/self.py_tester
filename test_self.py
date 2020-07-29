"""Automatic tests for self.py course.

Course URL: https://campus.gov.il/course/course-v1-cs-gov_cs_selfpy101/
"""
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from collections import deque

import self as sp

# list of ASCII hangman phases from:
# https://s3.eu-west-1.amazonaws.com/data.cyber.org.il/virtual_courses/python/rolling_assignment/resources/hangman.txt
HANGMAN_ASCII_PHASE = [
    # [0]
    r"""    x-------x""",
    # [1]
    r"""    x-------x
    |
    |
    |
    |
    |""",
    # [2]
    r"""    x-------x
    |       |
    |       0
    |
    |
    |""",
    # [3]
    r"""    x-------x
    |       |
    |       0
    |       |
    |
    |""",
    # [4]
    r"""    x-------x
    |       |
    |       0
    |      /|\
    |
    |""",
    # [5]
    r"""    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |""",
    # [6]
    r"""    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |""",
]


class SelfPyTestCase(unittest.TestCase):

    # def test_ex_4_2_2(self):
    #     self.assertIn('ex_4_2_2', dir(sp), 'Function to found')
    #     cases = (('sun', 'NOT'), ('bob', 'OK'), ('Borrow or rob', 'OK'))
    #     for case in cases:
    #         self.assertEqual(sp.ex_4_2_2(case[0]), case[1])

    def test_ex_5_3_4(self):
        """Testing last_early function"""
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
        """Testing distance function"""
        self.assertIn('distance', dir(sp), 'Function to found')
        cases = (
            ([1, 2, 10], True),
            ([4, 5, 3], False),
            ([1, 2, 3], False),
        )
        for case in cases:
            self.assertEqual(sp.distance(*case[0]), case[1])

    def test_ex_5_3_6(self):
        """Testing filter_teens function"""
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
        """Testing chocolate_maker function"""
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
        """Testing is_valid_input function"""
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
        """Testing shift_left function"""
        self.assertIn('shift_left', dir(sp), 'Function to found')
        cases = (
            ([0, 1, 2], [1, 2, 0]),
            (['monkey', 2.0, 1], [2.0, 1, 'monkey']),
        )
        for case in cases:
            self.assertEqual(sp.shift_left(case[0]), case[1])

    def test_ex_6_2_3(self):
        """Testing format_list function"""
        self.assertIn('format_list', dir(sp), 'Function to found')
        cases = (
            (["hydrogen", "helium", "lithium", "beryllium", "boron",
              "magnesium"], 'hydrogen, lithium, boron and magnesium'),
            (["hydrogen", "helium"], 'hydrogen and helium'),
        )
        for case in cases:
            self.assertEqual(sp.format_list(case[0]), case[1])

    def test_ex_6_2_4(self):
        """Testing extend_list_x function"""
        self.assertIn('extend_list_x', dir(sp), 'Function to found')
        cases = (
            ([[4, 5, 6], [1, 2, 3]], [1, 2, 3, 4, 5, 6]),
        )
        for case in cases:
            self.assertEqual(sp.extend_list_x(*case[0]), case[1])

    def test_ex_6_3_1(self):
        """Testing are_lists_equal function"""
        self.assertIn('are_lists_equal', dir(sp), 'Function to found')
        list1 = [0.6, 1, 2, 3]
        list2 = [3, 2, 0.6, 1]
        list3 = [9, 0, 5, 10.5]
        self.assertEqual(sp.are_lists_equal(list1, list2), True)
        self.assertEqual(sp.are_lists_equal(list1, list3), False)

    def test_ex_6_3_2(self):
        """Testing longest function"""
        self.assertIn('longest', dir(sp), 'Function to found')
        cases = (
            (["111", "234", "2000", "goru", "birthday", "09"], "birthday"),
            (["nanu", "nanu", "mork", "and", "Williams", "mindy", "Robin"],
             "Williams"),
        )
        for case in cases:
            self.assertEqual(sp.longest(case[0]), case[1])

    def test_ex_6_4_1(self):
        """Testing check_valid_input function"""
        self.assertIn('check_valid_input', dir(sp), 'Function to found')
        cases = (
            (['C', ['a', 'b', 'c']], False, 'in old letters, but uppercase.'),
            (['ep', ['a', 'b', 'c']], False, '2 letters'),
            (['$', ['a', 'b', 'c']], False, 'not alpha'),
            (['s', ['a', 'b', 'c']], True, 'valid'),
            (['a', []], True, 'empty old letters'),
        )
        for case in cases:
            self.assertEqual(sp.check_valid_input(*case[0]), case[1], case[2])

    def test_ex_6_4_2(self):
        """Testing try_update_letter_guessed function"""
        self.assertIn('try_update_letter_guessed', dir(sp), 'Function missing')
        old_letters = ['a', 'p', 'c', 'f']
        cases = (
            ('A', old_letters, 'X\na -> c -> f -> p\n', False,
             'in old letters, but uppercase.'),
            ('s', old_letters, '', True, 'OK guess "s"'),
            ('$', old_letters, 'X\na -> c -> f -> p -> s\n', False,
             'not alpha'),
            ('d', old_letters, '', True, 'OK guess "d"'),
            # ('a', [], True, 'empty old letters'),
        )
        for case in cases:
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                rv = sp.try_update_letter_guessed(case[0], case[1])
                op = fake_stdout.getvalue()
                # print(f'rv: {rv}; op: {op}; op == case[2] {op == case[2]}; '
                #       f'rv == case[3] {rv == case[3]}', file=sys.stderr)
                self.assertTrue(op == case[2] and rv == case[3], case[4])

    def test_ex_7_1_4(self):
        """Testing squared_numbers function"""
        self.assertIn('squared_numbers', dir(sp), 'Function to found')
        cases = (
            (4, 8, [16, 25, 36, 49, 64]),
            (-3, 3, [9, 4, 1, 0, 1, 4, 9]),
        )
        for case in cases:
            self.assertEqual(sp.squared_numbers(case[0], case[1]), case[2])

    def test_ex_7_2_1(self):
        """Testing is_greater function"""
        self.assertIn('is_greater', dir(sp), 'Function to found')
        base_list = [1, 30, 25, 60, 27, 28]
        cases = (
            ([base_list, 28], [30, 60], 'return 2 out of 6'),
            ([base_list, 0], [1, 30, 25, 60, 27, 28], 'return all 6'),
            ([base_list, 60], [], 'return empty'),
        )
        for case in cases:
            self.assertEqual(sorted(sp.is_greater(*case[0])), sorted(case[1]))

    def test_ex_7_2_2(self):
        """Testing numbers_letters_count function"""
        self.assertIn('numbers_letters_count', dir(sp), 'Function to found')
        cases = (
            ('Python 3.6.3', [3, 9], 'example test'),
            ('363', [3, 0], 'no letters'),
            ('Python...', [0, 9], 'no digits'),
        )
        for case in cases:
            self.assertEqual(sp.numbers_letters_count(case[0]), case[1],
                             case[2])

    def test_ex_7_2_4(self):
        """Testing seven_boom function"""
        self.assertIn('seven_boom', dir(sp), 'Function to found')
        self.assertEqual(
            sp.seven_boom(17),
            ['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM',
             15, 16, 'BOOM']
        )

    def test_ex_7_2_5(self):
        """Testing sequence_del function"""
        self.assertIn('sequence_del', dir(sp), 'Function to found')
        cases = (
            ('ppyyyyythhhhhooonnnnn', 'python'),
            ('SSSSsssshhhh', 'Ssh'),
            ('Heeyyy   yyouuuu!!!', 'Hey you!'),
        )
        for case in cases:
            self.assertEqual(sp.sequence_del(case[0]), case[1])

    @unittest.skip('To test Ex 7.2.6, comment this line')
    def test_ex_7_2_6(self):
        """Testing Ex 7.2.6"""
        self.assertIn('ex_7_2_6', dir(sp), 'Function to found')
        in_out_pairs = (
            ([1], 'Milk,Cottage,Tomatoes'),  # print list
            ([2], '3'),  # print list length
            ([3, 'Cottage'], 'True'),  # is given product in list
            ([3, 'Beer'], 'False'),
            ([4, 'Cottage'], '1'),  # count given product in list
            ([5, 'Cottage'], None),  # remove given product from list
            ([6, '7UP'], None),  # add given product to list
            ([6, '7UP'], None),
            ([4, '7UP'], '2'),
            ([6, 'GU'], None),
            ([7], '7UP,7UP,GU'),  # print all illegal products
            ([6, 'Milk'], None),
            ([1], 'Milk,Tomatoes,7UP,7UP,GU,Milk'),
            ([8], None),  # remove duplicates from list
            ([1], ['Milk', 'Tomatoes', '7UP', 'GU']),
            ([9], None),  # Exit
        )
        mock_inputs = [item for in_list in in_out_pairs for item in in_list[0]]
        mock_inputs.insert(0, "Milk,Cottage,Tomatoes")
        expected_out = [item[1] for item in in_out_pairs]

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            with patch('builtins.input', side_effect=mock_inputs):
                sp.ex_7_2_6()
        to_stdout: str = fake_stdout.getvalue()
        # print(f'\nstdout:\n{to_stdout}', file=sys.stderr)
        output = deque(to_stdout.split('\n'))
        for expected_line in expected_out:
            if expected_line is None:
                continue
            output_line = output.popleft().strip()
            if isinstance(expected_line, list):
                output_to_list = output_line.split(',')
                self.assertListEqual(sorted(output_to_list),
                                     sorted(expected_line))
            else:
                self.assertEqual(output_line, expected_line)

    def test_ex_7_2_7(self):
        """Testing arrow function"""
        self.assertIn('arrow', dir(sp), 'Function to found')
        cases = (
            (['#', 1], '#\n'),
            (['>', 2], '>\n>>\n>\n'),
            (['*', 5], '*\n**\n***\n****\n*****\n****\n***\n**\n*\n'),
        )
        for case in cases:
            self.assertEqual(sp.arrow(*case[0]), case[1])

    def test_ex_7_3_1(self):
        """Testing show_hidden_word function"""
        self.assertIn('show_hidden_word', dir(sp), 'Function to found')
        cases = (
            (["mammals", ['s', 'p', 'j', 'i', 'm', 'k']], 'm _ m m _ _ s'),
            (["amphibians", ['q', 'j', 'e', 't', 'k']], '_ _ _ _ _ _ _ _ _ _'),
            (["dog", []], '_ _ _'),
            (["banana", ['a', 'b', 'c', 'n']], 'b a n a n a'),
        )
        for case in cases:
            self.assertEqual(sp.show_hidden_word(*case[0]), case[1])

    def test_ex_7_3_2(self):
        """Testing check_win function"""
        self.assertIn('check_win', dir(sp), 'Function to found')
        cases = (
            (["mammals", ['s', 'p', 'j', 'i', 'm', 'k']], False),
            (["amphibians", ['q', 'j', 'e', 't', 'k']], False),
            (["dog", []], False),
            (["banana", ['a', 'b', 'c', 'n']], True),
        )
        for case in cases:
            self.assertEqual(sp.check_win(*case[0]), case[1])

    def test_ex_8_2_2(self):
        """Testing sort_prices function"""
        self.assertIn('sort_prices', dir(sp), 'Function to found')
        cases = (
            ([('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')],
             [('bread', '9.0'), ('milk', '5.5'), ('candy', '2.5')]),
            ([('milk', '-1.0'), ('candy', '-2.5'), ('bread', '9.0')],
             [('bread', '9.0'), ('milk', '-1.0'), ('candy', '-2.5')]),
        )
        for case in cases:
            self.assertEqual(sp.sort_prices(case[0]), case[1])

    def test_ex_8_2_3(self):
        """Testing mult_tuple function"""
        self.assertIn('mult_tuple', dir(sp), 'Function to found')
        cases = (
            ([(1, 2), (4, 5)],
             ((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))),
            ([(1, 2, 3), (4, 5, 6)],
             ((1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5),
              (3, 6), (4, 1), (5, 1), (6, 1), (4, 2), (5, 2), (6, 2), (4, 3),
              (5, 3), (6, 3))),
        )
        for case in cases:
            self.assertTupleEqual(
                tuple(sorted(sp.mult_tuple(*case[0]))),
                tuple(sorted(case[1]))
            )

    def test_ex_8_2_4(self):
        """Testing sort_anagrams function"""
        self.assertIn('sort_anagrams', dir(sp), 'Function to found')
        list_of_words = [
            'deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating',
            'ternaries', 'smelters', 'termless', 'salted', 'staled',
            'greatening', 'lasted', 'resmelts'
        ]
        expected = sorted([
            ['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'],
            ['retainers', 'ternaries'], ['pants'],
            ['generating', 'greatening'], ['smelters', 'termless', 'resmelts']
        ])
        self.assertListEqual(sorted(sp.sort_anagrams(list_of_words)), expected)

    @unittest.skip('To test Ex 8.3.2, comment this line')
    def test_ex_8_3_2(self):
        """Testing Ex 8.3.2"""
        self.assertIn('ex_8_3_2', dir(sp), 'Function to found')
        person = {
            'first_name': 'Mariah',
            'last_name': 'Carey',
            'birth_date': '27.03.1970',
            'hobbies': ['Sing', 'Compose', 'Act'],
        }
        cases = (
            (1, 'Carey', None),
            (2, 'March', None),
            (3, '3', None),
            (4, 'Act', None),
            (5, '', ('hobbies', 3, 'Cooking')),
            (6, '(27, 3, 1970)', None),
            (7, '50', ('age', None, '50')),
        )
        for case in cases:
            mock_inputs = [case[0]]
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                with patch('builtins.input', side_effect=mock_inputs):
                    sp.ex_8_3_2(person)
            to_stdout: str = fake_stdout.getvalue()
            found = to_stdout.strip()
            if case[1] != '':
                self.assertEqual(found.casefold(), case[1].casefold())

            if case[2] is not None:
                dict_check: tuple = case[2]
                found = person[dict_check[0]]
                if dict_check[1] is not None:
                    found = found[dict_check[1]]
                expected: str = dict_check[2]
                self.assertEqual(str(found).casefold(), expected.casefold())

    def test_ex_8_3_3(self):
        """Testing count_chars function"""
        self.assertIn('count_chars', dir(sp), 'Function to found')
        magic_str = "abra cadabra"
        expected = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
        self.assertDictEqual(sp.count_chars(magic_str), expected)

    def test_ex_8_3_4(self):
        """Testing inverse_dict function"""
        self.assertIn('inverse_dict', dir(sp), 'Function to found')
        course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
        expected = {3: ['I', 'love'], 2: ['self.py!']}
        self.assertDictEqual(sp.inverse_dict(course_dict), expected)

    def test_ex_8_4_1(self):
        """Testing print_hangman function"""
        self.assertIn('print_hangman', dir(sp), 'Function to found')
        # HANGMAN_ASCII_PHASE
        for miss in range(7):
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                sp.print_hangman(miss)
            to_stdout: str = fake_stdout.getvalue()
            cleaned_output = '\n'.join(
                [line.rstrip() for line in to_stdout.split('\n')
                 if line.strip() != '']
            )
            # print(f'\nto_stdout:\n{to_stdout}<<<\n'
            #       f'cleaned_output:\n{cleaned_output}<<<', file=sys.stderr)
            self.assertEqual(cleaned_output, HANGMAN_ASCII_PHASE[miss])


if __name__ == '__main__':
    unittest.main()
