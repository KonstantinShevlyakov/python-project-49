#!usr/bin/env
from random import randint
from math import gcd


def get_announcement():
    return 'Find the greatest common divisor of given numbers.'


def main():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    correct_answer = gcd(num1, num2)
    return question, correct_answer


if __name__ == '__main__':
    main()
