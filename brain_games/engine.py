#!usr/bin/env python3
import prompt


def rounds_count():
    return 3


def main(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    announcement = game.get_announcement()
    print(announcement)
    count = 0
    while count < rounds_count():
        question, correct_answer = game.main()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != str(correct_answer):
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
        elif count == rounds_count() - 1:
            print(f'Congratulations, {name}!')
            break
        else:
            print('Correct!')
            count += 1


if __name__ == '__main__':
    main()
