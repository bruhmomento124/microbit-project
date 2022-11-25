# microbit-project
small school project

the game itself: The game is a simple, bop-it like matching game. the user will run the program on a microbit and launch the python program on a connected computer, the computer will give an input that the user will have to match with the microbit.

accompyaning microbit program: https://makecode.microbit.org/_dHUhUaa404t3

as stated in main.py

- this code is pretty over commented, this is mainly because its a school project

- quick summary of how it all works:
- the microbit has a function to send serial data through a USB input, i assign a few actions on the accompanying microbit project (https://makecode.microbit.org/_dHUhUaa404t3)
- the microbit sends the data depending on what the function is, and the python project checks if its the correct data
 - this explanation isnt the greatest, but you can find more in depth explanations by reading the comments throughout the code


some notes: 
- unsure about COM ports, program may refuse to run as its coded for COM3 and this may change
- code is very overcommented, this is because its a school project
- its also a tad bit messy, it was pretty rushed and i'm unfamiliar with serial stuff
