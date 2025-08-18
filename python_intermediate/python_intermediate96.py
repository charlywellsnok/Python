Step 2: Get Computer's Pick
Project Changes
Removed the pass statement inside the Game class
Added the __init__() method
Added the get_computer_pick method
import random

class Game:
    def __init__(self):
        # call the get_computer_pick() method 
        self.computer_pick = self.get_computer_pick()    
    
    def get_computer_pick(self):
        # get random number among 1, 2 and 3
        random_number = random.randint(1, 3)
        
        # possible options 
        options = {1: 'rock', 2: 'paper', 3: 'scissors'}
        
        # return the value present at random_number
        return options[random_number]
Here are the different parts of the program:

The __init__() method

When an object of the Game class is created, this method is called.

Inside this method, we have called the get_computer_pick() method which returns a value among 'rock', 'paper' and 'scissors' randomly. The return value is assigned to the computer_pick attribute.

The get_computer_pick() method

Inside the function, we have generated the random number between 1 and 3, which is assigned to the random_number variable. To generate a random number, we have imported the random module at the beginning of the code.

Then, we have created a dictionary with keys 1, 2 and 3 and their values 'rock', 'paper' and 'scissors' respectively.

Then, we have returned a random value among 'rock', 'paper' and 'scissors' using the return options[random_number] statement.

Confused about something? Ask a question!
