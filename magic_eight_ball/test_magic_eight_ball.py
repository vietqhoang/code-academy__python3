'Unit tests for magic_eight_ball'

import re
from math import ceil
from unittest import TestCase, skip
from unittest.mock import patch
from magic_eight_ball import ask_question

class TestMagicEightBallAskQuestion(TestCase):
    'Tests for `ask_question`'

    POSSIBLE_ANSWERS = [
        'Ask again later.',
        'Better not tell you now.',
        'It is decidedly so.',
        'My sources say no.',
        'Outlook not so good.',
        'Reply hazy, try again.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes - definitely.'
    ]
    REGEX_ESCAPED_POSSIBLE_ANSWERS = (
        rf'('
        rf'{"|".join([re.escape(answer) for answer in POSSIBLE_ANSWERS])}'
        rf')'
    )

    def setUp(self):
        self.subject = ask_question

    @patch('magic_eight_ball._input_name', return_value = 'Viet')
    @patch('magic_eight_ball._input_question', return_value = 'Is the sky blue?')
    def test_ask_question(self, _input_name, _input_question):
        (
            'When name and question are inputted, '
            'it is expected to output a string with '
            'the name, question, and random Magic Eight Ball answer'
        )

        expected_answer = (
            rf'^\n'
            rf'Viet asks: Is the sky blue\?\n'
            rf'Magic 8-Ball’s answer: {self.REGEX_ESCAPED_POSSIBLE_ANSWERS}$'
        )

        # NOTE: Given there are 9 answers, the probability of having each answer to appear
        # once is (9/9)+(9/8)+(9/7)+(9/6)+(9/5)+(9/4)+(9/3)+(9/2)+(9/1) = 25.46
        number_of_runs = ceil(
            sum(
                [(len(self.POSSIBLE_ANSWERS) / (x + 1)) for x in range(len(self.POSSIBLE_ANSWERS))]
            )
        )

        for _ in range(number_of_runs):
            self.assertRegex(
                self.subject(),
                expected_answer
            )

    @patch('magic_eight_ball._input_name', return_value = '')
    @patch('magic_eight_ball._input_question', return_value = 'Is the sky blue?')
    def test_ask_question_with_empty_name(self, _input_name, _input_question):
        (
            'When name is empty and question is inputted, '
            'it is expected to output a string with '
            'the question and random Magic Eight Ball answer'
        )

        expected_answer = (
            rf'^\n'
            rf'Question: Is the sky blue\?\n'
            rf'Magic 8-Ball’s answer: {self.REGEX_ESCAPED_POSSIBLE_ANSWERS}$'
        )

        self.assertRegex(
            self.subject(),
            expected_answer
        )

    @skip('Have not figured out how to implement this test')
    def test_ask_question_with_empty_question(self):
        (
            'When name is inputted and question is empty, '
            'it is expected to prompt for the question again'
        )

        expected_prompt = 'You must ask a question!'

        self.assertRegex(
            self.subject(),
            expected_prompt
        )
