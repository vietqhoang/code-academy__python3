import unittest
from block_letter import BlockLetter

class TestBlockLetter(unittest.TestCase):
  def setUp(self):
    self.block_letter = BlockLetter

  def test_characters_with_v(self):
    expectation = (
      'V   V\n'
      'V   V\n'
      'V   V\n'
      'V   V\n'
      'V   V\n'
      ' V V \n'
      '  V  '
    )

    self.assertEqual(self.block_letter.characters('V'), expectation)

  def test_characters_with_q(self):
    expectation = (
      ' QQQ \n'
      'Q   Q\n'
      'Q   Q\n'
      'Q   Q\n'
      'Q   Q\n'
      'Q  Q \n'
      ' QQ Q'
    )

    self.assertEqual(self.block_letter.characters('Q'), expectation)

  def test_characters_with_h(self):
    expectation = (
      'H   H\n'
      'H   H\n'
      'H   H\n'
      'HHHHH\n'
      'H   H\n'
      'H   H\n'
      'H   H'
    )

    self.assertEqual(self.block_letter.characters('H'), expectation)

  def test_characters_with_vqh(self):
    expectation = (
      'V   V  QQQ  H   H\n'
      'V   V Q   Q H   H\n'
      'V   V Q   Q H   H\n'
      'V   V Q   Q HHHHH\n'
      'V   V Q   Q H   H\n'
      ' V V  Q  Q  H   H\n'
      '  V    QQ Q H   H'
    )

    self.assertEqual(self.block_letter.characters('VQH'), expectation)
