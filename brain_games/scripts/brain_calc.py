#!usr/bin/env python3
from random import randint, choice
import prompt
import brain_games.scripts.brain_games


def calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        return 'Wrong operator'


def main():
    name = brain_games.scripts.brain_games.main()
    count = 0
    operators = ['+', '-', '*']
    print('What is the result of the expression?')
    while count < 3:
        first_num = randint(1, 10)
        second_num = randint(1, 10)
        operator = choice(operators)
        print(f'Question:{first_num} {operator} {second_num}')
        answer = prompt.string('Your answer: ')
        correct_answer = calc(first_num, second_num, operator)
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}")
            break
        count += 1
        if count == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
