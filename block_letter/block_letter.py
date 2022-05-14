'Module responsible for block letters'

from functools import reduce

class BlockLetter:
    'Class which transforms a string into block letters'

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
    def characters(cls, string):
        'Returns string as ASCII block letters'

        return '\n'.join(
            map(
                lambda row_index: cls._ascii_row_for_characters([*string], row_index),
                range(cls.CHARACTER_HEIGHT)
            )
        )

    @classmethod
    def _ascii_row_for_characters(cls, characters, row_index):
        return ' '.join(
            map(
                lambda character: cls._ascii_row_for_character(
                    character, cls.ASCII_CHARACTER_INDEXES[character][row_index]
                ),
                characters
            )
        )

    @classmethod
    def _ascii_row_for_character(cls, character, column_indexes):
        return reduce(
            lambda result, column_index: result + (' ', character)[column_index in column_indexes],
            range(cls.CHARACTER_WIDTH),
            ''
        )
