"""Automatic tests for self.py course exercises.

These are unit tests for exercises from self.py course.
They cover most "open" exercises (code writing tasks) from units 5 to 9.
Course URL: https://campus.gov.il/course/course-v1-cs-gov_cs_selfpy101/

In addition there are 2 optional linter tests: style check (PEP-8) and
logical code checks. To use them, their linter modules should be
installed on your machine. This can be done by running::

    python -m pip install colorama pycodestyle pylint

**Usage:**
Create a new file named 'self.py' in same directory (as this file).
Write/copy your implementation of course exercises functions to this
file (self.py) and run the command blow (from same directory)::

    python test_self.py

Your python version should be 3.6+
More information at: https://github.com/izmirli/self.py_tester/
"""

__version__ = '2.1.1'

import unittest
from unittest.mock import patch
from io import StringIO
import os
import re
from collections import deque, defaultdict

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

# handle colors conditionally
try:
    import colorama
    colorama.init()
except ImportError:
    COLOR_FLAG = False
else:
    COLOR_FLAG = True


def style_me(text: str, style: str = 'white') -> str:
    """Add color and style to given text with ANSI escape character sequences.
    If colorama module isn't loaded, return given text as is.

    :param text: the text to be colored/styled.
    :param style: success/fail/warn/emphasize/illuminate or white (default).
    :return: the styled text with ANSI escape character sequences.
    """
    if not COLOR_FLAG:
        return text

    styled = '\033[1m'  # make it bold
    if style == 'success':
        styled += colorama.Fore.LIGHTGREEN_EX
    elif style == 'fail':
        styled += colorama.Fore.RED
    elif style == 'warn':
        styled += colorama.Fore.LIGHTMAGENTA_EX
    elif style == 'emphasize':
        styled += colorama.Fore.LIGHTCYAN_EX
    elif style == 'illuminate':
        styled += colorama.Fore.LIGHTYELLOW_EX
    else:
        styled += colorama.Fore.WHITE

    return styled + text + colorama.Style.RESET_ALL


