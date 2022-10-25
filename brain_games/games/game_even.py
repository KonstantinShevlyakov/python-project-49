#!usr/bin/evn python3
from random import randint


def is_even(number):
    return number % 2 == 0 and 'yes' or 'no'


def get_announcement():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    question = randint(1, 100)
    correct_answer = is_even(question)
    return question, correct_answer


if __name__ == '__main__':
    main()
