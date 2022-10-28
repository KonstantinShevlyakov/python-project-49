from random import randint


def is_even(number):
    return number % 2 == 0 and 'yes' or 'no'


ANNOUNCEMENT = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    question = randint(1, 100)
    correct_answer = is_even(question)
    return question, correct_answer
