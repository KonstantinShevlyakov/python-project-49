from random import randint, choice


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


ANNOUNCEMENT = 'What number is missing in the progression?'


def get_game_data():
    question = get_progression()
    correct_answer = choice(question)
    index = question.index(correct_answer)
    question[index] = '..'
    question = ' '.join(str(element) for element in question)
    return question, correct_answer
