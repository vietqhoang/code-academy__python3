'Module responsible for block letters'

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
        [_ascii_row_for_characters([*string], row_index) for row_index in range(CHARACTER_HEIGHT)]
    )

def _ascii_row_for_characters(characters, row_index):
    return ' '.join(
        [
            _ascii_row_for_character(character, ASCII_CHARACTER_INDEXES[character][row_index])
            for character in characters
        ]
    )

def _ascii_row_for_character(character, column_indexes):
    return ''.join(
        [
            (' ', character)[column_index in column_indexes]
            for column_index in range(CHARACTER_WIDTH)
        ]
    )
