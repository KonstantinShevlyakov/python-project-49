#!usr/bin/env python3
from random import randint
from math import sqrt
import brain_games.announcements
# from brain_games.announcements import get_result
# import prompt


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
    announcement = 'Answer "yes" if given number is prime. ' \
                   'Otherwise answer "no".'
    count = 0
    game_data = []
    while count < brain_games.announcements.rounds_count():
        num = randint(0, 100)
        correct_answer = is_prime(num)
        game_data.append((str(num), str(correct_answer)))
        count += 1
    return brain_games.announcements.main(announcement, game_data)

# def main():
#     name = brain_games.announcements.main()
#     count = 0
#     print('Answer "yes" if given number is prime. Otherwise answer "no".')
#     while count < brain_games.announcements.rounds_count():
#         number = randint(0, 100)
#         print(f'Question: {number}')
#         answer = prompt.string('Your answer: ')
#         correct_answer = is_prime(number)
#         result = get_result(answer, correct_answer, name, count)
#         if result == 0:
#             break
#         else:
#             count += 1


if __name__ == '__main__':
    main()
