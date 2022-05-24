'Module responsible for Magic Eight Ball game'

from random import choice

ANSWERS = [
    'Yes - definitely.',
    'It is decidedly so.',
    'Without a doubt.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
]

def ask_question():
    (
        'Prompts user input for name and question. '
        'Outputs string containing summary of inputs and the Magic Eight Ball answer'
    )

    return _result(_input_name(), _input_question())

def _input_name():
    return _input_with_whitespace('What is your name?')

def _input_question(repeated_prompt = False):
    question_prompt = 'You must ask a question!' if repeated_prompt else 'What is your question?'

    return (
        _input_with_whitespace(question_prompt) or
        _input_question(repeated_prompt = True)
    )

def _input_with_whitespace(prompt):
    return input(f'{prompt} ').strip()

def _result(name, question):
    question_heading = f'{name} asks' if name else 'Question'

    return (
        f'\n'
        f'{question_heading}: {question}\n'
        f'Magic 8-Ball’s answer: {choice(ANSWERS)}'
    )
