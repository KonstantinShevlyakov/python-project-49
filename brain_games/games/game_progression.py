#!usr/bin/env python3
from random import randint, choice
import brain_games.announcements
from brain_games.announcements import get_result
import prompt


def get_progression():
    progression = []
    len_progression = randint(5, 10)
    step = randint(2, 10)
    element = randint(0, 50)
    progression.append(element)
    i = 0
    while i < len_progression:
        element += step
        progression.append(element)
        i += 1
    return progression


def main():
    name = brain_games.announcements.main()
    count = 0
    print('What number is missing in the progression?')
    while count < brain_games.announcements.rounds_count():
        progression = get_progression()
        correct_answer = choice(progression)
        index = progression.index(correct_answer)
        progression[index] = '..'
        progression = ' '.join(str(element) for element in progression)
        print(f'Question: {progression}')
        answer = prompt.string('Your answer: ')
        result = get_result(answer, correct_answer, name, count)
        if result == 0:
            break
        else:
            count += 1


if __name__ == '__main__':
    main()
