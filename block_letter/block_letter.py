from functools import reduce

class BlockLetter:
  CHARACTER_HEIGHT = 7
  CHARACTER_WIDTH = 5
  ASCII_CHARACTER_INDEXES = {
    'H': (
      (0, 4),
      (0, 4),
      (0, 4),
      (0, 1, 2, 3, 4),
      (0, 4),
      (0, 4),
      (0, 4)
    ),
    'Q': (
      (1, 2, 3),
      (0, 4),
      (0, 4),
      (0, 4),
      (0, 4),
      (0, 3),
      (1, 2, 4)
    ),
    'V': (
      (0, 4),
      (0, 4),
      (0, 4),
      (0, 4),
      (0, 4),
      (1, 3),
      (2,)
    )
  }

  @classmethod
  def characters(klass, string):
    return '\n'.join(map(lambda row_index: klass.__ascii_row_for_characters([*string], row_index), range(klass.CHARACTER_HEIGHT)))

  @classmethod
  def __ascii_row_for_characters(klass, characters, row_index):
    return ' '.join(map(lambda character: klass.__ascii_row_for_character(character, klass.ASCII_CHARACTER_INDEXES[character][row_index]), characters))

  @classmethod
  def __ascii_row_for_character(klass, character, column_indexes):
    return reduce(lambda result, column_index: result + (' ', character)[column_index in column_indexes], range(klass.CHARACTER_WIDTH), '')
