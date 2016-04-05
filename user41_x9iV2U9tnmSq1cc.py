# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

no_of_chances_used = 0
secret_number = 0
range = 100 # default range is [0,100)


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    global no_of_chances_used
    no_of_chances_used = 0 # initializing this to 0 for new game
    
    global secret_number
    
    
    if range == 100:
        secret_number = random.randrange(0, 100)
        print ""
        print "New game. Range is from 0 to 100"
        print "Number of remaining guesses is ", int(math.ceil(math.log(100, 2)))
    else:
        secret_number = random.randrange(0, 1000)
        print ""
        print "New game. Range is from 0 to 1000"
        print "Number of remaining guesses is ", int(math.ceil(math.log(1000, 2)))

    return
 
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global range
    range = 100
    new_game()
    
    return

def range1000():
    # button that changes the range to [0,1000) and starts a new game     

    global range
    range = 1000
    new_game()
    
    return
    
def input_guess(guess):
    # main game logic goes here	
    print ""
    print "Guess was ", guess
    global no_of_chances_used
    no_of_chances_used += 1
    
    # Calculating the max no of chances for a given range
    max_no_of_chances = 0
    if range == 100:
        max_no_of_chances = int(math.ceil(math.log(100, 2)))
    else:
        max_no_of_chances = int(math.ceil(math.log(1000, 2)))
        
    #If no chances left, start new game
    #otherwise continue with the game
    if max_no_of_chances - no_of_chances_used < 0:
        print "You loose! No more guesses left."
        new_game()
        return
    else:
        if range == 100:
            print "Number of remaining guesses is ", max_no_of_chances - no_of_chances_used
        else:
            print "Number of remaining guesses is ", max_no_of_chances - no_of_chances_used
    
    guess_value = int(guess)
    if guess_value > secret_number:
        print "Lower!"
    elif guess_value < secret_number:
        print "Higher!"
    else:
        print "Correct!"
        new_game()
        
    return

    
# create frame
frame = simplegui.create_frame("Guess Number", 300, 300, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
