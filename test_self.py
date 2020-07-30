"""Automatic tests for self.py course.

Course URL: https://campus.gov.il/course/course-v1-cs-gov_cs_selfpy101/
"""
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
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
        if 'last_early' not in dir(sp):
            self.skipTest('Function last_early is missing')
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
        if 'distance' not in dir(sp):
            self.skipTest('Function distance is missing')
        cases = (
            ([1, 2, 10], True),
            ([4, 5, 3], False),
            ([1, 2, 3], False),
        )
        for case in cases:
            self.assertEqual(sp.distance(*case[0]), case[1])

    def test_ex_5_3_6(self):
        """Testing filter_teens function"""
        if 'filter_teens' not in dir(sp):
            self.skipTest('Function filter_teens is missing')
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
            self.assertEqual(sp.chocolate_maker(*case[0]), case[1])

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
            ('א', False, 'א is invalid'),
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
            self.assertEqual(sp.shift_left(case[0]), case[1])

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
            self.assertEqual(sp.format_list(case[0]), case[1])

    def test_ex_6_2_4(self):
        """Testing extend_list_x function"""
        if 'extend_list_x' not in dir(sp):
            self.skipTest('Function extend_list_x is missing')
        cases = (
            ([[4, 5, 6], [1, 2, 3]], [1, 2, 3, 4, 5, 6]),
        )
        for case in cases:
            self.assertEqual(sp.extend_list_x(*case[0]), case[1])

    def test_ex_6_3_1(self):
        """Testing are_lists_equal function"""
        if 'are_lists_equal' not in dir(sp):
            self.skipTest('Function are_lists_equal is missing')
        list1 = [0.6, 1, 2, 3]
        list2 = [3, 2, 0.6, 1]
        list3 = [9, 0, 5, 10.5]
        self.assertEqual(sp.are_lists_equal(list1, list2), True)
        self.assertEqual(sp.are_lists_equal(list1, list3), False)

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
            self.assertEqual(sp.longest(case[0]), case[1])

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
                rv = sp.try_update_letter_guessed(case[0], case[1])
                op = fake_stdout.getvalue()
                # print(f'rv: {rv}; op: {op}; op == case[2] {op == case[2]}; '
                #       f'rv == case[3] {rv == case[3]}', file=sys.stderr)
                self.assertTrue(op == case[2] and rv == case[3], case[4])

    def test_ex_7_1_4(self):
        """Testing squared_numbers function"""
        if 'squared_numbers' not in dir(sp):
            self.skipTest('Function squared_numbers is missing')
        cases = (
            (4, 8, [16, 25, 36, 49, 64]),
            (-3, 3, [9, 4, 1, 0, 1, 4, 9]),
        )
        for case in cases:
            self.assertEqual(sp.squared_numbers(case[0], case[1]), case[2])

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
            self.assertEqual(sorted(sp.is_greater(*case[0])), sorted(case[1]))

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

    @unittest.skip('To test Ex 7.2.6, comment this line')
    def test_ex_7_2_6(self):
        """Testing Ex 7.2.6"""
        if 'ex_7_2_6' not in dir(sp):
            self.skipTest('Function ex_7_2_6 is missing')
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
        if 'arrow' not in dir(sp):
            self.skipTest('Function arrow is missing')
        cases = (
            (['#', 1], '#\n'),
            (['>', 2], '>\n>>\n>\n'),
            (['*', 5], '*\n**\n***\n****\n*****\n****\n***\n**\n*\n'),
        )
        for case in cases:
            self.assertEqual(sp.arrow(*case[0]), case[1])

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
            self.assertEqual(sp.show_hidden_word(*case[0]), case[1])

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
            self.assertEqual(sp.check_win(*case[0]), case[1])

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
                tuple(sorted(case[1]))
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

    @unittest.skip('To test Ex 8.3.2, comment this line')
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
        if 'count_chars' not in dir(sp):
            self.skipTest('Function count_chars is missing')
        magic_str = "abra cadabra"
        expected = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
        self.assertDictEqual(sp.count_chars(magic_str), expected)

    def test_ex_8_3_4(self):
        """Testing inverse_dict function"""
        if 'inverse_dict' not in dir(sp):
            self.skipTest('Function inverse_dict is missing')
        course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
        expected = {3: ['I', 'love'], 2: ['self.py!']}
        self.assertDictEqual(sp.inverse_dict(course_dict), expected)

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
            self.assertEqual(cleaned_output, HANGMAN_ASCII_PHASE[miss])

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

    @unittest.skip('To check Ex 9.2.1, comment this line.')
    def test_ex_9_1_2(self):
        """Testing Ex 9.1.2"""
        if 'ex_9_1_2' not in dir(sp):
            self.skipTest('Function ex_9_1_2 is missing')

        words_file = os.path.abspath('f04.txt')
        cases = (
            (['sort'], "['about', 'and', 'away', 'believe', 'can', 'day', "
                       "'every', 'fly', 'i', 'it', 'my', 'night', 'sky', "
                       "'spread', 'the', 'think', 'touch', 'wings']"),
            (['rev'], """ylf nac i eveileb i
yks eht hcuot nac i eveileb i
yad dna thgin yreve ti tuoba kniht i
yawa ylf dna sgniw ym daerps"""),
            (['last', 2], 'i think about it every night and day\n'
                          'spread my wings and fly away'),
        )
        for case in cases:
            mock_inputs = [words_file, *case[0]]
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                with patch('builtins.input', side_effect=mock_inputs):
                    sp.ex_9_1_2()
            to_stdout: str = fake_stdout.getvalue()
            found = to_stdout.strip()
            self.assertEqual(found, case[1])

    def test_ex_9_2_2(self):
        """Testing copy_file_content function"""
        if 'copy_file_content' not in dir(sp):
            self.skipTest('Function copy_file_content is missing')
        source = os.path.abspath('f01.txt')
        destination = os.path.abspath('f05.txt')
        with open(source, 'r') as fh:
            source_content = fh.read()
        sp.copy_file_content(source, destination)
        with open(destination, 'r') as fh:
            dest_content = fh.read()
        with open(destination, 'w') as fh:
            fh.write('-- And Now for Something Completely Different --')
        self.assertEqual(source_content, dest_content)

    @unittest.skip('To check your Python code against PEP-8 '
                   'style conventions, comment this line.')
    def test_pycodestyle(self):
        """"Test that your code conform to PEP-8."""
        try:
            import pycodestyle
        except ImportError as ex:
            print(f'ImportError data: ', file=sys.stderr)
            self.skipTest(f'{ex}. Run "pip install pycodestyle" before to '
                          'use this test.')
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


if __name__ == '__main__':
    unittest.main()
