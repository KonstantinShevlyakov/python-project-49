#!usr/bin/evn python3
# import brain_games.scripts.brain_games
from random import randint
import brain_games.announcements
import prompt


def is_even(number):
    return number % 2 == 0 and 'yes' or 'no'


def main():
    name = brain_games.announcements.main()
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count < brain_games.announcements.rounds_count():
        random_int = randint(1, 100)
        print(f'Question: {random_int}')
        answer = prompt.string('Your answer: ')
        correct_answer = is_even(random_int)
        result = brain_games.announcements.get_result(answer, correct_answer, name, count)
        if result == 0:
            break
        elif result == 2:
            break
        else:
            count += 1


if __name__ == '__main__':
    main()
