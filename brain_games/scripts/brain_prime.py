#!usr/bin/env python3
from random import randint
from math import sqrt
import brain_games.scripts.brain_games
import prompt


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


def main():
    name = brain_games.scripts.brain_games.main()
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count < 3:
        number = randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        correct_answer = is_prime(number)
        if answer != str(correct_answer):
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}")
            break
        count += 1
        if count == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