class SelfPyTestCase(unittest.TestCase):
    """Test self.py course exercises"""

    def test_ex_5_3_4(self):
        """Testing last_early function"""
        if 'last_early' not in dir(sp):
            self.skipTest('Function last_early is missing')
        cases = (
            ("happy birthday", True),
            ("best of luck", False),
            ("Wow", True),
            ("X", False),
        )
        for case in cases:
            self.assertEqual(sp.last_early(case[0]), case[1],
                             f'Failed on "{case[0]}"')

    def test_ex_5_3_5(self):
        """Testing distance function"""
        if 'distance' not in dir(sp):
            self.skipTest('Function distance is missing')
        cases = (
            ([1, 2, 10], True),
            ([4, 5, 3], False),
            ([1, 2, 3], False),
        )
        for case in cases:
            self.assertEqual(
                sp.distance(*case[0]), case[1],
                f'Failed on: num1={case[0][0]}, '
                f'num2={case[0][1]}, num3={case[0][2]}'
            )

    def test_ex_5_3_6(self):
        """Testing filter_teens function"""
        if 'filter_teens' not in dir(sp):
            self.skipTest('Function filter_teens is missing')
        cases = (
            ([], 0, 'no args, default arguments should be used'),
            ([20], 20, 'one grownup (20), missing 2 args - default teen ages'),
            ([1, 2, 3], 6, 'all my children < 13 (1, 2, 3)'),
            ([2, 13, 1], 3, '2 kids, one teen (2, 13, 1)'),
            ([2, 1, 15], 18, '2 kids, one special teen (2, 1, 15)'),
        )
        for case in cases:
            self.assertEqual(sp.filter_teens(*case[0]), case[1], case[2])

    def test_ex_5_3_7(self):
        """Testing chocolate_maker function"""
        if 'chocolate_maker' not in dir(sp):
            self.skipTest('Function chocolate_maker is missing')
        cases = (
            ([3, 1, 8], True),
            ([3, 1, 9], False),
            ([3, 2, 9], False),
            ([3, 2, 10], True),
            ([0, 2, 10], True),
            ([10, 0, 10], True),
        )
        for case in cases:
            self.assertEqual(
                sp.chocolate_maker(*case[0]), case[1],
                f'Failed on: small={case[0][0]}, big={case[0][1]}, '
                f'x={case[0][2]}'
            )

    def test_ex_5_4_1(self):
        """Testing func function for its docstring"""
        if 'func' not in dir(sp):
            self.skipTest('Function func is missing')
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            help(sp.func)
            output = fake_stdout.getvalue()
        # print(f'output:\n{output}\n---', sys.stderr)
        self.assertRegex(output, r'func\(num1, num2\)\n[ \t]+\w+[^\n]{7}',
                         'no func description (at least 8 characters)')
        self.assertRegex(output, r':param num1:[ \t]+\w+', 'num1 description')
        self.assertRegex(output, r':param num2:[ \t]+\w+', 'num2 description')
        self.assertRegex(output, r':type num1:[ \t]+\w+\n', 'no num1 type')
        self.assertRegex(output, r':type num2:[ \t]+\w+\n', 'no num2 type')
        self.assertRegex(output, r':return:[ \t]+\w+', 'no return description')
        self.assertRegex(output, r':rtype:[ \t]+\w+\n', 'no return type')

    def test_ex_5_5_1(self):
        """Testing is_valid_input function"""
        if 'is_valid_input' not in dir(sp):
            self.skipTest('Function is_valid_input is missing')
        cases = (
            ('a', True, 'a is valid'),
            ('A', True, 'A is valid'),
            ('$', False, '$ is invalid'),
            ('ab', False, '"ab" is invalid'),
            ('app$', False, '"app$" is invalid'),
            ('', False, '"" (empty string) is invalid'),
            ('א', False, 'א (Hebrew Alef) is invalid'),
        )
        for case in cases:
            self.assertEqual(sp.is_valid_input(case[0]), case[1], case[2])

    def test_ex_6_1_2(self):
        """Testing shift_left function"""
        if 'shift_left' not in dir(sp):
            self.skipTest('Function shift_left is missing')
        cases = (
            ([0, 1, 2], [1, 2, 0]),
            (['monkey', 2.0, 1], [2.0, 1, 'monkey']),
        )
        for case in cases:
            self.assertEqual(sp.shift_left(case[0]), case[1],
                             f'original list: {case[0]}')

    def test_ex_6_2_3(self):
        """Testing format_list function"""
        if 'format_list' not in dir(sp):
            self.skipTest('Function format_list is missing')
        cases = (
            (["hydrogen", "helium", "lithium", "beryllium", "boron",
              "magnesium"], 'hydrogen, lithium, boron and magnesium'),
            (["hydrogen", "helium"], 'hydrogen and helium'),
        )
        for case in cases:
            self.assertEqual(sp.format_list(case[0]), case[1],
                             f'original list: {case[0]}')

    def test_ex_6_2_4(self):
        """Testing extend_list_x function"""
        if 'extend_list_x' not in dir(sp):
            self.skipTest('Function extend_list_x is missing')
        cases = (
            ([[4, 5, 6], [1, 2, 3]], [1, 2, 3, 4, 5, 6]),
            ([[2], [1]], [1, 2]),
            ([['one', 1], [1, 'one']], [1, 'one', 'one', 1]),
            ([[7, 7, 7, 7, 7, 7, 7], [0, 1, 2, 3, 4]],
             [0, 1, 2, 3, 4, 7, 7, 7, 7, 7, 7, 7]),
        )
        for case in cases:
            self.assertEqual(
                sp.extend_list_x(case[0][0].copy(), case[0][1].copy()),
                case[1],
                f'original lists: {case[0]}'
            )

    def test_ex_6_3_1(self):
        """Testing are_lists_equal function"""
        if 'are_lists_equal' not in dir(sp):
            self.skipTest('Function are_lists_equal is missing')
        list1 = [0.6, 1, 2, 3]
        list2 = [3, 2, 0.6, 1]
        list3 = [9, 0, 5, 10.5]
        self.assertEqual(sp.are_lists_equal(list1, list2), True,
                         f'list1={list1}, list2={list2} should be equal')
        self.assertEqual(sp.are_lists_equal(list1, list3), False,
                         f'list1={list1}, list2={list3} should NOT be equal')

    def test_ex_6_3_2(self):
        """Testing longest function"""
        if 'longest' not in dir(sp):
            self.skipTest('Function longest is missing')
        cases = (
            (["111", "234", "2000", "goru", "birthday", "09"], "birthday"),
            (["nanu", "nanu", "mork", "and", "Williams", "mindy", "Robin"],
             "Williams"),
        )
        for case in cases:
            self.assertEqual(sp.longest(case[0]), case[1],
                             f'list was: {case[0]}')

    def test_ex_6_4_1(self):
        """Testing check_valid_input function"""
        if 'check_valid_input' not in dir(sp):
            self.skipTest('Function check_valid_input is missing')
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
        if 'try_update_letter_guessed' not in dir(sp):
            self.skipTest('Function try_update_letter_guessed is missing')
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
                return_value = sp.try_update_letter_guessed(case[0], case[1])
                output = fake_stdout.getvalue()
                # print(f'rv: {return_value}; output: {output}; '
                #       f'output == case[2] {output == case[2]}; '
                #       f'rv == case[3] {return_value == case[3]}',
                #       file=sys.stderr)
                self.assertTrue(output == case[2] and
                                return_value == case[3], case[4])

    def test_ex_7_1_4(self):
        """Testing squared_numbers function"""
        if 'squared_numbers' not in dir(sp):
            self.skipTest('Function squared_numbers is missing')
        cases = (
            (4, 8, [16, 25, 36, 49, 64]),
            (-3, 3, [9, 4, 1, 0, 1, 4, 9]),
        )
        for case in cases:
            self.assertEqual(sp.squared_numbers(case[0], case[1]), case[2],
                             f'start={case[0]}, stop={case[1]}')

    def test_ex_7_2_1(self):
        """Testing is_greater function"""
        if 'is_greater' not in dir(sp):
            self.skipTest('Function is_greater is missing')
        base_list = [1, 30, 25, 60, 27, 28]
        cases = (
            ([base_list, 28], [30, 60], 'return 2 out of 6'),
            ([base_list, 0], [1, 30, 25, 60, 27, 28], 'return all 6'),
            ([base_list, 60], [], 'return empty'),
        )
        for case in cases:
            self.assertEqual(sorted(sp.is_greater(*case[0])), sorted(case[1]),
                             f'list={base_list}, n={case[0][1]}')

    def test_ex_7_2_2(self):
        """Testing numbers_letters_count function"""
        if 'numbers_letters_count' not in dir(sp):
            self.skipTest('Function numbers_letters_count is missing')
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
        if 'seven_boom' not in dir(sp):
            self.skipTest('Function seven_boom is missing')
        self.assertEqual(
            sp.seven_boom(17),
            ['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM',
             15, 16, 'BOOM']
        )

    def test_ex_7_2_5(self):
        """Testing sequence_del function"""
        if 'sequence_del' not in dir(sp):
            self.skipTest('Function sequence_del is missing')
        cases = (
            ('ppyyyyythhhhhooonnnnn', 'python'),
            ('SSSSsssshhhh', 'Ssh'),
            ('Heeyyy   yyouuuu!!!', 'Hey you!'),
        )
        for case in cases:
            self.assertEqual(sp.sequence_del(case[0]), case[1])

    @unittest.skip('Disabled. Enable by commenting this line.')
    def test_ex_7_2_6(self):
        """Testing Ex 7.2.6"""
        if 'ex_7_2_6' not in dir(sp):
            self.skipTest('Function ex_7_2_6 is missing')
        in_out_pairs = (
            (['1'], 'Milk,Cottage,Tomatoes'),  # print list
            (['2'], '3'),  # print list length
            (['3', 'Cottage'], 'True'),  # is given product in list
            (['3', 'Beer'], 'False'),
            (['4', 'Cottage'], '1'),  # count given product in list
            (['5', 'Cottage'], None),  # remove given product from list
            (['6', '7UP'], None),  # add given product to list
            (['6', '7UP'], None),
            (['4', '7UP'], '2'),
            (['6', 'GU'], None),
            (['7'], '7UP,7UP,GU'),  # print all illegal products
            (['6', 'Milk'], None),
            (['1'], 'Milk,Tomatoes,7UP,7UP,GU,Milk'),
            (['8'], None),  # remove duplicates from list
            (['1'], ['Milk', 'Tomatoes', '7UP', 'GU']),
            (['9'], None),  # Exit
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
        action_count = -1
        for expected_line in expected_out:
            action_count += 1
            if expected_line is None:
                continue
            output_line = output.popleft().strip()
            if isinstance(expected_line, list):
                output_to_list = output_line.split(',')
                self.assertListEqual(
                    sorted(output_to_list), sorted(expected_line),
                    f'Action#{in_out_pairs[action_count][0][0]} '
                    f'(Test#{action_count}).'
                )
            else:
                self.assertEqual(
                    output_line, expected_line,
                    f'Action#{in_out_pairs[action_count][0][0]}; '
                    f'(Test#{action_count}).'
                )

    def test_ex_7_2_7(self):
        """Testing arrow function"""
        if 'arrow' not in dir(sp):
            self.skipTest('Function arrow is missing')
        cases = (
            (['*', 5], '*\n**\n***\n****\n*****\n****\n***\n**\n*'),
            (['>', 2], '>\n>>\n>'),
            (['#', 1], '#'),
        )
        for case in cases:
            self.assertEqual(sp.arrow(*case[0]), case[1],
                             f'char={case[0][0]}, len={case[0][1]}')

    def test_ex_7_3_1(self):
        """Testing show_hidden_word function"""
        if 'show_hidden_word' not in dir(sp):
            self.skipTest('Function show_hidden_word is missing')
        cases = (
            (["mammals", ['s', 'p', 'j', 'i', 'm', 'k']], 'm _ m m _ _ s'),
            (["amphibians", ['q', 'j', 'e', 't', 'k']], '_ _ _ _ _ _ _ _ _ _'),
            (["dog", []], '_ _ _'),
            (["banana", ['a', 'b', 'c', 'n']], 'b a n a n a'),
        )
        for case in cases:
            self.assertEqual(sp.show_hidden_word(*case[0]), case[1],
                             f'word={case[0][0]}, old_letters={case[0][1]}')

    def test_ex_7_3_2(self):
        """Testing check_win function"""
        if 'check_win' not in dir(sp):
            self.skipTest('Function check_win is missing')
        cases = (
            (["mammals", ['s', 'p', 'j', 'i', 'm', 'k']], False),
            (["amphibians", ['q', 'j', 'e', 't', 'k']], False),
            (["dog", []], False),
            (["banana", ['a', 'b', 'c', 'n']], True),
        )
        for case in cases:
            self.assertEqual(sp.check_win(*case[0]), case[1],
                             f'word={case[0][0]}, old_letters={case[0][1]}')

    def test_ex_8_2_2(self):
        """Testing sort_prices function"""
        if 'sort_prices' not in dir(sp):
            self.skipTest('Function sort_prices is missing')
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
        if 'mult_tuple' not in dir(sp):
            self.skipTest('Function mult_tuple is missing')
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
                tuple(sorted(case[1])),
                f'tuple1: {case[0][0]}, tuple2: {case[0][1]}'
            )

    def test_ex_8_2_4(self):
        """Testing sort_anagrams function"""
        if 'sort_anagrams' not in dir(sp):
            self.skipTest('Function sort_anagrams is missing')
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

    @unittest.skip('Disabled. Enable by commenting this line.')
    def test_ex_8_3_2(self):
        """Testing Ex 8.3.2"""
        if 'ex_8_3_2' not in dir(sp):
            self.skipTest('Function ex_8_3_2 is missing')
        person = {
            'first_name': 'Mariah',
            'last_name': 'Carey',
            'birth_date': '27.03.1970',
            'hobbies': ['Sing', 'Compose', 'Act'],
        }
        cases = (
            ('1', 'Carey', None, 'Last name'),
            ('2', ('march', 'mar', '3', '03'), None, 'Month of birth'),
            ('3', '3', None, 'Number of hobbies'),
            ('4', 'Act', None, 'Last hobby'),
            ('5', '', ('hobbies', 3, 'Cooking'), 'Add Cooking as a new hobby'),
            ('6', '(27, 3, 1970)', None, 'Birth date tuple'),
            ('7', '50', ('age', None, '50'), 'Add age'),
        )
        for case in cases:
            mock_inputs = [case[0]]
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                with patch('builtins.input', side_effect=mock_inputs):
                    sp.ex_8_3_2(person)
            to_stdout: str = fake_stdout.getvalue()
            found = to_stdout.strip()
            if isinstance(case[1], tuple):
                self.assertIn(found.casefold(), case[1],
                              f'Action#{case[0]} {case[3]}')
            elif case[1] != '':
                self.assertEqual(found.casefold(), case[1].casefold(),
                                 f'Action#{case[0]} {case[3]}')

            if case[2] is not None:
                dict_check: tuple = case[2]
                found = person[dict_check[0]]
                if dict_check[1] is not None:
                    found = found[dict_check[1]]
                expected: str = dict_check[2]
                self.assertEqual(str(found).casefold(), expected.casefold(),
                                 f'Action#{case[0]} {case[3]}')

    def test_ex_8_3_3(self):
        """Testing count_chars function"""
        if 'count_chars' not in dir(sp):
            self.skipTest('Function count_chars is missing')
        magic_str = "abra cadabra"
        expected = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
        self.assertDictEqual(sp.count_chars(magic_str), expected,
                             f'my_str: "{magic_str}"')

    def test_ex_8_3_4(self):
        """Testing inverse_dict function"""
        if 'inverse_dict' not in dir(sp):
            self.skipTest('Function inverse_dict is missing')
        cases = (
            ({'I': 3, 'love': 3, 'self.py!': 2},
             {3: ['I', 'love'], 2: ['self.py!']}, 'Course example'),
            ({'k5': 'v3', 'k1': 'v1', 'k2': 'v3', 'k3': 'v3', 'k4': 'v3'},
             {'v3': ['k2', 'k3', 'k4', 'k5'], 'v1': ['k1']}, 'sorting'),
        )
        for case in cases:
            self.assertDictEqual(sp.inverse_dict(case[0]), case[1], case[2])

    def test_ex_8_4_1(self):
        """Testing print_hangman function"""
        if 'print_hangman' not in dir(sp):
            self.skipTest('Function print_hangman is missing')
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
            self.assertEqual(cleaned_output, HANGMAN_ASCII_PHASE[miss],
                             f'num_of_tries: {miss}')

    def test_ex_9_1_1(self):
        """Testing are_files_equal function"""
        if 'are_files_equal' not in dir(sp):
            self.skipTest('Function are_files_equal is missing')

        cases = (
            ('f01.txt', 'f02.txt', False, 'unequal files'),
            ('f01.txt', 'f03.txt', True, 'equal files'),
        )
        for case in cases:
            outcome = sp.are_files_equal(os.path.abspath(case[0]),
                                         os.path.abspath(case[1]))
            self.assertTrue(outcome == case[2], case[3])

    @unittest.skip('Disabled. Enable by commenting this line.')
    def test_ex_9_1_2(self):
        """Testing Ex 9.1.2"""
        if 'ex_9_1_2' not in dir(sp):
            self.skipTest('Function ex_9_1_2 is missing')

        words_file = os.path.abspath('f04.txt')
        cases = (
            (['sort'],
             "['about', 'and', 'away', 'believe', 'can', 'day', "
             "'every', 'fly', 'i', 'it', 'my', 'night', 'sky', "
             "'spread', 'the', 'think', 'touch', 'wings']",
             'checking sort'),
            (['rev'], """ylf nac i eveileb i
yks eht hcuot nac i eveileb i
yad dna thgin yreve ti tuoba kniht i
yawa ylf dna sgniw ym daerps""", 'checking rev'),
            (['last', 2], 'i think about it every night and day\n'
                          'spread my wings and fly away', 'checking last'),
        )
        for case in cases:
            mock_inputs = [words_file, *case[0]]
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                with patch('builtins.input', side_effect=mock_inputs):
                    sp.ex_9_1_2()
            to_stdout: str = fake_stdout.getvalue()
            found = to_stdout.strip()
            self.assertEqual(found, case[1], case[2])

    def test_ex_9_2_2(self):
        """Testing copy_file_content function"""
        if 'copy_file_content' not in dir(sp):
            self.skipTest('Function copy_file_content is missing')
        source = os.path.abspath('f01.txt')
        destination = os.path.abspath('f05.txt')
        with open(source, 'r') as file_handle:
            source_content = file_handle.read()
        sp.copy_file_content(source, destination)
        with open(destination, 'r') as file_handle:
            destination_content = file_handle.read()
        with open(destination, 'w') as file_handle:
            file_handle.write(
                '-- And Now for Something Completely Different --'
            )
        self.assertEqual(source_content, destination_content)

    def test_ex_9_2_3(self):
        """Testing who_is_missing function"""
        if 'who_is_missing' not in dir(sp):
            self.skipTest('Function who_is_missing is missing')
        source = os.path.abspath('f02.txt')
        expected = 5
        destination = os.path.abspath('found.txt')
        return_value = sp.who_is_missing(source)
        with open(destination, 'r') as file_handle:
            destination_content = file_handle.readline().strip()
        os.unlink(destination)
        self.assertIs(return_value, expected,
                      'Return value is not as expected.')
        self.assertEqual(destination_content, str(expected))

    def test_ex_9_3_1(self):
        """Testing my_mp3_playlist function"""
        if 'my_mp3_playlist' not in dir(sp):
            self.skipTest('Function my_mp3_playlist is missing')
        source = os.path.abspath('f06.txt')
        self.assertEqual(
            sp.my_mp3_playlist(source),
            ("Tudo Bom", 5, "The Black Eyed Peas")
        )

    def test_ex_9_3_2(self):
        """Testing my_mp4_playlist function"""
        if 'my_mp4_playlist' not in dir(sp):
            self.skipTest('Function my_mp4_playlist is missing')
        cases = (
            (os.path.abspath('f06.txt'),
             """Tudo Bom;Static and Ben El Tavori;5:13;
I Gotta Feeling;The Black Eyed Peas;4:05;
Python Love Story;Unknown;4:15;
Paradise;Coldplay;4:23;
Where is the love?;The Black Eyed Peas;4:13;""",
             '5-lines file',
             """Tudo Bom;Static and Ben El Tavori;5:13;
I Gotta Feeling;The Black Eyed Peas;4:05;
Instrumental;Unknown;4:15;
Paradise;Coldplay;4:23;
Where is the love?;The Black Eyed Peas;4:13;
"""),
            (os.path.abspath('f07.txt'),
             'Always Look On The Bright Side Of Life;Monty Python;3:23;\n\n'
             'Python Love Story',
             '1-line file',
             'Always Look On The Bright Side Of Life;Monty Python;3:23;\n'),
        )
        for case in cases:
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                sp.my_mp4_playlist(case[0], "Python Love Story")
            to_stdout: str = fake_stdout.getvalue()
            with open(case[0], 'r') as file_handle:
                file_content = file_handle.read()
            with open(case[0], 'w') as file_handle:
                file_handle.write(case[3])
            self.assertEqual(to_stdout.strip(), case[1], f'stdout {case[2]}')
            self.assertEqual(file_content.strip(), case[1],
                             f'content {case[2]}')

    def test_ex_9_4_1(self):
        """Testing choose_word function"""
        if 'choose_word' not in dir(sp):
            self.skipTest('Function choose_word is missing')
        source = os.path.abspath('f01.txt')
        cases = (
            (1, (90, 'Beautiful'), 'first word'),
            (3, (90, 'better'), 'word in middle of 1st line'),
            (52, (90, 'explicitly'), 'word in middle of file'),
            (220, (90, 'obvious'), 'wrap index'),
        )
        for case in cases:
            self.assertTupleEqual(
                sp.choose_word(source, case[0]), case[1], case[2]
            )

    @unittest.skip('Disabled. Enable pycodestyle by commenting this line.')
    def test_pycodestyle(self):
        """Test that your code conform to PEP-8."""
        try:
            import pycodestyle
        except ImportError as ex:
            self.skipTest(f'{ex}. Run "pip install pycodestyle" '
                          f'to use this test.')
        style = pycodestyle.StyleGuide(
            repeat=False,  # show just the first occurrence of each error.
            show_pep8=True,  # show the relevant text of PEP 8 for each error.
            show_source=True,  # show source code for each error.
            statistics=True,  # [Not working here] count errors and warnings.
        )
        result = style.check_files(['self.py'])
        self.assertEqual(
            result.total_errors, 0,
            f"Found {result.total_errors} code style errors (and warnings)."
        )

    @unittest.skip('Disabled. Enable pylint by commenting this line.')
    def test_pylint(self):
        """Lint your code to find programming errors and more."""
        try:
            from pylint import epylint as lint
        except ImportError as ex:
            self.skipTest(f'{ex}. Run "pip install pylint" to use this test.')

        (pylint_out, _) = lint.py_run('self.py', return_std=True)

        output: str = pylint_out.getvalue()
        rating = ''
        messages = {}
        for line in output.split('\n'):
            # self.py:85: convention (C0116, missing-function-docstring,
            # ex_4_2_2) Missing function or method docstring
            match = re.search(r'self\.py:(\d+): (\w+) \(([A-Z]\d+), (\S+), '
                              r'(\S+)?\) (\w.+)\s*$', line, re.IGNORECASE)
            if match:
                (l_num, l_type, l_code, l_short_msg, l_func, l_long_msg) = \
                    match.group(1, 2, 3, 4, 5, 6)
                if l_code not in messages:
                    messages[l_code] = {
                        'line': l_num, 'type': l_type, 'code': l_code,
                        'short_msg': l_short_msg, 'func': l_func,
                        'long_msg': l_long_msg
                    }
                    continue

            match = re.search(r'Your code .* (1?\d(?:\.\d+)?)/10', line)
            if match:
                rating = match.group(1)

        if len(messages) >= 1:
            print(f'rating: {rating}/10\n\n'
                  f'Problems found (show first occurrence of each type):')
            for msg in messages.values():
                func = f'::{msg["func"]}' if msg["func"] else ""
                print(f'[Line#{msg["line"]}{func}] '
                      f'[{msg["type"]}::{msg["code"]}] '
                      f'{msg["long_msg"]}')
        self.assertGreater(
            float(rating), 9.85, 'Your code\'s pylint rating is too low'
        )


