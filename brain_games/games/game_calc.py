#!usr/bin/env python3
from random import randint, choice
# import prompt
import brain_games.announcements
# from brain_games.announcements import get_result


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
    announcement = 'What is the result of the expression?'
    count = 0
    operators = ['+', '-', '*']
    game_data = []
    while count < brain_games.announcements.rounds_count():
        first_num = randint(1, 10)
        second_num = randint(1, 10)
        operator = choice(operators)
        correct_answer = calc(first_num, second_num, operator)
        question = f'{first_num} {operator} {second_num}'
        game_data.append((question, str(correct_answer)))
        count += 1
    return brain_games.announcements.main(announcement, game_data)


# def main():
#     name = brain_games.announcements.main()
#     count = 0
#     operators = ['+', '-', '*']
#     print('What is the result of the expression?')
#     while count < brain_games.announcements.rounds_count():
#         first_num = randint(1, 10)
#         second_num = randint(1, 10)
#         operator = choice(operators)
#         print(f'Question: {first_num} {operator} {second_num}')
#         answer = prompt.string('Your answer: ')
#         correct_answer = calc(first_num, second_num, operator)
#         result = get_result(answer, correct_answer, name, count)
#         if result == 0:
#             break
#         else:
#             count += 1


if __name__ == '__main__':
    main()
