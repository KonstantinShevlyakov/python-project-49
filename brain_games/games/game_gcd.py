from random import randint
from math import gcd


ANNOUNCEMENT = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    correct_answer = gcd(num1, num2)
    return question, correct_answer
