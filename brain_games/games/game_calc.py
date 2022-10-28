from random import randint, choice


def calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        return 'Wrong operator'


ANNOUNCEMENT = 'What is the result of the expression?'


def get_game_data():
    operators = ['+', '-', '*']
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    operator = choice(operators)
    correct_answer = calc(num1, num2, operator)
    question = f'{num1} {operator} {num2}'
    return question, correct_answer
