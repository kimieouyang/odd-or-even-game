# Add your Python code here. E.g.
from microbit import *
import random 
# Intro msg to welcome and provide instruction of the game
# There are three types of answer status: correct, wrong, and timeout
# No matter the player answer it correctly or not, or even timeout, 
# the new random number would keep showing after the status is defined
# So player can keep playing non-stop
display.show(Image.HAPPY)
sleep(2000)
display.scroll('Press btn A when is odd number')
sleep(2000)
display.scroll('Press btn B when is even number')
sleep(2000)
display.show(Image.HEART)
sleep(1000)
display.scroll('means correct')
sleep(2000)
display.show(Image.SAD)
sleep(1000)
display.scroll('means wrong')
sleep(1000)
display.show(Image.SKULL)
sleep(1000)
display.scroll('means timeout')
sleep(1000)
display.scroll('Lets start!')
sleep(500)

# Setup for this game
game_started = running_time()
# Use running time funtion to track how long a game was started, 
# and save it as one variable for future time related function usage
game_over = 10000
# Set up a game over time, this variable would be used in a timeout condition when no button is pressed, 
# the system would determine as a timeout and start over a new game
myrandnum = random.randint(1, 9)
# I only pick random numbers from 1-9 for this game by importing random function

while True:
    # This is the loop of the game
    display.show(myrandnum)
    # After the system pick a random number from 1-9, display on microbit 
    is_even = myrandnum % 2 == 0
    # Set a variable for defining true or fale statement, here set myrandnum % 2 ==0 is true
    if button_a.is_pressed():
    # Btn A represent odd number in my game
        if is_even:
            display.show(Image.SAD)
            # if button A is pressed and the number is an even number
            # this is the wrong answer. Display a sad face
        else:
            display.show(Image.HEART)
            # if button A is pressed and the number is an odd number 
            # this is the right answer. Display a happy face
        sleep(2000)
        # Let the sad face or heart display for 2 seconds
        myrandnum = random.randint(1, 9)
        # Pick a random number from 1-9 again
        game_started = running_time()
        # Capture the current running time as the new start time for new game
        continue
        # This make the loop starts over to display a random number
    
    if button_b.is_pressed():
    # Btn B represent even number in my game
        if is_even:
            display.show(Image.HEART)
            # if button B is pressed and the number is an even number
            # this is the right answer. Display a heart
        else:
            display.show(Image.SAD)
            # if button B is pressed and the number is an odd number
            # this is the wrong answer. Display a sad face
        sleep(2000)
        # Let the sad face or heart display for 2 seconds
        myrandnum = random.randint(1, 9)
        # Pick a random number from 1-9 again
        game_started = running_time()
        # Capture the current running time as the new start time for new game
        continue
        # This make the loop starts over to display a random number
    
    waiting = running_time() - game_started
    # Get the current time and subtract the game starting time and define it as the waiting time
    # Waiting time is for the time out condition when there is no interaction happens
    if waiting >= game_over:
        # I've set the "time out" time as 10 seconds, so if no interaction happens at all for 10 second or more
        # That means time out 
        display.show(Image.SKULL)
        # skull image indicate "time out" and the hint for restart the game
        sleep(2000)
        # Let the skull display for 2 seconds
        myrandnum = random.randint(1, 9)
        # Pick a random number from 1-9 
        game_started = running_time()
        # Capture the current running time as the new start time for new game
        continue
        # This make the loop starts over to display a random number
        

