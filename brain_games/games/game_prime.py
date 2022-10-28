from random import randint
from math import sqrt


def is_prime(num):
    prime_flag = 0
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return 'yes'
        else:
            return 'no'
    else:
        return 'no'


ANNOUNCEMENT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_data():
    question = randint(0, 100)
    correct_answer = is_prime(question)
    return question, correct_answer
