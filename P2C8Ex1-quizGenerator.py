#! python3

import random
import os

QUIZ_FOLDER = './P2C8Ex2-GeneratedQuiz'

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico'
    : 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia'
    : 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

if not os.path.exists(QUIZ_FOLDER):
    os.mkdir(QUIZ_FOLDER)

os.chdir(QUIZ_FOLDER)


for quizNum in range(5):

    quizFile = open('captialquiz-%s.txt' %(quizNum + 1), 'w')
    answerKeyFile = open('answerkey-%s.txt' %(quizNum + 1), 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for qnNum in range(50):

        correctAnswer = capitals[states[qnNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('%s. What is the capital of %s?\n' % (qnNum + 1, states[qnNum]))

        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' %(quizNum +1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
