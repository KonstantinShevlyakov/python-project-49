#!usr/bin/env python3
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    return name


def rounds_count():
    return 3


def get_result(answer, correct_answer, name, count):
    result = 0
    if count < rounds_count() - 1:
        if answer != str(correct_answer):
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}")
            return result
        else:
            print('Correct!')
            result = 1
            return result
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
