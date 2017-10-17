#! python
import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

guess = ''
logging.debug("Start of program")
while guess not in ('heads', 'tails'): # bad check to end loop
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug("Choice is %s" %guess)
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    logging.debug("Toss result is %d" %toss)
    if toss == guess: # comparing string entry with number toss
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guesss = input() # wrong variable declaration
        logging.debug("Second choice is %s" %guess)
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
    logging.debug("Loop end. Guess is %s" %guess)
logging.debug('End of program')
