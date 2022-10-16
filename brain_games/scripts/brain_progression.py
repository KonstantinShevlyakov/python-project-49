#!usr/bin/env python3
from random import randint, choice
import brain_games.scripts.brain_games
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
    name = brain_games.scripts.brain_games.main()
    count = 0
    print('What number is missing in the progression?')
    while count < 3:
        progression = get_progression()
        correct_answer = choice(progression)
        index = progression.index(correct_answer)
        progression[index] = '..'
        progression = ' '.join(str(element) for element in progression)
        print(f'Question: {progression}')
        answer = prompt.string('Your answer: ')
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
