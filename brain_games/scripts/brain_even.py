#!usr/bin/evn python3
import brain_games.scripts.brain_games
from random import randint
import prompt


def is_even(number):
    return number % 2 == 0 and 'yes' or 'no'


def main():
    name = brain_games.scripts.brain_games.main()
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count < 3:
        random_int = randint(1, 100)
        print(f'Question: {random_int}')
        answer = prompt.string('Your answer: ')
        correct_answer = is_even(random_int)
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'."
                  f"\nLet's try again, {name}")
            break
        count += 1
        if count == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
