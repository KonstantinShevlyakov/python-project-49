#!usr/bin/env python3
import prompt


# def main():
#     print('Welcome to the Brain Games!')
#     name = prompt.string('May I have your name? ')
#     print(f'Hello, {name}!')
#     return name


def rounds_count():
    return 3


def main(announcement, game_data):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(announcement)
    count = 0
    lost = False
    while count < rounds_count():
        print(f'Question: {game_data[count][0]}')
        answer = prompt.string('Your answer: ')
        correct_answer = game_data[count][1]
        if get_result(answer, correct_answer) == 0:
            lost = True
            break
        else:
            print('Correct!')
            count += 1
    if lost is True:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'."
              f"\nLet's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')


def get_result(answer, correct_answer):
    result = 0
    if answer != correct_answer:
        return result
    else:
        result = 1
        return result


# def get_result(answer, correct_answer, name, count):
#     result = 0
#     if count < rounds_count():
#         if answer != str(correct_answer):
#             print(f"'{answer}' is wrong answer ;(. "
#                   f"Correct answer was '{correct_answer}'."
#                   f"\nLet's try again, {name}!")
#             return result
#         elif count < rounds_count() - 1:
#             result = 1
#             print('Correct!')
#             return result
#         else:
#             print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