class CustomTestResult(unittest.runner.TextTestResult):
    """Override default TextTestResult to add printout & count outcomes."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_count = defaultdict(int)
        self.missing_exercises = []

    def get_custom_count(self):
        """Retrieve the custom count."""
        return self.custom_count

    def get_missing_exercises_list(self):
        """Retrieve the missing exercises list."""
        return self.missing_exercises

    def addSuccess(self, test: unittest.case.TestCase) -> None:
        ex_display = self.get_test_display_name(test)
        print(f'{ex_display}: ' + style_me('OK', 'success'))
        self.custom_count["success"] += 1
        super().addSuccess(test)

    def addFailure(self, test: unittest.case.TestCase, err) -> None:
        ex_display = self.get_test_display_name(test)
        self.custom_count["problems"] += 1
        # exception_type, exception_value, exception_tb = err
        exception_value = err[1]
        print(f'{style_me(ex_display)}: {style_me("FAIL", "fail")}')
        print(style_me('---\n' + str(exception_value) + '\n---', "fail"))
        super().addFailure(test, err)

    def addError(self, test: unittest.case.TestCase, err) -> None:
        ex_display = self.get_test_display_name(test)
        self.custom_count["problems"] += 1
        exception_value = err[1]
        print(f'{style_me(ex_display)}: {style_me("ERROR", "fail")}')
        print(style_me('---\n' + str(exception_value) + '\n---', "fail"))
        super().addError(test, err)

    def addSkip(self, test: unittest.case.TestCase, reason: str) -> None:
        ex_display = self.get_test_display_name(test)
        if re.search(r'Disabled', reason, re.IGNORECASE):
            pass
            # print(f'{ex_display}: Disabled (advanced users can read '
            #       f'documentaion to enable)')
        elif re.search(r'Function .+ missing', reason, re.IGNORECASE):
            self.custom_count["missing"] += 1
            self.missing_exercises.append(ex_display[9:])
        else:
            print(f'{ex_display}: {style_me(reason, "warn")}')

        super().addSkip(test, reason)

    def printErrors(self) -> None:
        """Abort errors/fails printout."""
        return

    @staticmethod
    def get_test_display_name(test: unittest.case.TestCase) -> str:
        """Extract, process and return display name from test.

        :param test: the TestCase object to retreive the info from.
        :return: display name string.
        """
        t_name = test.id()
        match = re.search(r'test_(?:ex_(\d)_(\d)_(\d)|(\w+))\s*$', t_name)
        if match and match.group(1) is not None:
            t_name = f'Exercise {match.group(1)}.{match.group(2)}' \
                     f'.{match.group(3)}'
        elif match and match.group(4) is not None:
            t_name = match.group(4)
        description = test.shortDescription()
        match = re.search(r'Testing (\w+) function', description, re.I)
        if match:
            t_name += f' ({match.group(1)})'
        elif not re.search(r'Testing Ex \d\.\d\.\d', description):
            t_name += f' ({description[:-1]})'

        return t_name


class CustomTestRunner(unittest.TextTestRunner):
    """Override default TextTestRunner result class & run method for
    custom display.
    """

    def __init__(self, *args, **kwargs):
        """Override result class to CustomTestResult & mo verbosity"""
        super().__init__(resultclass=CustomTestResult, verbosity=0,
                         *args, **kwargs)

    def run(self, test) -> unittest.result.TestResult:
        """Override by adding custom output to the end."""
        result = super().run(test)
        custom_count = result.get_custom_count()
        missing_exercises = result.get_missing_exercises_list()

        if custom_count["problems"] > 0:
            print(style_me(
                f'{custom_count["problems"]:2} exercises have problems',
                'fail'
            ))

        print(style_me(
            f'{custom_count["success"]:2} exercises done successfully',
            'success' if custom_count["success"] > 0 else 'white'
        ))

        if custom_count["missing"] > 0:
            print(style_me(
                f'{custom_count["missing"]:2} exercises left to do',
                'emphasize'
            ))
            print('\tNext exercises:', ', '.join(missing_exercises[:3]))

        if custom_count["problems"] == 0 and custom_count["missing"] == 0:
            print('\n' + style_me(f'{"Grate Job!":^60}', 'emphasize'))
            if custom_count["success"] >= 36:
                positive_reinforcement = \
                    "You are an advanced programmer going above and beyond"
                print(style_me(
                    f'{positive_reinforcement:^60}', 'illuminate'
                ))
            elif custom_count["success"] > 33:
                print(style_me(
                    f'{"You did more and I like it!":^60}', 'illuminate'
                ))
            if custom_count["success"] >= 38:
                positive_reinforcement = \
                    '>'*10 + " You have mastered self.py exercises " + '<'*10
                print(style_me(f'{positive_reinforcement:^60}', 'warn'))

        return result


if __name__ == '__main__':
    test_runner = CustomTestRunner()
    unittest.main(testRunner=test_runner)
