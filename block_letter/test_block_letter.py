'Unit tests for block_letter'

from unittest import TestCase
from block_letter import characters_to_block_letters

class TestCharactersToBlockLetter(TestCase):
    'Tests for `characters_to_block_letter`'

    def setUp(self):
        self.subject = characters_to_block_letters

    def test_characters_to_block_letters_with_v(self):
        'When the argument is is an `V`, it is expected to output the `V` block letter'

        expectation = (
            'V   V\n'
            'V   V\n'
            'V   V\n'
            'V   V\n'
            'V   V\n'
            ' V V \n'
            '  V  '
        )

        self.assertEqual(self.subject('V'), expectation)

    def test_characters_to_block_letters_with_q(self):
        'When the argument is is an `Q`, it is expected to output the `Q` block letter'

        expectation = (
            ' QQQ \n'
            'Q   Q\n'
            'Q   Q\n'
            'Q   Q\n'
            'Q   Q\n'
            'Q  Q \n'
            ' QQ Q'
        )

        self.assertEqual(self.subject('Q'), expectation)

    def test_characters_to_block_letters_with_h(self):
        'When the argument is is an `H`, it is expected to output the `H` block letter'

        expectation = (
            'H   H\n'
            'H   H\n'
            'H   H\n'
            'HHHHH\n'
            'H   H\n'
            'H   H\n'
            'H   H'
        )

        self.assertEqual(self.subject('H'), expectation)

    def test_characters_to_block_letters_with_vqh(self):
        (
            'When the argument is multiple characters, '
            'it is expected to output characters from left-to-right'
        )

        expectation = (
            'V   V  QQQ  H   H\n'
            'V   V Q   Q H   H\n'
            'V   V Q   Q H   H\n'
            'V   V Q   Q HHHHH\n'
            'V   V Q   Q H   H\n'
            ' V V  Q  Q  H   H\n'
            '  V    QQ Q H   H'
        )

        self.assertEqual(self.subject('VQH'), expectation)
