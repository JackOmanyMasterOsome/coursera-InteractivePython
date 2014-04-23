"""Rock-paper-scissors-lizard-Spock template"""
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the follwing pass statement and fill in your code below
    if name.lower() == "rock":
        return 0
    elif name.lower() == "spock":
        return 1
    elif name.lower() == "paper":
        return 2
    elif name.lower() == "lizard":
        return 3
    elif name.lower() == "scissors":
        return 4
    else :
        return "ERROR IN : name_to_number"

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the follwing pass statement and fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "ERROR IN : number_to_name"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the follwing pass statement and fill in your code below
    # print a blank line to separate consecutive games
    print 
    # print "You will be playing against Sir Lancealot"
    # print out the message for the player's choice
    # print "And you have chosen : "+str(player_choice)
    print "Player chooses "+str(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    if player_number == "ERROR IN : name_to_number":
        print player_number
    # compute random guess for comp_number using random.randrange()
    else:
        comp_number = random.randrange(5)
        # convert comp_number to comp_choice using the function number_to_name()
        comp_choice = number_to_name(comp_number)
        if comp_choice == "ERROR IN : number_to_name":
            print comp_choice
        else:
            # print out the message for computer's choice
            # print "Sir Lancealot has chosen : "+str(comp_choice)
            print "Computer chooses "+str(comp_choice)
            # compute difference of comp_number and player_number modulo five
            difference = (comp_number - player_number) % 5
            # use if/elif/else to determine winner, print winner message
            # print "As per my calculations : ",
            if difference > 2:
                # print "You win!"
                print "Player",
            elif difference == 0:
                # print "Match Drawn :("
                print "Player and computer tie!"
                print "Nobody",
            elif difference <= 2:
                # print "Sir Lancealot wins!"
                print "Computer",
            else :
                print "ERROR IN: rpsls if statement"
                print "But someone",
            print "wins!"
        
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

