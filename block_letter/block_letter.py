'Module responsible for block letters'

from functools import reduce

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

def characters_to_block_letters(string):
    'Returns string as ASCII block letters'

    return '\n'.join(
        map(
            lambda row_index: _ascii_row_for_characters([*string], row_index),
            range(CHARACTER_HEIGHT)
        )
    )

def _ascii_row_for_characters(characters, row_index):
    return ' '.join(
        map(
            lambda character: _ascii_row_for_character(
                character, ASCII_CHARACTER_INDEXES[character][row_index]
            ),
            characters
        )
    )

def _ascii_row_for_character(character, column_indexes):
    return reduce(
        lambda result, column_index: result + (' ', character)[column_index in column_indexes],
        range(CHARACTER_WIDTH),
        ''
    )
