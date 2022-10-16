#!usr/bin/env
from random import randint
import prompt
import brain_games.scripts.brain_games
from math import gcd


def main():
    name = brain_games.scripts.brain_games.main()
    count = 0
    print('Find the greatest common divisor of given numbers.')
    while count < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')
        correct_answer = gcd(num1, num2)
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
