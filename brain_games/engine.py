import prompt


ROUNDS = 3


def main(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    announcement = game.ANNOUNCEMENT
    print(announcement)
    count = 0
    while count < ROUNDS:
        question, correct_answer = game.get_game_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != str(correct_answer):
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
        elif count == ROUNDS - 1:
            print(f'Congratulations, {name}!')
            break
        else:
            print('Correct!')
            count += 1
