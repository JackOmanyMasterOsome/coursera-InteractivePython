""""Guess the number" game"""

import random
import simplegui
import math
# global variables used
secret_number = 0
# Default game of range [0,100)
range_min = 0
range_max = 100
remaining_guesses = 0
# helper function to start and restart the game
def new_game():
    global secret_number, remaining_guesses
    secret_number = random.randrange(range_min, range_max)
    print "New Game in Range [%s , %s)"%(str(range_min),str(range_max))
    # reset remaining_guesses
    remaining_guesses = int(math.ceil(math.log((range_max - 0 + 1), 2)))
    print "You start with", display_remaining_guesses()
    
def display_remaining_guesses():
    display_string = ""
    if remaining_guesses > 0:
        display_string += str(remaining_guesses)
    elif remaining_guesses == 0 :
        display_string += "no more"
    else: 
        print "ERROR: why remaining_guesses < 0 coming here?"
    # Grammar Nazi
    if remaining_guesses == 1:
        display_string += " guess"
    else :
        display_string += " guesses"
    return display_string

# event handlers for control panel
def range100():
    global range_max, range_min
    range_max = 100
    range_min = 0
    print 
    print "="*42
    print 
    print "You have started a",
    new_game()  

def range1000():
    global range_max, range_min
    range_max = 1000
    range_min = 0
    print 
    print "="*42
    print 
    print "You have started a",
    new_game()
    
def input_guess(guess):
    global remaining_guesses
    print 
    guess_int = int(guess)
    print "You guessed", str(guess_int)
    remaining_guesses -= 1
    # out-of-range input
    if (guess_int >= range_max 
        or guess_int < range_min):
            print "Hey! Y U no enter in the correct range [%s , %s)"%(str(range_min),str(range_max))
    # The Game
    if guess_int < secret_number:
        print "Nope, Higher!"
    elif guess_int == secret_number:
        # game won
        print "Correct!"
        print "You've won this game with", display_remaining_guesses(), "remaining"
        print "The Secret Number was indeed :",str(secret_number)
        print "Congratulations!"
        print 
        print "="*42
        print
        print "I am starting a",
        new_game()
    elif guess_int > secret_number:
        print "Nope, Lower!"
    else:
        print "This game is wonking correctly"
        print "Please restart, and deduct my marks"
    if remaining_guesses > 0:
        print "You have", display_remaining_guesses(), "remaining"
        if remaining_guesses == 1:
            # last chance
            print "This is your last chance!"
    else :
        # lost game
        print "Oops!"
        print "You have exhausted all your chances :("
        print "The Secret Number was :", str(secret_number)
        print "Missed it by %s eh _/\_"%str(abs(secret_number - guess_int))
        print 
        print "="*42
        print
        print "Nevermind, I am starting a",
        new_game()
    
# create frame
frame_title = 'Guess the Number'
canvas_width = 350
canvas_height = 250
control_width = 250
guess_number_frame = simplegui.create_frame(frame_title, canvas_width, canvas_height, control_width)
# register event handlers for control elements
# Button100
button100_text = 'New Game with Range [0 , 100)'
button100_width = 250
button100 = guess_number_frame.add_button(button100_text,range100, button100_width)
# Button1000
button1000_text = 'New Game with Range [0 , 1000)'
button1000_width = button100_width
button1000 = guess_number_frame.add_button(button1000_text,range1000, button1000_width)
# Input_guess
input_guess_label = 'Enter Your Guess'
input_guess_width = button100_width
input_guess = guess_number_frame.add_input(input_guess_label, input_guess, input_guess_width)
# call new_game and start frame
print "Hello to my version of Guess the Number"
print "You can start a New Game any time by clicking one of the buttons on the right"
print 
print "="*42
print
print "For now, I am starting a", 
new_game()
guess_number_frame.start()

# always remember to check your completed program against the grading rubric
