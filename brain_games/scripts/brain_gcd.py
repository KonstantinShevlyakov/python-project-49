#!usr/bin/env
from random import randint
import prompt
import brain_games.announcements
from brain_games.announcements import get_result
from math import gcd


def main():
    name = brain_games.announcements.main()
    count = 0
    print('Find the greatest common divisor of given numbers.')
    while count < brain_games.announcements.rounds_count():
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')
        correct_answer = gcd(num1, num2)
        result = get_result(answer, correct_answer, name, count)
        if result == 0:
            break
        else:
            count += 1


if __name__ == '__main__':
    main()
