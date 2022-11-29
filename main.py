"""this code is pretty over commented, this is mainly because its a school project
quick summary of how it all works:

the microbit has a function to send serial data through a USB input, i assign a few actions on the accompanying microbit project (https://makecode.microbit.org/_dHUhUaa404t3)
the microbit sends the data depending on what the function is, and the python project checks if its the correct data
this explanation isnt the greatest, but you can find more in depth explanations by reading the comments throughout the code
"""

import serial, random, time
# this serial port can change, microbit is weird
ser = serial.Serial('COM3', 115200) # serial port and baud rate
score = 0 # score variable
try: # if score.txt exists, print "High Score: " and the score
    with open("score.txt", "r") as f:
        print("High Score: " + f.read())
        ser.write(("High Score: " + f.read()).encode('utf-8')) # send the high score to the microbit
except FileNotFoundError:
    print("No high score yet!")

# explanation
print("this is a simple matching game, the game will select a random option from the microbit and you will have to match it by selecting the same option on the microbit")
print("the options are: a, ab, b, shake")
input("press enter to start the game") # using an input() to pause until user input
# there are better ways to go about this but its in a function for easier looping and testing stuff
def game():
    options = ["a", "ab", "b", "shake"] # available functions from the microbit
    choice = random.choice(options) # making a variable for easier use
    print(choice)
    i = True
    while i == True:
        # choices = [""] # unused
        data = ser.readline().decode('utf-8').rstrip() # reads serial data and strips excess formatting
        if data == choice: # this code could look wayyyy better, but its rushed
            print("correct choice" + "\n" * 4) # the \n * 4 is to separate for the next game
            global score
            score += 1
            i = False
            score += 1 # self explanatory
        else:
            print("nope, you selected " + data + "\n" * 4) 
            ser.write(("Game Over! Final score: " + str(score) + "!").encode('utf-8')) # sends the final score to the microbit
            try: # if the score is higher than the high score, it will overwrite the high score
                with open("score.txt", "r") as f:
                    if score > int(f.read()):
                        with open("score.txt", "w") as f:
                            f.write(str(score))
            except FileNotFoundError:
                with open("score.txt", "w") as f:
                    f.write(str(score))
            print("final score: " + str(score))
            time.sleep(0.5)
            exit()

while True:
    game()
